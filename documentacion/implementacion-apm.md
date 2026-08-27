# Implementación del Monitoreo de APM

## Herramientas utilizadas

- **Aplicación demo instrumentada:** expone métricas Prometheus en `/metrics`.
- **Prometheus:** recopila métricas de solicitudes, errores y duración.
- **Grafana:** visualiza throughput, error rate y latencia p95.

## Flujo

`Cliente -> Aplicación (:8000) -> /metrics -> Prometheus (:9090) -> Grafana (:3000)`

## Instrumentación

La aplicación registra:

- `http_requests_total{method,endpoint,status}`: contador de solicitudes.
- `http_request_duration_seconds`: histograma de duración.

A partir de estas métricas se implementa el enfoque **RED**:

- **Rate:** solicitudes por segundo.
- **Errors:** porcentaje de respuestas 5xx.
- **Duration:** latencia, usando percentil p95.

## Configuración

La configuración solicitada por el reto está en `monitoreo-apm/configuracion-apm.yaml`. La configuración ejecutable de Prometheus está consolidada en `prometheus/prometheus.yml`.

## Alertas

En `prometheus/alerts.yml`:

- **HighHttpErrorRate:** más del 5% de errores 5xx durante 1 minuto.
- **HighP95Latency:** p95 superior a 1 segundo durante 2 minutos.

Los umbrales son demostrativos. En producción deberían derivarse de SLO, comportamiento histórico y tolerancia del negocio.

## Generación de tráfico para la demostración

```bash
for i in $(seq 1 30); do curl -s http://localhost:8000/work > /dev/null; done
for i in $(seq 1 5); do curl -s http://localhost:8000/error > /dev/null; done
```

Después abrir Grafana en `http://localhost:3000` con usuario `admin` y contraseña `admin`. El dashboard **Assessment - Infraestructura y APM** se provisiona automáticamente.

## Consultas útiles

```promql
sum(rate(http_requests_total[1m]))
100 * sum(rate(http_requests_total{status=~"5.."}[5m])) / clamp_min(sum(rate(http_requests_total[5m])), 0.001)
histogram_quantile(0.95, sum by(le) (rate(http_request_duration_seconds_bucket[5m])))
```

## Consideraciones de producción

En un sistema real se añadirían trazas distribuidas con OpenTelemetry, métricas de dependencias externas, correlación con logs, etiquetas controladas para evitar alta cardinalidad, SLI/SLO formales y alertas orientadas a síntomas visibles por el usuario.
