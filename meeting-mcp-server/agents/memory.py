def run_memory_agent(actions):

    memory = {}

    for item in actions:
        owner = item["owner"]
        task = item["task"]

        memory[owner] = task

    return memory