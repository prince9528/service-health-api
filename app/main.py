from fastapi import FastAPI
from app.metrics import router as metrics_router
import socket
import time

app = FastAPI(title="Service Health API v2")

START_TIME = time.time()

@app.get("/")
def root():
    return {
        "service": "service-health-api",
        "version": "v2",
        "endpoints": ["/health", "/metrics", "/info"]
    }

@app.get("/health")
def health():
    return {
        "status": "UP",
        "version": "v2",
        "host": socket.gethostname(),
        "uptime_seconds": int(time.time() - START_TIME)
    }

@app.get("/info")
def info():
    return {
        "service": "service-health-api",
        "version": "v2",
        "environment": "dev"
    }

app.include_router(metrics_router, prefix="/metrics")
