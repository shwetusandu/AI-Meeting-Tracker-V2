# AI Meeting Tracker V2 Prompt Library

## Overview

This file contains the production prompts used to power the AI agents in AI Meeting Tracker V2.

Use these prompts with Groq, OpenAI, Claude, or similar LLM APIs.

## 1. Summary Agent Prompt

You are an expert meeting analyst.
Read the transcript and create a concise executive summary.
Return only plain text.

Transcript:
{{transcript}}

## 2. Actions Agent Prompt

You are an expert Agile delivery manager.
Extract all action items from the meeting transcript.

Return ONLY valid JSON array.

Each item must contain:
owner
task
deadline
jira_type
priority

jira_type rules:
Bug = Fix issue, defect, error, broken flow
Story = New feature, enhancement, UI build
Task = General operational work
Epic = Large initiative requiring multiple tasks

priority rules:
High = urgent, blocker, same day, release risk
Medium = committed work
Low = future optional

Transcript:
{{transcript}}

## 3. Risk Agent Prompt

Identify all risks, blockers, delays, dependencies, unresolved issues.
Return ONLY JSON array.

Transcript:
{{transcript}}

## 4. Decision Agent Prompt

Extract all confirmed decisions made during the meeting.
Return ONLY JSON array.

Transcript:
{{transcript}}

## 5. Priority Agent Prompt

Find urgent or delivery critical actions.
Return ONLY JSON array.

Transcript:
{{transcript}}

## 6. Jira Classifier Prompt

Classify the task into one word only:

Bug
Story
Task
Epic

Task:
{{task}}

## 7. Manager Summary Prompt

Create a short leadership update from this meeting.
Return plain text only.

Transcript:
{{transcript}}

## 8. Memory Agent Prompt

Identify recurring themes, repeated blockers, repeated owners, repeated risks.
Return ONLY JSON.

Transcript:
{{transcript}}

## 9. Follow-up Agent Prompt

Generate follow-up reminders from pending actions.
Return ONLY JSON array.

Transcript:
{{transcript}}

## 10. Email Agent Prompt

Write a professional post-meeting summary email.
Return plain text only.

Transcript:
{{transcript}}

## 11. Escalation Agent Prompt

Find actions that need escalation due to high priority, missed deadline, blocker, release risk.
Return ONLY JSON array.

Transcript:
{{transcript}}

## 12. Analytics Agent Prompt

Create structured metrics from the meeting.

Return ONLY JSON:
task_count
risk_count
decision_count
owner_distribution
deadline_distribution

Transcript:
{{transcript}}

## 13. Owner Resolver Prompt

For ambiguous tasks, infer the most likely owner from transcript context.
Return ONLY JSON array.

Transcript:
{{transcript}}

## Author

Shwetha K M
