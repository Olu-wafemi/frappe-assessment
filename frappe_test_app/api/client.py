import frappe
from frappe import _

@frappe.whitelist(allow_guest=True)
def create_client():
    data = frappe.local.form_dict
    client_data = frappe.new_doc("Client")
    client_data.update(data)
    client_data.insert()
    return client_data.as_dict()

@frappe.whitelist(allow_guest=True)
def get_clients():
    clients = frappe.get_all("Client", fields=["name", "client_name", "contact_info", "address", "projects"])
    return clients

@frappe.whitelist(allow_guest=True)
def get_client_by_id():
    client_id = frappe.local.form_dict.get('client_id')
    client = frappe.get_doc("Client", client_id)
    return client.as_dict()

@frappe.whitelist(allow_guest=True)
def update_client():
    data = frappe.local.form_dict
    client_id = data.get('client_id')
    client = frappe.get_doc("Client", client_id)
    client.update(data)
    client.save()
    return client.as_dict()

@frappe.whitelist(allow_guest=True)
def delete_client():
    client_id = frappe.local.form_dict.get('client_id')
    client = frappe.get_doc("Client", client_id)
    client.delete()
    return {"status": "Deleted", "client_id": client_id}
