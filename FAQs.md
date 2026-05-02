# AI Meeting Tracker V2 Interview FAQs

## Overview

This document contains important questions and strong answer directions based on the AI Meeting Tracker V2 project.

---

## 1. What problem does AI Meeting Tracker V2 solve?

It converts unstructured meeting transcripts into structured outputs such as tasks, owners, deadlines, risks, decisions, Jira types, escalations, and analytics.

---

## 2. Why did you build this project?

Many teams attend meetings but fail to convert discussions into execution. I built a system that turns meetings into operational workflows automatically.

---

## 3. What technologies were used?

- Python
- FastAPI
- React
- Make.com
- Groq LLM API
- Google Sheets API
- ngrok
- JSON REST APIs

---

## 4. What is the architecture of the solution?

Frontend uploads transcripts.
Backend FastAPI receives requests.
Multiple AI agents process the transcript.
Structured JSON is returned.
Make.com triggers downstream automations.

---

## 5. What are AI agents in this project?

Each agent performs one responsibility:

- Summary Agent
- Actions Agent
- Risk Agent
- Decision Agent
- Jira Classifier
- Escalation Agent
- Analytics Agent

This modular design improves maintainability and scaling.

---

## 6. Why use multiple agents instead of one prompt?

Specialized agents usually perform better than one large generic prompt because each has a narrow objective and clearer outputs.

---

## 7. How did you classify Jira ticket types?

The actions extraction flow inferred whether work should be Bug, Story, Task, or Epic based on transcript context.

---

## 8. What challenges did you face?

- 404 route issues
- 500 backend errors
- JSON parsing failures
- Inconsistent LLM outputs
- Make.com mapping issues
- ngrok tunnel expiration
- Mixed data structures

---

## 9. How did you solve inconsistent AI outputs?

I implemented normalization logic to convert strings, lists, and JSON text into clean structured objects.

---

## 10. Why FastAPI?

FastAPI is fast, async-friendly, clean for REST APIs, and ideal for AI backend services.

---

## 11. Why Make.com?

It accelerates workflow automation without writing extra integration code for every downstream system.

---

## 12. How was Google Sheets used?

As a lightweight data store for logs, KPI metrics, and dashboard reporting.

---

## 13. How does the frontend work?

React frontend allows transcript upload, displays KPIs, charts, and operational summaries.

---

## 14. What happens after transcript upload?

Transcript is sent to backend.
AI agents process it.
JSON response is returned.
Make.com scenarios trigger tasks, alerts, and logs.

---

## 15. How did you debug production issues?

Used logs, traceback analysis, route validation, payload inspection, and schema checks.

---

## 16. What makes this project different from tutorials?

This involved real debugging, live integrations, payload failures, schema fixes, and production thinking.

---

## 17. How would you scale this project?

- PostgreSQL instead of Sheets
- Queue workers
- Redis caching
- Authentication
- Cloud deployment
- Monitoring
- Vector memory across meetings

---

## 18. How would you improve AI quality?

- Better prompts
- Output validators
- Retry logic
- Function calling
- Historical context memory
- Human review loops

---

## 19. What business impact can this create?

- Better accountability
- Faster follow-up
- Lower meeting waste
- Improved visibility
- Faster delivery execution

---

## 20. What was your personal contribution?

Designed architecture, built backend APIs, integrated automation flows, debugged failures, and implemented multi-agent orchestration.

---

## 21. If given more time, what would you add?

- Slack integration
- Jira auto-creation
- Voice transcript ingestion
- Sentiment analysis
- Delivery forecasting
- Cross-meeting memory

---

## 22. What did you learn from this project?

How to move from AI prototype to operational system through debugging, integrations, schema discipline, and modular design.

---

## 23. Can this be used in enterprises?

Yes. It can support PMO teams, delivery teams, agile teams, leadership reviews, and client operations.

---

## 24. Why is this relevant for AI Solution Architect roles?

Because it combines AI, APIs, workflows, data handling, business outcomes, and systems thinking.

---

## 25. What is your proudest part of the project?

Turning a failing prototype into a fully working end-to-end AI automation platform.

---

## Author

Shwetha K M
