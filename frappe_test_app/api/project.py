import frappe
import json
from frappe import _

@frappe.whitelist(allow_guest=True)
def create_project():
    data = frappe.local.form_dict
    project_data = frappe.new_doc("Project")
    project_data.update(data)
    project_data.insert()
    return project_data.as_dict()

@frappe.whitelist(allow_guest=True)
def get_projects():
    cache_key = 'get_projects_cache_key'
    cached_data = get_cache(cache_key)

    if cached_data:
        frappe.logger().info("Cache hit for get_projects")
        return cached_data 
    projects = frappe.get_all("Project", fields=["name", "project_name", "start_date", "end_date", "status", "client", "assigned_to", "budget", "description"])

    set_cache(cache_key, json.dumps(projects), ttl=3600)
    return projects

@frappe.whitelist(allow_guest=True)
def get_project_by_id():
    project_id = frappe.local.form_dict.get('project_id')
    project = frappe.get_doc("Project", project_id)
    return project.as_dict()

@frappe.whitelist(allow_guest=True)
def update_project():
    data = frappe.local.form_dict
    project_id = data.get('project_id')
    project = frappe.get_doc("Project", project_id)
    project.update(data)
    project.save()
    return project.as_dict()

@frappe.whitelist(allow_guest=True)
def delete_project():
    project_id = frappe.local.form_dict.get('project_id')
    project = frappe.get_doc("Project", project_id)
    project.delete()
    return {"status": "Deleted", "project_id": project_id}


def get_cache(key):
  
    return frappe.cache().get(key)

def set_cache(key, data, ttl=3600):
    # Save data to cache with specified TTL
    frappe.cache().set(key, data, ttl)
