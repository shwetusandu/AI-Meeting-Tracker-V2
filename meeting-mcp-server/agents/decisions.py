import os, json
from groq import Groq
from dotenv import load_dotenv
from config import MODEL_NAME

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def run_decision_agent(transcript):
    prompt = f"""
Extract decisions made in meeting.

Return ONLY JSON array.

[
  {{
    "decision":"Sprint scope approved"
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