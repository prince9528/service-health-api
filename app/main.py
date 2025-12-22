from fastapi import FastAPI
from app.metrics import router as metrics_router
import socket
import time

app = FastAPI(title="Service Health API")

START_TIME = time.time()

@app.get("/health")
def health():
    return {
        "status": "UP",
        "host": socket.gethostname(),
        "uptime_seconds": int(time.time() - START_TIME)
    }

@app.get("/info")
def info():
    return {
        "service": "service-health-api",
        "version": "1.0.0",
        "environment": "dev"
    }

app.include_router(metrics_router, prefix="/metrics")
