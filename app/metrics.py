from fastapi import APIRouter, Response
import psutil
import time
from prometheus_client import Gauge, Counter, generate_latest, CONTENT_TYPE_LATEST

router = APIRouter()
START_TIME = time.time()

cpu_usage = Gauge("service_health_cpu_usage_percent", "CPU usage")
memory_usage = Gauge("service_health_memory_usage_percent", "Memory usage")
disk_usage = Gauge("service_health_disk_usage_percent", "Disk usage")
uptime = Gauge("service_health_uptime_seconds", "Uptime")
http_requests = Counter("service_health_http_requests_total", "HTTP requests")

@router.get("")
def metrics():
    http_requests.inc()
    cpu_usage.set(psutil.cpu_percent(interval=0.1))
    memory_usage.set(psutil.virtual_memory().percent)
    disk_usage.set(psutil.disk_usage("/").percent)
    uptime.set(time.time() - START_TIME)

    return Response(
        generate_latest(),
        media_type=CONTENT_TYPE_LATEST
    )
