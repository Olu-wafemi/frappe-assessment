import frappe
from frappe import _

@frappe.whitelist(allow_guest=True)
def create_employee():
    data = frappe.local.form_dict
    employee_data = frappe.new_doc("Employee")
    employee_data.update(data)
    employee_data.insert()
    return employee_data.as_dict()

@frappe.whitelist(allow_guest=True)
def get_employees():
    employees = frappe.get_all("Employee", fields=["name", "employee_name", "email", "phone", "department", "role"])
    return employees

@frappe.whitelist(allow_guest=True)
def get_employee_by_id():
    employee_id = frappe.local.form_dict.get('employee_id')
    employee = frappe.get_doc("Employee", employee_id)
    return employee.as_dict()

@frappe.whitelist(allow_guest=True)
def update_employee():
    data = frappe.local.form_dict
    employee_id = data.get('employee_id')
    employee = frappe.get_doc("Employee", employee_id)
    employee.update(data)
    employee.save()
    return employee.as_dict()

@frappe.whitelist(allow_guest=True)
def delete_employee():
    employee_id = frappe.local.form_dict.get('employee_id')
    employee = frappe.get_doc("Employee", employee_id)
    employee.delete()
    return {"status": "Deleted", "employee_id": employee_id}
