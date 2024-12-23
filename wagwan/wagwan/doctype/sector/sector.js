// Copyright (c) 2024, Sofian Saleh and contributors
// For license information, please see license.txt

frappe.ui.form.on('Sector', {
	refresh: function(frm) {
		console.log('hello')
		frm.add_custom_button(__('Show Msg'), function() {
			frappe.msgprint("Hello World");
		});
	}
});
