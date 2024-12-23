frappe.ui.form.on("Item", {
    refresh:function(frm){
        
        frm.add_custom_button(__('Show Msg'),function(){


            let d = new frappe.ui.Dialog({
                title: 'Enter details',
                fields: [
                    {
                        label: 'Customer Name',
                        fieldname: 'name',
                        fieldtype: 'Data'
                    },
                    // {
                    //     label: 'Last Name',
                    //     fieldname: 'last_name',
                    //     fieldtype: 'Data'
                    // },
                    // {
                    //     label: 'Age',
                    //     fieldname: 'age',
                    //     fieldtype: 'Int'
                    // }
                ],
                size: 'small', // small, large, extra-large 
                primary_action_label: 'Fetch',
                primary_action(values) {
                    
                    frappe.call({
                        method: 'wagwan.api.get_customers',
                        args: {
                            item_code: frm.doc.name
                        },
                        freeze: true,
                        freeze_message: "Sending Request....",
        
                        callback: function(r) {
                            console.log(r)
                            if (r.message){
                                frappe.msgprint(`<h3>${r.message[0].name}: ${r.message[0].customer_type}</h3>`)
                            }
                        }
                    });
                    d.hide();
                }
            });
            
            d.show();
            



                   
    })
    },
    // custom_author:function(frm){
    //     console.log('hello')
    
    // }
})

// frappe.ui.form.on('Sector', {
// 	refresh: function(frm) {
// 		console.log('hello')
// 		frm.add_custom_button(__('Show Msg'), function() {
// 			frappe.msgprint("Hello World");
// 		});
// 	}
// });
