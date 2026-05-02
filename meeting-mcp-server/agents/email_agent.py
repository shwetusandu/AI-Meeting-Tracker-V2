import os
from groq import Groq
from dotenv import load_dotenv
from config import MODEL_NAME

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def run_email_agent(actions):

    # Extract the first action's owner and task for the email
    if not actions:
        return "No actions to email."

    action = actions[0]
    owner = action.get("owner", "Unassigned")
    task = action.get("task", "No task specified")

    prompt = f"""
Write a professional follow-up email.

Owner: {owner}
Task: {task}
"""

    res = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[{"role":"user","content":prompt}]
    )

    return res.choices[0].message.content