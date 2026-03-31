# k8s-incident-monitor-ai

A Kubernetes incident monitoring tool that detects cluster issues and triages them using AI, either via the OpenAI or a local LLaMA 3.2 model running on local machine.

---

## What it does

- Watches your Kubernetes cluster for common issues (Errors, CrashLoopBackOff, OOMKilled, Pending pods etc.)
- Sends detected incidents to an AI model for triage, root cause analysis and basic info of the issue
- Displays everything in a live tmux dashboard that auto-refreshes every 2 seconds

---

## Requirements

- `kubectl` configured and connected to a cluster
- `tmux`
- **For cloud AI:**  **OpenAI API KEY**
- **For local AI:**   **Ollama with `llama3.2`**

---

## Setup

```bash
git clone https://github.com/KharelSandip/k8s-incident-monitor-ai.git
cd k8s-incident-monitor-ai
chmod +x dashboard.sh
```

---

## AI Triage Modes

### Cloud AI — Anthropic API (Claude)

Export your API key, then run the dashboard:

```bash
export OPENAI_API_KEY="sk-your-key-here"
./dashboard.sh 
```

The monitor formats each incident into a prompt and calls the OpenAI API. OpenAI returns a triage response with a likely root cause and remediation steps.

### Local AI — Ollama + LLaMA 3.2

No API key or internet needed. Triage runs entirely on your machine.

```bash
# Install Ollama and pull the model
ollama pull llama3.2

# Start the local server
ollama serve

# Edit and Run the dashboard
./dashboard.sh
```

Incidents are sent to `localhost:11434` where LLaMA 3.2 handles triage locally using the Ollama framework.

---

## Dashboard

Launches a tmux session with 3 panes:

```
┌──────────────────┬──────────────────┐
│  Cluster Health  │  Live Incidents  │
│  (pods & nodes)  │  (anomalies)     │
│                  ├──────────────────┤
│                  │  AI Triage       │
│                  │  (cloud/local)   │
└──────────────────┴──────────────────┘
```

All panes use `watch -n 2` and refresh automatically.

To stop the dashboard:

```bash
tmux kill-session -t k8s-monitor
```

---

## Project Structure

```
k8s-incident-monitor-ai/
├── dashboard.sh          # Launches the tmux dashboard
├── scripts/
│   ├── detect_incidents.sh
│   ├── triage.sh         # Picks cloud_ai or local_ai
│   ├── cloud_ai.sh       # Calls Anthropic API
│   └── local_ai.sh       # Calls Ollama locally
└── README.md
```

---

## Work in Progress

- Slack / PagerDuty alerting
- Multi-cluster support
- Auto-remediation with confirmation prompt
- Helm chart for in-cluster deployment