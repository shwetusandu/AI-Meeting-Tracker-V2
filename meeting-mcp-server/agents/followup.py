from datetime import datetime

def run_followup_agent(actions):

    reminders = []

    for item in actions:

        status = item.get("status", "Open")

        if status == "Open":

            reminders.append({
                "owner": item["owner"],
                "task": item["task"],
                "message": f"Reminder for {item['owner']}: Please update status for '{item['task']}'"
            })

    return reminders