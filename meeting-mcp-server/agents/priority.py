import os
from groq import Groq
from dotenv import load_dotenv
from config import MODEL_NAME

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def run_priority_agent(actions):

    # Extract the first action's task for priority assignment
    if not actions:
        return "No actions to prioritize."

    action = actions[0]
    task = action.get("task", "No task specified")

    prompt = f"""
Assign priority: High / Medium / Low

Task:
{task}

Return only one word.
"""

    res = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[{"role":"user","content":prompt}]
    )

    return res.choices[0].message.content