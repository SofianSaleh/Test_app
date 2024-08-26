import frappe


@frappe.whitelist()
def test_1():
    doc = frappe.get_doc("Employee", "HR-EMP-00001")
    return f"{doc.employee_name}, {doc.gender}"
