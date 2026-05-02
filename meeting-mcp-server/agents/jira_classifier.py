import os
from groq import Groq
from dotenv import load_dotenv
from config import MODEL_NAME

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def run_jira_agent(task):

    prompt = f"""
Classify into:
Bug / Story / Task / Epic

Task:
{task}

Return one word only.
"""

    res = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[{"role":"user","content":prompt}]
    )

    return res.choices[0].message.content