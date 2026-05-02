# AI Meeting Tracker V2

## Overview

AI Meeting Tracker V2 is a production-grade meeting intelligence platform that transforms raw meeting transcripts into structured execution outputs.

It combines AI agents, FastAPI APIs, React dashboard UI, Google Sheets logging, Make.com workflow automation, and frontend analytics.

The platform converts meetings into:

- Action items
- Owners
- Deadlines
- Priorities
- Jira ticket types
- Risks
- Decisions
- Escalations
- Follow-ups
- Executive summaries
- Analytics

---

## Business Problem Solved

Most teams attend meetings but lose accountability afterward.

This platform converts conversations into measurable execution systems.

---

## Required Tools To Install

## Backend

```bash
pip install fastapi uvicorn requests pandas gspread google-auth python-multipart python-dotenv groq
```

## Frontend

```bash
npm install
npm install axios recharts
```

## Public Tunnel

```bash
npm install -g ngrok
```

or install ngrok manually.

---

## Folder Structure With Placement Guide

```text
AI Meeting Tracker V2/
│
├── backend/
│   ├── main.py
│   ├── config.py
│   ├── requirements.txt
│   ├── .env
│   ├── service_account.json
│   │
│   └── agents/
│       ├── summary.py
│       ├── actions.py
│       ├── risks.py
│       ├── decisions.py
│       ├── priority.py
│       ├── jira_classifier.py
│       ├── manager_summary.py
│       ├── memory.py
│       ├── followup.py
│       ├── email_agent.py
│       ├── escalation.py
│       ├── analytics.py
│       └── owner_resolver.py
│
├── frontend/
│   ├── package.json
│   ├── vite.config.js
│   ├── node_modules/
│   └── src/
│       ├── App.jsx
│       ├── App.css
│       └── api.js
│
├── docs/
│   ├── prompts.md
│   ├── architecture.png
│   └── screenshots/
│
├── .gitignore
└── README.md
```

---

## Where Files Should Be Placed

## backend/

Place:

- main.py
- config.py
- requirements.txt
- .env
- service_account.json

## backend/agents/

Place all AI agent files.

## frontend/src/

Place:

- App.jsx
- App.css
- api.js

## docs/

Place:

- prompts
- screenshots
- architecture diagrams
- workflow exports

---

## Architecture Flowchart

```text
Transcript Input
      ↓
React Upload / Make.com Trigger
      ↓
FastAPI Backend
      ↓
Multi-Agent AI Processing
      ├─ Summary Agent
      ├─ Actions Agent
      ├─ Risk Agent
      ├─ Decision Agent
      ├─ Priority Agent
      ├─ Jira Classifier
      ├─ Escalation Agent
      └─ Analytics Agent
      ↓
Structured JSON Output
      ↓
Make.com Downstream Flows
      ├─ Alerts
      ├─ Sheets Logging
      ├─ Jira Tasks
      └─ Dashboard Updates
```

---

## AI Agent Responsibilities

- Summary Agent
- Actions Agent
- Risk Agent
- Decision Agent
- Priority Agent
- Manager Summary Agent
- Memory Agent
- Follow-up Agent
- Email Agent
- Escalation Agent
- Analytics Agent
- Owner Resolver Agent

---

## Main API Endpoints

### GET /

Health check

### GET /dashboard/summary

Dashboard metrics

### POST /upload-transcript

Upload transcript from frontend

### POST /process-meeting

Main AI processing endpoint

### GET /test-sheet

Google Sheets connectivity test

---

## Example Output

```json
{
  "status":"success",
  "summary":"Release remains on track.",
  "tasks":[
    {
      "owner":"Mary",
      "task":"Complete export UI",
      "jira_type":"Story",
      "priority":"High"
    }
  ],
  "risks":[
    {
      "risk":"UI delay may impact release"
    }
  ]
}
```

---

## How To Use

## Backend

```bash
cd backend
pip install -r requirements.txt
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

## Public Tunnel

```bash
ngrok http 8000
```

## Frontend

```bash
cd frontend
npm install
npm run dev
```

## Make.com URL

```text
https://your-ngrok-url.ngrok-free.app/process-meeting
```

---

## API Keys And Credentials

## 1. Groq API Key

File:

```text
backend/.env
```

Example:

```text
GROQ_API_KEY=your_key_here
MODEL_NAME=llama-3.3-70b-versatile
```

## 2. Google Sheets Credentials

File:

```text
backend/service_account.json
```

## 3. Spreadsheet ID

Inside:

```text
backend/main.py
```

Change:

```python
SPREADSHEET_ID = "your_sheet_id"
```

## 4. Make.com Webhook

Inside:

```text
backend/main.py
```

Change:

```python
webhook_url = "https://hook.eu1.make.com/your_webhook_id"
```

## 5. Frontend API URL

Inside:

```text
frontend/src/api.js
frontend/src/App.jsx
```

Use:

```text
http://localhost:8000
```

or

```text
https://your-ngrok-url.ngrok-free.app
```

---

## Real Challenges Solved

- 404 route failures
- 500 backend errors
- JSON parsing failures
- Inconsistent LLM outputs
- Make.com iterator issues
- ngrok tunnel expiry
- Schema mismatches
- Agent orchestration bugs

---

## Conclusion

AI Meeting Tracker V2 is a real-world AI operations platform.

It transforms meetings into execution systems using AI agents, automation, APIs, and business workflows.

This demonstrates practical AI engineering and production thinking.

---
