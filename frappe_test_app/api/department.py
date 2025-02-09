import frappe
from frappe import _

@frappe.whitelist(allow_guest=True)
def create_department():
    data = frappe.local.form_dict
    department_data = frappe.new_doc("Department")
    department_data.update(data)
    department_data.insert()
    return department_data.as_dict()

@frappe.whitelist(allow_guest=True)
def get_departments():
    departments = frappe.get_all("Department", fields=["name", "department_name", "manager", "employees"])
    return departments

@frappe.whitelist(allow_guest=True)
def get_department_by_id():
    department_id = frappe.local.form_dict.get('department_id')
    department = frappe.get_doc("Department", department_id)
    return department.as_dict()

@frappe.whitelist(allow_guest=True)
def update_department():
    data = frappe.local.form_dict
    department_id = data.get('department_id')
    department = frappe.get_doc("Department", department_id)
    department.update(data)
    department.save()
    return department.as_dict()

@frappe.whitelist(allow_guest=True)
def delete_department():
    department_id = frappe.local.form_dict.get('department_id')
    department = frappe.get_doc("Department", department_id)
    department.delete()
    return {"status": "Deleted", "department_id": department_id}
