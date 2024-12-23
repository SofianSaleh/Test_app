import frappe
import frappe.utils


def get_context(ctx):
    ctx.no_cache = 1
    try:
        page_size = 5

        # Get the current page number from query parameters (default to 1)
        current_page = int(frappe.form_dict.page or 1)
        total_items = frappe.db.count("Item")

        # Calculate the offset (skip)
        start = (current_page - 1) * page_size

        items = frappe.get_all(
            "Item",
            fields=["name", "item_name", "image"],
            limit_start=start,
            limit_page_length=page_size,
        )
        for item in items:
            item["url"] = frappe.utils.get_url_to_form("Item", item["name"])
        ctx["items"] = items

        ctx.total_pages = (total_items + page_size - 1) // page_size
        ctx.current_page = current_page
        ctx.page_size = page_size

    except Exception as e:
        print(e)
