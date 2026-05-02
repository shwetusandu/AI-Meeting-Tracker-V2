# AI Meeting Tracker V2

## Overview

AI Meeting Tracker V2 is a production-style meeting intelligence platform that converts raw meeting transcripts into structured operational outputs.

The system ingests transcripts from a React frontend or automation trigger, processes them through specialized AI agents, and sends clean outputs into Make.com for downstream execution.

## Folder Structure

```text
AI Meeting Tracker V2/
├── backend/
│   ├── main.py
│   ├── requirements.txt
│   ├── service_account.json
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
├── frontend/
│   ├── src/
│   ├── App.jsx
│   └── App.css
├── docs/
│   ├── prompts.md
│   └── architecture.png
└── README.md
```

## Flowchart

```text
Transcript Input
      ↓
React Upload / Make.com Webhook
      ↓
FastAPI Backend
      ↓
Multi AI Agent Processing
      ├─ Summary Agent
      ├─ Actions Agent
      ├─ Risk Agent
      ├─ Decision Agent
      ├─ Jira Classifier
      ├─ Escalation Agent
      └─ Analytics Agent
      ↓
Structured JSON Output
      ↓
Make.com Downstream Flows
      ├─ Sheets Logging
      ├─ Alerts
      ├─ Jira Tasks
      └─ Dashboard Updates
```

## Core Business Use Case

Teams lose actions, decisions, deadlines, and blockers after meetings.

This platform converts every meeting into trackable execution data.

## How to Use

### 1. Install Backend

```bash
pip install -r requirements.txt
```

### 2. Start API

```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

### 3. Start Public Tunnel

```bash
ngrok http 8000
```

### 4. Run Frontend

```bash
npm install
npm run dev
```

### 5. Use the System

- Upload transcript file from frontend
- Or send transcript via Make.com webhook
- AI agents process transcript
- View dashboard metrics
- Trigger downstream automations

## AI Agent System

- Summary Agent
- Actions Agent
- Risk Agent
- Decision Agent
- Priority Agent
- Jira Classifier Agent
- Manager Summary Agent
- Memory Agent
- Follow-up Agent
- Email Agent
- Escalation Agent
- Analytics Agent
- Owner Resolver Agent

## Tech Stack

- Python
- FastAPI
- React
- Make.com
- Groq LLM API
- Google Sheets API
- ngrok

## Real Engineering Challenges Solved

- 404 / 500 route failures
- JSON schema mismatches
- AI output normalization
- Make.com bundle mapping
- ngrok tunnel issues
- Multi-agent orchestration bugs

## Conclusion

AI Meeting Tracker V2 demonstrates how AI can transform meetings into execution systems.

Instead of storing transcripts, it converts conversations into tasks, ownership, priorities, risks, Jira-ready work items, and automated business workflows.

This project reflects practical AI engineering, automation architecture, and real-world delivery thinking.

## Author

Shwetha K M
