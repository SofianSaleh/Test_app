import frappe


@frappe.whitelist()
def test_1():
    doc = frappe.get_doc("Employee", "HR-EMP-00001")
    return f"{doc.employee_name}, {doc.gender}"


def validate(doc, event):
    frappe.throw("err")


@frappe.whitelist()
def get_customers(item_code: str):
    item_code1 = frappe.form_dict["item_code"]
    print(item_code)

    return frappe.get_all("Customer", fields=["name", "customer_type"])


# frappe.get_all("Item", filters={"item_name": ["not in", ["a", "b"]]})
@frappe.whitelist()
def get_outliar():
    data = frappe.db.get_all(
        "Sales Invoice", fields=["name", "custom_customer_outstanding_after_invoice"]
    )
    t = []
    for d in data:
        # if d.custom_customer_outstanding_after_invoice:

        # frappe.db.set_value(
        #     "Sales Invoice",
        #     d.name,
        #     "custom_customer_outstanding_after_invoice",
        #     float(d.custom_customer_outstanding_after_invoice),
        # )
        # frappe.db.commit()
        t.append(
            {
                "name": d.name,
                "data": d.custom_customer_outstanding_after_invoice,
                "t": type(d.custom_customer_outstanding_after_invoice),
                "is_number": has_numbers(
                    d.custom_customer_outstanding_after_invoice, d.name
                ),
            }
        )

    # frappe.log_error("tsts", t)
    return t


import re


def has_numbers(inputString, invoice):
    try:
        if inputString:
            a = bool(re.search(r"\d", inputString))
            return a
    except Exception as e:
        frappe.log_error("err", e)
        return False
