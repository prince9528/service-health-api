# service-health-api-v3

Service Health & CI Metrics Dashboard (v3)

## 🚀 Overview

`service-health-api-v3` is an evolution of v2 that adds:
- Containerized Jenkins CI
- Prometheus metrics for CI pipelines
- Grafana dashboards for application and CI observability
- Kubernetes-native observability components

## 🧱 Architecture

- **FastAPI** backend exposing health & system metrics
- **Prometheus** scrapes:
  - Application metrics
  - Jenkins pipeline metrics
- **Grafana** visualizes:
  - App health
  - CI build success/failure
- **Jenkins (Dockerized)** handles CI
- **Kubernetes manifests** remain the source of truth

## 📁 Repository Structure

service-health-api-v3/
├── app/
│   ├── main.py
│   ├── metrics.py
│   └── __init__.py
│
├── docker/
│   ├── app/
│   │   └── Dockerfile
│   └── jenkins/
│       ├── Dockerfile
│       └── plugins.txt
│
├── compose/
│   └── docker-compose.yml
│
├── k8s/
│   ├── deployment.yaml
│   ├── service.yaml
│   │
│   ├── prometheus/
│   │   ├── config.yaml          # Prometheus config (metrics + Jenkins)
│   │   └── deployment.yaml
│   │
│   └── grafana/
│       ├── deployment.yaml
│       └── dashboards/
│
├── Jenkinsfile
├── requirements.txt
├── .dockerignore
└── README.md
