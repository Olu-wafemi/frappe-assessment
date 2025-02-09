# api.py
import frappe
from frappe import _

@frappe.whitelist(allow_guest=True)
def create_task():
    try:
       
        task_data = frappe.local.form_dict

  
        task = frappe.get_doc({
            'doctype': 'Task',
            'title': task_data.get('title'),
            'description': task_data.get('description'),
            'assigned_to': task_data.get('assigned_to')
        })
        task.insert()

        return {"message": "Task created successfully", "task_id": task.name}
    except Exception as e:
        frappe.log_error(f"Error creating task: {e}", "Create Task Error")
        return {"message": "Error creating task", "error": str(e)}

@frappe.whitelist(allow_guest=True)
def update_task():
    try:
      
        task_data = frappe.local.form_dict
        task_id = task_data.get('task_id')

        task = frappe.get_doc('Task', task_id)
        task.update({
            'title': task_data.get('title', task.title),
            'description': task_data.get('description', task.description),
            'assigned_to': task_data.get('assigned_to', task.assigned_to)
        })
        task.save()

        return {"message": "Task updated successfully"}
    except Exception as e:
        frappe.log_error(f"Error updating task: {e}", "Update Task Error")
        return {"message": "Error updating task", "error": str(e)}

@frappe.whitelist(allow_guest=True)
def get_task():
    try:
         
        task_data = frappe.local.form_dict
        task_id = task_data.get('task_id')

        task = frappe.get_doc('Task', task_id)
        task_details = {
            'title': task.title,
            'description': task.description,
            'assigned_to': task.assigned_to,
            'status': task.status
        }
        return task_details
    except Exception as e:
        frappe.log_error(f"Error fetching task: {e}", "Get Task Error")
        return {"message": "Error fetching task", "error": str(e)}

@frappe.whitelist(allow_guest=True)
def delete_task():
    try:
        
        task_data = frappe.local.form_dict
        task_id = task_data.get('task_id')

        task = frappe.get_doc('Task', task_id)
        task.delete()

        return {"message": "Task deleted successfully"}
    except Exception as e:
        frappe.log_error(f"Error deleting task: {e}", "Delete Task Error")
        return {"message": "Error deleting task", "error": str(e)}
