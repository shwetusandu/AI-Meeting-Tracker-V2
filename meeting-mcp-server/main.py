# REBUILD COPY OF YOUR main.py
# Preserves original integrations
# Fixes route conflicts
# Fixes Make.com processing response
# Keeps dashboard + upload + sheets + agents imports

import traceback
import uuid
import requests
import gspread
import pandas as pd
import re

from datetime import datetime
from fastapi import FastAPI, Request, UploadFile, File
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from google.oauth2.service_account import Credentials

# ORIGINAL AGENT IMPORTS PRESERVED
from agents import actions
from agents.summary import run_summary_agent
from agents.actions import run_actions_agent
from agents.risks import run_risk_agent
from agents.decisions import run_decision_agent
from agents.priority import run_priority_agent
from agents.manager_summary import run_manager_summary
from agents.memory import run_memory_agent
from agents.followup import run_followup_agent
from agents.email_agent import run_email_agent
from agents.escalation import run_escalation_agent
from agents.analytics import run_analytics_agent
from agents.owner_resolver import run_owner_resolver

app = FastAPI(title="AI Meeting OS - Real Time Meeting Processor")

# ---------------------------------------------------
# CORS
# ---------------------------------------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ---------------------------------------------------
# INPUT MODEL
# ---------------------------------------------------
class MeetingInput(BaseModel):
    meeting_id: str
    title: str
    date: str
    transcript: str
    source: str

# ---------------------------------------------------
# GOOGLE SHEETS
# ---------------------------------------------------
SERVICE_FILE = "service_account.json"
SPREADSHEET_ID = "1tDu0AHVuBMyHL_Dxm--Tx5qAywiqnzuojzbizDP4yxE"

SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive"
]

creds = Credentials.from_service_account_file(
    SERVICE_FILE,
    scopes=SCOPES
)

gc = gspread.authorize(creds)

def get_sheet_df(tab_name):
    ws = gc.open_by_key(SPREADSHEET_ID).worksheet(tab_name)
    rows = ws.get_all_records()
    return pd.DataFrame(rows)

# ---------------------------------------------------
# HOME
# ---------------------------------------------------
@app.get("/")
def home():
    return {
        "status": "ok",
        "engine": "Groq"
    }

# ---------------------------------------------------
# DASHBOARD SUMMARY
# ---------------------------------------------------
@app.get("/dashboard/summary")
def dashboard_summary():
    try:
        meeting_df = get_sheet_df("meeting_log")
        action_df = get_sheet_df("actions_log")

        meetings = (
            meeting_df["meeting_id"].nunique()
            if "meeting_id" in meeting_df.columns else 0
        )

        tasks = len(action_df)

        risks = 0
        if "priority" in action_df.columns:
            risks = len(
                action_df[
                    action_df["priority"]
                    .astype(str)
                    .str.lower()
                    .isin(["high", "critical"])
                ]
            )

        overdue = 0
        if "due_date" in action_df.columns:
            overdue = len(
                action_df[
                    action_df["due_date"]
                    .astype(str)
                    .str.lower()
                    .isin(["overdue", "missed", "yesterday"])
                ]
            )

        ownerStats = []
        if "owner" in action_df.columns:
            counts = action_df["owner"].fillna("Unassigned").value_counts()

            ownerStats = [
                {"name": k, "value": int(v)}
                for k, v in counts.items()
            ]

        jiraTypes = []
        if "jira_type" in action_df.columns:
            counts = action_df["jira_type"].fillna("Task").value_counts()

            jiraTypes = [
                {"name": k, "value": int(v)}
                for k, v in counts.items()
            ]

        return {
            "meetings": int(meetings),
            "tasks": int(tasks),
            "risks": int(risks),
            "overdue": int(overdue),
            "ownerStats": ownerStats,
            "jiraTypes": jiraTypes,
            "weeklyTrend": [],
            "recentMeetings": []
        }

    except Exception as e:
        return {"error": str(e)}

# ---------------------------------------------------
# HEALTH ROUTES
# ---------------------------------------------------
@app.get("/process-meeting")
@app.get("/meeting/process")
def process_health():
    return {
        "status": "alive",
        "message": "Use POST"
    }

