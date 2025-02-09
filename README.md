# My Frappe Bench Setup (macOS)

This README documents my Frappe bench setup on macOS.

## Setup Steps

1. I first ensured I had Python 3 installed. I used `brew install python@3.9`
   I then installed `pip` if it wasn't already available, and updated it with `python3 -m pip install --upgrade pip`. I created and activated a virtual environment: `python3 -m venv frappe-env` and `source frappe-env/bin/activate`.

2. I installed Frappe Bench: `pip install frappe-bench`.

3. I initialized my bench: `bench init frappe-test-bench` and then `cd frappe-test-bench`.

4. I created an application using the `bench new-app frappe_test_bench` command and a new app spin app.

5. I created my site: `bench new-site frappe.test`,

6. I installed my app to the website

7. I started the bench: `bench start`.

#
