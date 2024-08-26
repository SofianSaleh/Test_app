// Copyright (c) 2024, Sofian Saleh and contributors
// For license information, please see license.txt
/* eslint-disable */

var i = 0
frappe.query_reports["Test Daily Attendance"] = {

	formatter: function (value, row, column, data, default_formatter) {
		value = default_formatter(value, row, column, data);
		i+=1
		// console.log(value)
		if (value === 'OK'){
			console.log(value, data)
			console.log(i)
			// console.log(row)
			value = "<span style='color:green; font-weight:bold'>" + value + "</span>";
		// 				'`<div class="dt-cell__content dt-cell__content--col-22" title="OK" style="background-color: aquamarine;">${value}</div>`		}
		}else if (value === 'Leave'){
			value = "<span style='color:blue; font-weight:bold'>" + value + "</span>";

		}else if (value === '' && column.id !== 'shift'){
			value = "<span style='color:red; font-weight:bold'>" + 'Absent' + "</span>";
		}

		return value 
	},
	"filters": [
		{
			"fieldname": "month",
			"label": __("Month"),
			"fieldtype": "Select",
			"reqd": 1 ,
			"options": [
				{ "value": 1, "label": __("Jan") },
				{ "value": 2, "label": __("Feb") },
				{ "value": 3, "label": __("Mar") },
				{ "value": 4, "label": __("Apr") },
				{ "value": 5, "label": __("May") },
				{ "value": 6, "label": __("June") },
				{ "value": 7, "label": __("July") },
				{ "value": 8, "label": __("Aug") },
				{ "value": 9, "label": __("Sep") },
				{ "value": 10, "label": __("Oct") },
				{ "value": 11, "label": __("Nov") },
				{ "value": 12, "label": __("Dec") },
			],
			"default": frappe.datetime.str_to_obj(frappe.datetime.get_today()).getMonth() + 1
		},
		{
			"fieldname":"year",
			"label": __("Year"),
			"fieldtype": "Select",
			"reqd": 1
		},
		{
			"fieldname":"employee",
			"label": __("Employee"),
			"fieldtype": "Link",
			"options": "Employee",
			get_query: () => {
				var company = frappe.query_report.get_filter_value('company');
				return {
					filters: {
						'company': company
					}
				};
			}
		},
		{
			"fieldname":"company",
			"label": __("Company"),
			"fieldtype": "Link",
			"options": "Company",
			"default": frappe.defaults.get_user_default("Company"),
			"reqd": 1
		},
		// {
		// 	"fieldname":"group_by",
		// 	"label": __("Group By"),
		// 	"fieldtype": "Select",
		// 	"options": ["","Branch","Grade","Department","Designation"]
		// },
		// {
		// 	"fieldname":"summarized_view",
		// 	"label": __("Summarized View"),
		// 	"fieldtype": "Check",
		// 	"Default": 0,
		// }
	],
	onload: function() {
		return  frappe.call({
			method: "hrms.hr.report.monthly_attendance_sheet.monthly_attendance_sheet.get_attendance_years",
			callback: function(r) {
				var year_filter = frappe.query_report.get_filter('year');
				year_filter.df.options = r.message;
				year_filter.df.default = r.message.split("\n")[0];
				year_filter.refresh();
				year_filter.set_input(year_filter.df.default);
			}
		});
	},
};
