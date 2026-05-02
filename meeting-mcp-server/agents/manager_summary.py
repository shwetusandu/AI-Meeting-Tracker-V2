import os
from groq import Groq
from dotenv import load_dotenv
from config import MODEL_NAME

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def run_manager_summary(transcript):

    prompt = f"""
Create 2-line executive summary for leadership.

Transcript:
{transcript}
"""

    res = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[{"role":"user","content":prompt}]
    )

    return res.choices[0].message.content