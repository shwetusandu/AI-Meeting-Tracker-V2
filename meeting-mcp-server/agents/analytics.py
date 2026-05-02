def run_analytics_agent(actions):

    # Extract the first action's risks and task for the email
    if not actions:
        return 

    action = actions[0]
    risks = action.get("risks", "Unassigned")
    tasks = action.get("tasks", "No task specified")
    priority = action.get("priority", "No priority specified")

    return {
        "total_actions": len(tasks),
        "total_risks": len(risks),
        "high_priority_tasks": len(priority)
    }