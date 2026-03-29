#  Kubernetes Incident Monitor with AI Triage

> A SRE project simulating real-world incident monitoring using Kubernetes, Docker, Python and evolving into an **AI-powered Triaging system**.

---

## Project Overview

This project demonstrates a complete SRE workflow from containerization to AI-driven incident response:

-  Build a Python application (Flask)
-  Containerize using Docker
-  Push image to Docker Hub
-  Deploy on Kubernetes (Minikube)
-  Expose service and test endpoints
-  Simulate failures for incident monitoring
-  Stream and analyze pod logs in real time
-  Automated health checks based on detected errors
-  Use of AI for triaging.

---

##  Tech Stack

| Layer | Technology |
|---|---|
| Application | Python (Flask) |
| Containerization | Docker |
| Orchestration | Kubernetes (Minikube) |
| CLI | kubectl |
| Registry | Docker Hub |
| Monitoring | Python (log streaming, health checks) |
| AI  | AI API integration |

---

##  Project Structure

## Project Structure

```bash
k8s-incident-monitor-ai/
├── app/
│   └── app.py
├── ai/
│   ├── ai_triage.py
│   └── prompt.txt
├── k8s/
│   ├── deployment.yaml
│   └── service.yaml
├── monitor/
│   ├── log_monitor.py
│   ├── health_check.py
│   └── reports/
│       └── alerts.txt
├── docs/
├── dashboard.sh
├── requirements.txt
├── README.md
└── .gitignore
```

## ⚙️ Features

### Flask Application & Kubernetes Deployment

**Flask Endpoints:**
- `GET /` → Basic response
- `GET /health` → Health check
- `GET /error` → Simulate HTTP 500 error
- `GET /login` → User login 

**Infrastructure:**
-  Dockerized application
-  Image pushed to Docker Hub
-  Deployed to Kubernetes cluster (Minikube)
-  Service exposed via ClusterIP
-  Port forwarding for local access
-  Basic logging enabled

###  Kubernetes Log Monitoring & Health Checks 

**Log Monitoring (`monitor/log_monitor.py`):**
-  Streams pod logs in real time using the Kubernetes Python client
-  Detects error patterns (e.g. HTTP 500s, crash indicators)
-  Stores triggered alerts to a local file for downstream consumption

**Health Check (`monitor/health_check.py`):**
-  Reads the alerts file produced by the log monitor
-  Evaluates system health based on error frequency/thresholds
-  Reports overall health status (healthy / degraded / critical)

---
##  AI Triage

In the project, I adds AI-based incident analysis.

The AI triage script reads the latest alert from `monitor/reports/alerts.txt`, sends it to an AI model, and returns a short incident explanation.

### What it does

- Reads the latest alert from the alerts file
- Sends the alert to AI for analysis
- Returns:
  - what happened
  - possible cause
  - suggested fix

### Example flow

```text
Application error -> log monitor detects error -> alert stored in alerts.txt -> AI 
```

### Example alert
```text
2026-03-26 00:38:12 ALERT: ERROR:app:Intentional 500 error triggered
```

## Docker Workflow

### Build the image

```bash
docker build -t sandipkhl/k8-monitor-app:v2 ./app
```

### Push to Docker Hub

```bash
docker push sandipkhl/k8-monitor-app:v2
```

---

## Kubernetes Deployment

### 1. Start Minikube

```bash
minikube start
```

### 2. Apply manifests

```bash
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml
```

### 3. Verify resources

```bash
kubectl get pods
kubectl get svc
```

---

## Access the Application

### Port forward

```bash
kubectl port-forward service/incident-monitor-service 8080:80
```

### Test endpoints

```bash
curl http://localhost:8080/
curl http://localhost:8080/health
curl http://localhost:8080/error
curl http://localhost:8080/login
```

---

## Running the Monitor

### Stream logs and detect errors

```bash
python monitor/log_monitor.py
```

Streams logs from running pods, flags error patterns, and writes alerts to a local file.

### Check system health

```bash
python monitor/health_check.py
```

Reads the alerts file and outputs a health status based on the number and frequency of detected errors.

---

##  Simulating Incidents

- `/error` endpoint returns **HTTP 500**
- Logs are generated inside the container
- The log monitor detects these errors and stores alerts
- The health check script reflects degraded/critical status accordingly

---

## Screenshots

Screenshots available in `/docs/screenshots` showing:

- Docker build and logs
- Minikube cluster setup
- Kubernetes deployment
- Service exposure
- Application running in browser



##  Learning Outcomes

- Hands-on Kubernetes deployment
- Docker image lifecycle: build → push → pull
- Debugging containerized applications
- Service exposure and networking
- Real-time log streaming and pattern detection
- Health evaluation from structured alert data
- Foundation for SRE automation systems

---

##  Author

**Sandip Kharel**

---