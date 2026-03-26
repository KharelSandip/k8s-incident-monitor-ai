# 🚀 Kubernetes Incident Monitor with AI Triage

> A SRE project simulating real-world incident monitoring using Kubernetes, Docker, Python and evolving into an **AI-powered Triaging system**.

---

## 📌 Project Overview

This project demonstrates a complete SRE workflow from containerization to AI-driven incident response:

- ⚙️ Build a Python application (Flask)
- 🐳 Containerize using Docker
- 📦 Push image to Docker Hub
- ☸️ Deploy on Kubernetes (Minikube)
- 🌐 Expose service and test endpoints
- 💥 Simulate failures for incident monitoring
- 📡 Stream and analyze pod logs in real time
- 🏥 Automated health checks based on detected errors

The goal is to evolve this into an **AI-powered system**.

---

## 🧱 Tech Stack

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

## 📂 Project Structure

```
k8s-incident-monitor-ai/
├── app/                    # Flask application
│   ├── app.py
│   ├── Dockerfile
│   ├── requirements.txt
│   └── templates/
│
├── k8s/                    # Kubernetes manifests
│   ├── deployment.yaml
│   └── service.yaml
│
├── monitor/                # Monitoring scripts 
│   ├── log_monitor.py      # Streams pod logs and detects error patterns
│   └── health_check.py     # Reads alerts and determines system health
│
├── docs/                   # Screenshots and notes
└── README.md
```

---

## ⚙️ Features

### Phase 1 — Flask Application & Kubernetes Deployment

**Flask Endpoints:**
- `GET /` → Basic response
- `GET /health` → Health check
- `GET /error` → Simulate HTTP 500 error
- `GET /login` → User login 

**Infrastructure:**
- ✅ Dockerized application
- ✅ Image pushed to Docker Hub
- ✅ Deployed to Kubernetes cluster (Minikube)
- ✅ Service exposed via ClusterIP
- ✅ Port forwarding for local access
- ✅ Basic logging enabled

###  Kubernetes Log Monitoring & Health Checks ✅

**Log Monitoring (`monitor/log_monitor.py`):**
- ✅ Streams pod logs in real time using the Kubernetes Python client
- ✅ Detects error patterns (e.g. HTTP 500s, crash indicators)
- ✅ Stores triggered alerts to a local file for downstream consumption

**Health Check (`monitor/health_check.py`):**
- ✅ Reads the alerts file produced by the log monitor
- ✅ Evaluates system health based on error frequency/thresholds
- ✅ Reports overall health status (healthy / degraded / critical)

---

## 🐳 Docker Workflow

### Build the image

```bash
docker build -t sandipkhl/k8-monitor-app:v2 ./app
```

### Push to Docker Hub

```bash
docker push sandipkhl/k8-monitor-app:v2
```

---

## ☸️ Kubernetes Deployment

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

## 🌐 Access the Application

### Port forward

```bash
kubectl port-forward service/incident-monitor-service 8080:80
```

### Test endpoints

```bash
curl http://localhost:8080/
curl http://localhost:8080/health
curl http://localhost:8080/error
```

---

## 📡 Running the Monitor

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

## 🧪 Simulating Incidents

- `/error` endpoint returns **HTTP 500**
- Logs are generated inside the container
- The log monitor detects these errors and stores alerts
- The health check script reflects degraded/critical status accordingly

---

## 📸 Screenshots

Screenshots available in `/docs/screenshots` showing:

- Docker build and logs
- Minikube cluster setup
- Kubernetes deployment
- Service exposure
- Application running in browser

---

## 🧠 Planned Features

### Next — AI Triage 
- [ ] AI-based root cause analysis using LLM API
- [ ] Natural language incident summaries from raw logs
- [ ] Auto-remediation (restart pod, scale deployment, etc.)
- [ ] Circuit breaker for auto-healing
- [ ] Alerting integrations (Slack, PagerDuty, etc.)

---

## 🔐 SRE Best Practices (Planned)

- [ ] Idempotent recovery actions
- [ ] Circuit breaker for auto-healing
- [ ] Least privilege IAM usage
- [ ] Observability based on **Golden Signals**:

| Signal | Description |
|---|---|
| Latency | Time to serve requests |
| Errors | Rate of failed requests |
| Traffic | Demand on the system |
| Saturation | How "full" the service is |

---

## 🚀 Learning Outcomes

- Hands-on Kubernetes deployment
- Docker image lifecycle: build → push → pull
- Debugging containerized applications
- Service exposure and networking
- Real-time log streaming and pattern detection
- Health evaluation from structured alert data
- Foundation for SRE automation systems

---

## 👨‍💻 Author

**Sandip Kharel**

---