# ---------------------------------------------------
# MAIN PROCESS ROUTES
# Supports OLD + NEW URL
# ---------------------------------------------------
@app.post("/process-meeting")
@app.post("/meeting/process")
async def process_meeting(request: Request):

    try:
        data = await request.json()

        meeting_id = data.get("meeting_id", "")
        title = data.get("title", "")
        date = data.get("date", "")
        source = data.get("source", "")
        transcript = data.get("transcript", "")

        summary = run_summary_agent(transcript)
        actions = run_actions_agent(transcript)
        risks = run_risk_agent(transcript)
        decisions = run_decision_agent(transcript)
        priorities = run_priority_agent(actions)
        escalations = run_escalation_agent(actions)
        manager_summary = run_manager_summary(transcript)
        memory = run_memory_agent(actions)
        email_draft = run_email_agent(actions)
        analytics = run_analytics_agent(actions)
        followups = run_followup_agent(actions)
        owners = run_owner_resolver(actions)

        return JSONResponse(
            status_code=200,
            content={
                "status": "success",
                "meeting_id": meeting_id,
                "title": title,
                "date": date,
                "source": source,
                "summary": summary,
                "total_actions": len(actions),
                "actions": actions,
                "risks": risks,
                "decisions": decisions,
                "priorities": priorities,
                "escalations": escalations,
                "manager_summary": manager_summary,
                "memory": memory,
                "email_draft": email_draft,
                "analytics": analytics,        
                "followups": followups,
                "owners": owners,
                "processed_at": datetime.utcnow().isoformat()
            }
        )

    except Exception as e:
        print(traceback.format_exc())

        return JSONResponse(
            status_code=500,
            content={
                "status": "error",
                "message": str(e)
            }
        )

# ---------------------------------------------------
# SUMMARY
# ---------------------------------------------------
# def generate_summary(text):
#     lines = text.split("\n")
#     clean = [x.strip() for x in lines if x.strip()]
#     return " ".join(clean[:4])

# ---------------------------------------------------
# TASK EXTRACTION
# ---------------------------------------------------
def extract_tasks(text):

    tasks = []

    keywords = [
        "need to",
        "will",
        "handle",
        "finish",
        "complete",
        "send",
        "review",
        "create"
    ]

    for line in text.split("\n"):

        if ":" in line:

            speaker, statement = line.split(":", 1)

            speaker = speaker.strip()
            statement = statement.strip()

            if any(k in statement.lower() for k in keywords):

                tasks.append({
                    "assignee": speaker,
                    "task": statement,
                    "due_date": extract_due_date(statement),
                    "priority": "Medium",
                    "status": "Open"
                })

    return tasks

# ---------------------------------------------------
# DUE DATE
# ---------------------------------------------------
def extract_due_date(text):

    text = text.lower()

    if "today" in text:
        return "Today"
    if "tomorrow" in text:
        return "Tomorrow"
    if "friday" in text:
        return "Friday"
    if "this week" in text:
        return "This Week"
    if "next week" in text:
        return "Next Week"

    return "Not Mentioned"

# ---------------------------------------------------
# RISKS
# ---------------------------------------------------
def extract_risks(text):

    risks = []

    keys = [
        "risk",
        "issue",
        "delay",
        "blocked",
        "problem",
        "pending"
    ]

    for line in text.split("\n"):

        if any(k in line.lower() for k in keys):

            risks.append({
                "owner": "Team",
                "risk": line.strip(),
                "severity": "Medium"
            })

    return risks

# ---------------------------------------------------
# FILE UPLOAD
# ---------------------------------------------------
@app.post("/upload-transcript")
async def upload_transcript(file: UploadFile = File(...)):

    try:
        content = await file.read()

        transcript = content.decode(
            "utf-8",
            errors="ignore"
        )

        webhook_url = "https://hook.eu1.make.com/v4ea965omhqlww6ijxxahlhbsxoa7qxj"

        payload = {
            "meeting_id": "MTG-" + str(uuid.uuid4())[:8],
            "title": file.filename or "Untitled Meeting",
            "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "transcript": transcript,
            "source": "React Upload",
            "status": "pending_parse"
        }

        response = requests.post(
            webhook_url,
            json=payload,
            timeout=20
        )

        return {
            "status": "success",
            "file": file.filename,
            "make_status": response.status_code
        }

    except Exception as e:

        return {
            "status": "error",
            "message": str(e)
        }

# ---------------------------------------------------
# TEST SHEET
# ---------------------------------------------------
@app.get("/test-sheet")
def test_sheet():

    try:
        sh = gc.open_by_key(SPREADSHEET_ID)

        tabs = [ws.title for ws in sh.worksheets()]

        return {
            "status": "success",
            "tabs": tabs
        }

    except Exception as e:
        return {"error": str(e)}