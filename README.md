# 🚀 Kubernetes Incident Monitor with AI Triage

> A hands-on SRE project simulating real-world incident monitoring using Kubernetes, Docker, and Python — evolving into an **AI-powered self-healing system**.

---

## 📌 Project Overview

This project demonstrates a complete SRE workflow from containerization to AI-driven incident response:

- ⚙️ Build a Python application (Flask)
- 🐳 Containerize using Docker
- 📦 Push image to Docker Hub
- ☸️ Deploy on Kubernetes (Minikube)
- 🌐 Expose service and test endpoints
- 💥 Simulate failures for incident monitoring

The goal is to evolve this into an **AI-powered self-healing system**.

---

## 🧱 Tech Stack

| Layer | Technology |
|---|---|
| Application | Python (Flask) |
| Containerization | Docker |
| Orchestration | Kubernetes (Minikube) |
| CLI | kubectl |
| Registry | Docker Hub |
| AI (Planned) | AI API integration |

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
├── monitor/                # Monitoring scripts (Phase 3)
├── docs/                   # Screenshots and notes
└── README.md
```

---

## ⚙️ Features (Current)

**Flask Endpoints:**
- `GET /` → Basic response
- `GET /health` → Health check
- `GET /error` → Simulate HTTP 500 error

**Infrastructure:**
- ✅ Dockerized application
- ✅ Image pushed to Docker Hub
- ✅ Deployed to Kubernetes cluster (Minikube)
- ✅ Service exposed via ClusterIP
- ✅ Port forwarding for local access
- ✅ Basic logging enabled

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
curl http://127.0.0.1:8080/
curl http://127.0.0.1:8080/health
curl http://127.0.0.1:8080/error
```

---

## 🧪 Simulating Incidents

- `/error` endpoint returns **HTTP 500**
- Logs are generated inside the container
- Useful for **monitoring + alert simulation**

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

### Next Phase  — Monitoring
- [ ] Kubernetes pod monitoring (Python)
- [ ] Health check automation
- [ ] Incident detection (restart loops, failures)
- [ ] Log collection and analysis
- [ ] AI-based root cause analysis
- [ ] Auto-remediation (restart pod, scale, etc.)

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
- Foundation for SRE automation systems

---

## 👨‍💻 Author

**Sandip Kharel**

---
