app_name = "wagwan"
app_title = "Wagwan"
app_publisher = "Sofian Saleh"
app_description = "wagwan"
app_email = "s.saleh@ebkar.ly"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/wagwan/css/wagwan.css"
# app_include_js = "/assets/wagwan/js/wagwan.js"

# include js, css files in header of web template
# web_include_css = "/assets/wagwan/css/wagwan.css"
# web_include_js = "/assets/wagwan/js/wagwan.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "wagwan/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
doctype_js = {"Item" : "public/js/item.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "wagwan.utils.jinja_methods",
# 	"filters": "wagwan.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "wagwan.install.before_install"
# after_install = "wagwan.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "wagwan.uninstall.before_uninstall"
# after_uninstall = "wagwan.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "wagwan.utils.before_app_install"
# after_app_install = "wagwan.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "wagwan.utils.before_app_uninstall"
# after_app_uninstall = "wagwan.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "wagwan.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
#     "Item": {"validate": "wagwan.api.validate"}
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
# 	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"wagwan.tasks.all"
# 	],
# 	"daily": [
# 		"wagwan.tasks.daily"
# 	],
# 	"hourly": [
# 		"wagwan.tasks.hourly"
# 	],
# 	"weekly": [
# 		"wagwan.tasks.weekly"
# 	],
# 	"monthly": [
# 		"wagwan.tasks.monthly"
# 	],
# "*/30 * * * *":[]
# }

# Testing
# -------

# before_tests = "wagwan.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "wagwan.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "wagwan.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["wagwan.utils.before_request"]
# after_request = ["wagwan.utils.after_request"]

# Job Events
# ----------
# before_job = ["wagwan.utils.before_job"]
# after_job = ["wagwan.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"wagwan.auth.validate"
# ]
# fixtures = [
#     {"dt": "DocType Link", "filters": [["name", "in", ["b558013226"]]]},
#     {"dt": "Custom Field", "filters": [["name", "in", []]]},
# ]

fixtures = [
    {
        "dt": "Custom Field",
        "filters": [["name", "in", ["Item-custom_category", "Customer-custom_test"]]],
    }
]
