# Kubernetes Incident Monitor with AI Triage

## Overview
This project simulates a SRE incident monitoring workflow in Kubernetes.

It monitors pod health and service availability, collects debugging context such as logs and events, and uses AI to classify incidents and suggest next troubleshooting steps.

## Goals
- Detect Kubernetes pod failures
- Check service health endpoints
- Collect logs and events when incidents happen
- Generate simple incident summaries
- Use AI for triage and explanation

## Planned Features
- Pod health monitoring
- Restart count alerts
- CrashLoopBackOff detection
- Service health checks
- Log and event collection
- AI incident classification
- Incident report generation

## Tech Stack
- Kubernetes
- Python
- Kubernetes Python client
- Docker
- AI API integration

## Project Structure
- `app/` sample application
- `k8s/` Kubernetes manifests
- `monitor/` monitoring scripts
- `ai/` AI triage logic
- `reports/` generated incident reports
- `docs/` diagrams and screenshots

## Status
Project setup in progress.