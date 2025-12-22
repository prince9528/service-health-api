from fastapi import APIRouter
import psutil

router = APIRouter()

@router.get("")
def metrics():
    return {
        "cpu_percent": psutil.cpu_percent(interval=0.1),
        "memory": {
            "total_mb": int(psutil.virtual_memory().total / 1024 / 1024),
            "used_mb": int(psutil.virtual_memory().used / 1024 / 1024),
            "percent": psutil.virtual_memory().percent
        },
        "disk": {
            "total_gb": int(psutil.disk_usage("/").total / 1024 / 1024 / 1024),
            "used_gb": int(psutil.disk_usage("/").used / 1024 / 1024 / 1024),
            "percent": psutil.disk_usage("/").percent
        }
    }
