// Copyright (c) 2024, Sofian Saleh and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Test Stock ageing"] = {
  filters: [
    {
      fieldname: "company",
      label: __("Company"),
      fieldtype: "Link",
      options: "Company",
      default: frappe.defaults.get_user_default("Company"),
      reqd: 1,
    },
    {
      fieldname: "to_date",
      label: __("As On Date"),
      fieldtype: "Date",
      default: frappe.datetime.get_today(),
      reqd: 1,
    },
    {
      fieldname: "item_code",
      label: __("Item"),
      fieldtype: "Link",
      options: "Item",
    },
  ],
};
