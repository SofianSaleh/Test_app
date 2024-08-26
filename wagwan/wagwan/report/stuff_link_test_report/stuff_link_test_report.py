# Copyright (c) 2024, Sofian Saleh and contributors
# For license information, please see license.txt

import frappe


def get_data(filters):
	query = f"""
				SELECT e.name, e.default_shift, e.employee_name,
					(SELECT JSON_ARRAYAGG(
                            JSON_OBJECT(
                                'time',ec.time, 
                                'employee_name',ec.name , 
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
                            WHERE ec.employee = e.name)
				FROM `tabEmployee` AS e
				WHERE e.status = 'Active';
			"""
	res = frappe.db.sql(query, as_dict=True)

	print(res)


def execute(filters=None):
	columns, data = [], get_data(filters)
	return columns, data
