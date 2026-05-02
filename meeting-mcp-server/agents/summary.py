import os
from groq import Groq
from dotenv import load_dotenv
from config import MODEL_NAME

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def run_summary_agent(transcript):
    prompt = f"""
Summarize this meeting in one professional sentence.

Transcript:
{transcript}
"""

    res = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[{"role":"user","content":prompt}]
    )

    return res.choices[0].message.content