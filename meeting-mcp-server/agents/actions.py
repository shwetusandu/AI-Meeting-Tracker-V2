import os, json
from groq import Groq
from dotenv import load_dotenv
from config import MODEL_NAME

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def run_actions_agent(transcript):
    prompt = f"""
You are an expert Agile delivery manager.
From the meeting transcript, extract all action items.
for each action item return:
owner
task
deadline
jira_type
priority

jira_type rules:
Bug = Fix issue, defect, error, broken, patch, bug
Story = New feature, enhancement, UI build, module creation
Task = General work, follow-up, testing, documentation, support
Epic = Large milestone involving multiple tasks

priority rules:
High = urgent, blocker, today, critical, risk to delivery
Medium = normal committed work
Low = optional or future work

Return ONLY valid JSON array.

[
  {{
    "owner":"John",
    "task":"Complete API",
    "deadline":"Friday",
    "jira_type":"Task",
    "priority":"Medium"
  }}
]

Transcript:
{transcript}
"""

    res = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[{"role":"user","content":prompt}]
    )

    return json.loads(res.choices[0].message.content)