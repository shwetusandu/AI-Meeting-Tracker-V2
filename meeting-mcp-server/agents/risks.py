import os, json
from groq import Groq
from dotenv import load_dotenv
from config import MODEL_NAME

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def run_risk_agent(transcript):
    prompt = f"""
Identify project risks.

Return ONLY JSON array.

[
  {{
    "type":"Budget Delay",
    "severity":"High"
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