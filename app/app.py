import random
import time
from flask import Flask, Response, jsonify
from prometheus_client import Counter, Histogram, generate_latest, CONTENT_TYPE_LATEST

app = Flask(__name__)

REQUESTS = Counter(
    "http_requests_total",
    "Total de solicitudes HTTP procesadas",
    ["method", "endpoint", "status"],
)

REQUEST_LATENCY = Histogram(
    "http_request_duration_seconds",
    "Duración de las solicitudes HTTP en segundos",
    ["method", "endpoint"],
    buckets=(0.01, 0.025, 0.05, 0.1, 0.25, 0.5, 1, 2.5, 5),
)


def observe(endpoint):
    def decorator(fn):
        def wrapper(*args, **kwargs):
            start = time.perf_counter()
            status = "200"
            try:
                response = fn(*args, **kwargs)
                if isinstance(response, tuple):
                    status = str(response[1])
                return response
            except Exception:
                status = "500"
                raise
            finally:
                REQUESTS.labels("GET", endpoint, status).inc()
                REQUEST_LATENCY.labels("GET", endpoint).observe(time.perf_counter() - start)
        wrapper.__name__ = fn.__name__
        return wrapper
    return decorator


@app.get("/")
@observe("/")
def index():
    return jsonify(
        service="fintech-monitoring-demo",
        status="ok",
        endpoints=["/health", "/work", "/error", "/metrics"],
    )


@app.get("/health")
@observe("/health")
def health():
    return jsonify(status="UP")


@app.get("/work")
@observe("/work")
def work():
    time.sleep(random.uniform(0.05, 0.6))
    return jsonify(message="transacción simulada procesada")


@app.get("/error")
@observe("/error")
def error():
    return jsonify(error="error simulado para validar APM"), 500


@app.get("/metrics")
def metrics():
    return Response(generate_latest(), mimetype=CONTENT_TYPE_LATEST)
