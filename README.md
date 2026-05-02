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

Input:
- Meeting transcript
- Uploaded text file
- Automation webhook payload

Output:
- Action items
- Owners
- Deadlines
- Priority levels
- Jira ticket types
- Risks
- Escalations
- Follow-ups
- Manager summary
- Email summary draft
- Analytics signals

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

## Tech Stack

- Python
- FastAPI
- React
- Make.com
- Groq LLM API
- Google Sheets API
- ngrok
- JSON APIs

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

## Architecture

Frontend:
- React dashboard
- Transcript upload UI
- KPI metrics
- Charts and meeting visibility

Backend:
- FastAPI REST API
- Multi-agent orchestration engine
- JSON response layer
- Validation and normalization logic

Automation Layer:
- Make.com scenarios
- HTTP webhook triggers
- Downstream routing
- Task creation
- Notifications
- Logging

Tunnel / External Access:
- ngrok public endpoint for local development

Data Layer:
- Google Sheets logging tables
- Dashboard metrics source

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
## AI Agent System

This project uses a multi-agent design where each agent has one clear responsibility.

### 1. Summary Agent
Creates concise meeting summaries for leaders and stakeholders.

### 2. Actions Agent
Extracts tasks with:
- owner
- task description
- deadline
- priority
- Jira type

### 3. Risk Agent
Detects blockers, delays, dependencies, and delivery threats.

### 4. Decision Agent
Captures approved decisions made during meetings.

### 5. Priority Agent
Flags urgent work and delivery-critical actions.

### 6. Jira Classifier Agent
Maps work into:
- Bug
- Story
- Task
- Epic

### 7. Manager Summary Agent
Creates executive-level short updates.

### 8. Memory Agent
Captures recurring themes and historical context signals.

### 9. Follow-up Agent
Builds next-step reminders and pending actions.

### 10. Email Agent
Drafts post-meeting summary emails.

### 11. Escalation Agent
Detects high-priority unresolved work needing attention.

### 12. Analytics Agent
Produces operational metrics from meetings.

### 13. Owner Resolver Agent
Maps ambiguous actions to likely owners.

---

## MCP Server Usage

This project was structured as a meeting MCP server workflow.

MCP concepts used:
- Tool-style modular agents
- Server-side orchestration
- Structured request / response processing
- Reusable capability modules
- External automation connectivity

The backend acts as a meeting intelligence server that can be extended with more tools and agents.

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

## Images

# Make.com Workflow

![AI-Meeting-Tracker-V2](docs/Images/Make-Workflow.png)

# FrontEnd

![AI-Meeting-Tracker-V2](docs/Images/Executive-Dashboard.png)
![AI-Meeting-Tracker-V2](docs/Images/Meeting-Dashboard.png)
![AI-Meeting-Tracker-V2](docs/Images/Risk-Dashboard.png)
![AI-Meeting-Tracker-V2](docs/Images/Analytics-Dashboard.png)
![AI-Meeting-Tracker-V2](docs/Images/Tasks-Dashboard.png)
![AI-Meeting-Tracker-V2](docs/Images/Setting-Dashboard.png)

# Generated from Make.com

![AI-Meeting-Tracker-V2](docs/Images/Sample-Gmail.png)
![AI-Meeting-Tracker-V2](docs/Images/Sample-Jira-Ticket.png)
![AI-Meeting-Tracker-V2](docs/Images/Sample-Slack-Message.png)
![AI-Meeting-Tracker-V2](docs/Images/Sample-Slack-Remainder-Message.png)

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

This project demonstrates:

- practical AI engineering and production thinking
- Applied AI systems design
- Workflow automation
- Backend engineering
- Multi-agent orchestration
- Real debugging skills
- Production thinking
- Business process transformation

---
