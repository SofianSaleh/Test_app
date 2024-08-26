# Copyright (c) 2024, Sofian Saleh and contributors
# For license information, please see license.txt

import datetime
import json
import frappe
from calendar import day_abbr, monthrange
from itertools import groupby
from typing import Dict, List, Optional, Tuple

import frappe
from frappe import _
from frappe.query_builder.functions import Count, Extract, Sum
from frappe.utils import cint, cstr, getdate
from frappe.utils.data import get_first_day, get_last_day

Filters = frappe._dict


def get_sql_filters(filters):
	start_date = frappe.db.escape(
		f"{get_first_day(getdate(f'{filters.year}-{filters.month}-01'))}"
	)
	end_date = frappe.db.escape(
		f"{get_last_day(getdate(f'{filters.year}-{filters.month}-01'))}"
	)
	
	employee_filter = ''
	if filters.get("employee"):
		escaped_employee_input = frappe.db.escape(filters.get("employee"))
		employee_filter = f"AND e.name = {escaped_employee_input}"
	return {
		"start_date": start_date,
		"end_date": end_date,
		"employee_filter": employee_filter,
	}


def get_columns(filters: Filters) -> List[Dict]:
    columns = [
       {
            "label": _("Employee"),
            "fieldname": "employee",
            'fieldtype': 'Link',
            'options': 'Employee',
            'freeze': True,
            'width': 150
        }, 
        {
            "label": _("Shift"),
            "fieldname": "shift",
            "fieldtype": "Link",
            "options": "Shift Type",
            "width": 120,
        },
    ]

    columns.extend(get_columns_for_days(filters))

    return columns


def get_columns_for_leave_types() -> List[Dict]:
    leave_types = frappe.db.get_all("Leave Type", pluck="name")
    types = []
    for entry in leave_types:
        types.append(
            {
                "label": entry,
                "fieldname": frappe.scrub(entry),
                "fieldtype": "Float",
                "width": 120,
            }
        )

    return types


def get_columns_for_days(filters: Filters) -> List[Dict]:
    total_days = get_total_days_in_month(filters)
    days = []

    for day in range(1, total_days + 1):
        day = cstr(day)
        # forms the dates from selected year and month from filters
        date = "{}-{}-{}".format(cstr(filters.year), cstr(filters.month), day)
        # gets abbr from weekday number
        weekday = day_abbr[getdate(date).weekday()]
        # sets days as 1 Mon, 2 Tue, 3 Wed
        label = "{} {}".format(day, weekday)
        days.append(
            {"label": label, "fieldtype": "Data", "fieldname": day, "width": 65}
        )

    return days


def get_total_days_in_month(filters: Filters) -> int:
    return monthrange(cint(filters.year), cint(filters.month))[1]


def get_data(filters):
    sql_filters = get_sql_filters(filters)
    res = frappe.db.sql(
        f"""
						SELECT 
                        e.name as employee, e.default_shift as shift, e.employee_name,
                        (SELECT JSON_ARRAYAGG(
                            JSON_OBJECT(
                                'time',ec.time, 
                                'employee_name',ec.employee , 
                                'log_type',ec.log_type, 
                                'location', ec.device_id,
                                'device_id', ec.slm_device_id, 
                                'device_ip', ec.slm_device_ip, 
                                'device_model', ec.slm_device_model, 
                                'device_platform',ec.slm_device_platform, 
                                'device_platform', ec.slm_device_platform,
                                'shift', ec.shift
                            ) ORDER BY ec.creation) 
                            FROM `tabEmployee Checkin` 
                            AS ec 
                            WHERE ec.employee = e.name
					  		AND ec.time >= {sql_filters['start_date']} AND ec.time <= {sql_filters['end_date']}
					  ) AS checkin_list,

					  (SELECT 
                            JSON_ARRAYAGG(
                                JSON_OBJECT(
                                    'name', a.name,
                                    'status', a.status, 
                                    'employee_name', a.name, 
                                    'attendance_date',a.attendance_date, 
                                    'leave_application',a.leave_application,
                                    'leave_type',a.leave_type,
                                    'shift', a.shift
                                ) ORDER BY a.creation) 
                            FROM `tabAttendance` 
                            AS a 
                            WHERE a.employee = e.name 
                            # AND a.status = 'On Leave'
                            AND a.docstatus = 1
                            )
                            AS attendance_list

					  FROM `tabEmployee` AS e
					WHERE e.status = 'Active'
						{sql_filters['employee_filter']}
					  """,
        as_dict=True,
    )

    checkin_stack = []
    checkins = []
    for employee in res:
        attended_shift = []

        employee["checkin_list"] = (
            json.loads(employee["checkin_list"]) if employee["checkin_list"] else []
        )
        employee["attendance_list"] = (
            json.loads(employee["attendance_list"])
            if employee["attendance_list"]
            else []
        )

        for check in employee["checkin_list"]:
            if check["log_type"] == "IN":

                if checkin_stack and len(checkin_stack) > 0:
                    if getdate(checkin_stack[-1]["time"]) != getdate(check["time"]):
                        checkin_stack.pop()
                        checkin_stack.append(check)
                else:
                    checkin_stack.append(check)
            elif check["log_type"] == "OUT":
                if len(checkin_stack) > 0:
                    checkin = checkin_stack.pop()
                    if getdate(check["time"]) != getdate(checkin["time"]):
                        checkin_stack.append(checkin)
                    else:
                        if not check["shift"]:
                            day = datetime.datetime.strptime(
                                check["time"], "%Y-%m-%d %H:%M:%S.%f"
                            ).day
                            employee[str(day)] = "OK"
                        else:
                            # ! Get shift time
                            # ! Calculate worked time
                            day = datetime.datetime.strptime(
                                check["time"], "%Y-%m-%d %H:%M:%S.%f"
                            ).day
                            employee[str(day)] = "OK"
                            attended_shift.append(check)
                        checkins.append(checkin)
                        checkins.append(check)
        for attendance in employee["attendance_list"]:
            day = datetime.datetime.strptime(
                attendance["attendance_date"], "%Y-%m-%d"
            ).day
            employee[str(day)] = "Leave"

        checkin_stack = []
        employee["checkin_list"] = checkins
        checkins = []
    return res


def execute(filters=None):
    columns, data = get_columns(filters), get_data(filters)
    return columns, data
