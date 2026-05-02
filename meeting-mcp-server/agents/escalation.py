def run_escalation_agent(actions):

    escalations = []

    for item in actions:
        if item.get("priority") == "High":
            escalations.append({
                "owner": item["owner"],
                "task": item["task"],
                "reason": "High priority pending"
            })

    return escalations