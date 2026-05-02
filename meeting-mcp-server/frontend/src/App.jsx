import React, { useEffect, useState } from "react";
import "./App.css";
import {
  ResponsiveContainer,
  BarChart,
  Bar,
  PieChart,
  Pie,
  Cell,
  LineChart,
  Line,
  XAxis,
  YAxis,
  Tooltip,
  CartesianGrid,
} from "recharts";

const COLORS = ["#3b82f6", "#06b6d4", "#10b981", "#f59e0b", "#ef4444"];

export default function App() {
  const [page, setPage] = useState("dashboard");
  const [data, setData] = useState(null);
  const [uploading, setUploading] = useState(false);

  const API = "http://127.0.0.1:8000";

  useEffect(() => {
    loadDashboard();
  }, []);

  async function loadDashboard() {
    try {
      const res = await fetch(`${API}/dashboard/summary`);
      const json = await res.json();
      setData(json);
    } catch (err) {
      console.log(err);
    }
  }

  async function uploadTranscript(e) {
    const file = e.target.files[0];
    if (!file) return;

    try {
      setUploading(true);

      const formData = new FormData();
      formData.append("file", file);

      await fetch(`${API}/upload-transcript`, {
        method: "POST",
        body: formData,
      });

      setTimeout(() => {
        loadDashboard();
        setUploading(false);
      }, 2500);
    } catch (err) {
      console.log(err);
      setUploading(false);
    }
  }

  if (!data) return <div className="loading">Loading AI Dashboard...</div>;

  return (
    <div className="app">
      {/* SIDEBAR */}
      <aside className="sidebar">
        <div className="logo">AI Meeting OS</div>

        <button onClick={() => setPage("dashboard")}>Dashboard</button>
        <button onClick={() => setPage("meetings")}>Meetings</button>
        <button onClick={() => setPage("tasks")}>Tasks</button>
        <button onClick={() => setPage("risks")}>Risks</button>
        <button onClick={() => setPage("analytics")}>Analytics</button>
        <button onClick={() => setPage("settings")}>Settings</button>
      </aside>

      {/* MAIN */}
      <main className="main">
        <div className="topbar">
          <div>
            <h1>{title(page)}</h1>
            <p className="live">🟢 Connected to Live Backend</p>
          </div>

          <label className="uploadBtn">
            {uploading ? "Uploading..." : "+ Upload Transcript"}
            <input type="file" hidden onChange={uploadTranscript} />
          </label>
        </div>

        {/* DASHBOARD */}
        {page === "dashboard" && (
          <>
            <div className="cards">
              <Card title="Meetings" value={data.meetings} />
              <Card title="Tasks" value={data.tasks} />
              <Card title="Risks" value={data.risks} />
              <Card title="Overdue" value={data.overdue} />
            </div>

            <div className="grid2">
              <Panel title="Tasks by Owner">
                <ResponsiveContainer width="100%" height={320}>
                  <BarChart data={data.ownerStats}>
                    <CartesianGrid strokeDasharray="3 3" stroke="#1e293b" />
                    <XAxis dataKey="name" stroke="#94a3b8" />
                    <YAxis stroke="#94a3b8" />
                    <Tooltip />
                    <Bar dataKey="value" fill="#3b82f6" radius={[8,8,0,0]} />
                  </BarChart>
                </ResponsiveContainer>
              </Panel>

              <Panel title="Jira Type Split">
                <ResponsiveContainer width="100%" height={320}>
                  <PieChart>
                    <Pie
                      data={data.jiraTypes}
                      dataKey="value"
                      outerRadius={110}
                      label
                    >
                      {data.jiraTypes.map((_, i) => (
                        <Cell key={i} fill={COLORS[i % COLORS.length]} />
                      ))}
                    </Pie>
                    <Tooltip />
                  </PieChart>
                </ResponsiveContainer>
              </Panel>
            </div>

            <Panel title="Weekly Trend">
              <ResponsiveContainer width="100%" height={320}>
                <LineChart data={data.weeklyTrend}>
                  <CartesianGrid strokeDasharray="3 3" stroke="#1e293b" />
                  <XAxis dataKey="week" stroke="#94a3b8" />
                  <YAxis stroke="#94a3b8" />
                  <Tooltip />
                  <Line
                    type="monotone"
                    dataKey="meetings"
                    stroke="#10b981"
                    strokeWidth={4}
                  />
                </LineChart>
              </ResponsiveContainer>
            </Panel>
          </>
        )}

        {/* MEETINGS */}
        {page === "meetings" && (
          <Panel title="Recent Meetings">
            <table>
              <thead>
                <tr>
                  <th>ID</th>
                  <th>Title</th>
                  <th>Date</th>
                  <th>Status</th>
                </tr>
              </thead>
              <tbody>
                {data.recentMeetings.map((row, i) => (
                  <tr key={i}>
                    <td>{row.meeting_id}</td>
                    <td>{row.meeting_title}</td>
                    <td>{row.meeting_date}</td>
                    <td>{row.status}</td>
                  </tr>
                ))}
              </tbody>
            </table>
          </Panel>
        )}

        {/* TASKS */}
        {page === "tasks" && (
          <Panel title="Task Center">
            <table>
              <thead>
                <tr>
                  <th>Owner</th>
                  <th>Task</th>
                  <th>Priority</th>
                  <th>Due</th>
                </tr>
              </thead>
              <tbody>
                {data.recentMeetings.map((row, i) => (
                  <tr key={i}>
                    <td>{row.owner}</td>
                    <td>{row.task}</td>
                    <td>{row.priority}</td>
                    <td>{row.due_date}</td>
                  </tr>
                ))}
              </tbody>
            </table>
          </Panel>
        )}

        {/* RISKS */}
        {page === "risks" && (
          <div className="cards">
            <Card title="Open Risks" value={data.risks} />
            <Card title="Critical" value="9" />
            <Card title="Resolved" value="6" />
            <Card title="Overdue" value={data.overdue} />
          </div>
        )}

        {/* ANALYTICS */}
        {page === "analytics" && (
          <>
            <div className="cards">
              <Card title="Completion %" value="92%" />
              <Card title="AI Score" value="8.7" />
              <Card title="Avg Meetings" value={data.meetings} />
              <Card title="Health" value="Excellent" />
            </div>

            <Panel title="Owner Productivity">
              <ResponsiveContainer width="100%" height={320}>
                <BarChart data={data.ownerStats}>
                  <XAxis dataKey="name" />
                  <YAxis />
                  <Tooltip />
                  <Bar dataKey="value" fill="#8b5cf6" />
                </BarChart>
              </ResponsiveContainer>
            </Panel>
          </>
        )}

        {/* SETTINGS */}
        {page === "settings" && (
          <Panel title="System Settings">
            <table>
              <tbody>
                <tr>
                  <td>Backend URL</td>
                  <td>127.0.0.1:8000</td>
                </tr>
                <tr>
                  <td>Environment</td>
                  <td>Local Dev</td>
                </tr>
                <tr>
                  <td>Status</td>
                  <td>Operational</td>
                </tr>
              </tbody>
            </table>
          </Panel>
        )}
      </main>
    </div>
  );
}

function Card({ title, value }) {
  return (
    <div className="card">
      <p>{title}</p>
      <h2>{value}</h2>
    </div>
  );
}

function Panel({ title, children }) {
  return (
    <div className="panel">
      <h3>{title}</h3>
      {children}
    </div>
  );
}

function title(page) {
  const names = {
    dashboard: "Executive Dashboard",
    meetings: "Meetings Center",
    tasks: "Tasks Center",
    risks: "Risk Monitor",
    analytics: "Advanced Analytics",
    settings: "Platform Settings",
  };

  return names[page];
}