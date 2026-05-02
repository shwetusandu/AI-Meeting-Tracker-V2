def run_owner_resolver(actions):

    owner_memory = {
        "api": "John",
        "dashboard": "Mary",
        "bug": "Bhaskar",
        "jira": "Rupam",
        "report": "Anita"
    }

    for item in actions:

        if item["owner"].lower() in ["unknown", "", "unassigned", "team"]:

            task = item["task"].lower()

            assigned = "Manager"

            for keyword, owner in owner_memory.items():
                if keyword in task:
                    assigned = owner
                    break

            item["owner"] = assigned

    return actions