# Métricas Seleccionadas

## Estrategia

Se seleccionan los pilares **Infraestructura** y **APM** porque se complementan: infraestructura permite identificar si la plataforma dispone de recursos suficientes y APM permite observar el impacto real sobre las transacciones de negocio.

Para infraestructura se aplica el enfoque **USE** (Utilization, Saturation, Errors) y para la aplicación el enfoque **RED** (Rate, Errors, Duration).

## Métricas de Infraestructura

| Métrica | PromQL de referencia | Justificación |
|---|---|---|
| Utilización de CPU | `100 - (avg(rate(node_cpu_seconds_total{mode="idle"}[5m])) * 100)` | Un uso sostenido alto puede incrementar latencia, producir saturación y afectar la capacidad de procesar transacciones. |
| Utilización de memoria | `(1 - node_memory_MemAvailable_bytes / node_memory_MemTotal_bytes) * 100` | Permite anticipar presión de memoria, swapping u OOM que pueden degradar o interrumpir servicios. |
| Disponibilidad del target | `up{job="infraestructura"}` | Detecta si Prometheus puede recopilar métricas del host. Un valor `0` indica indisponibilidad del exporter o del nodo. |

## Métricas de APM

| Métrica | PromQL de referencia | Justificación |
|---|---|---|
| Rate / throughput | `sum(rate(http_requests_total[1m]))` | Permite conocer la carga real de la aplicación y correlacionarla con consumo de infraestructura. |
| Tasa de errores 5xx | `sum(rate(http_requests_total{status=~"5.."}[5m])) / sum(rate(http_requests_total[5m]))` | Los errores impactan directamente al usuario y pueden representar transacciones fallidas. |
| Latencia p95 | `histogram_quantile(0.95, sum by(le) (rate(http_request_duration_seconds_bucket[5m])))` | p95 representa la experiencia de la mayoría de usuarios mejor que un promedio simple y ayuda a detectar degradación. |
| Disponibilidad de la aplicación | `up{job="apm"}` | Confirma que el endpoint de métricas y la aplicación están accesibles. |

## Relación con el negocio

En un sistema fintech no basta con saber que un servidor está encendido. Una CPU estable puede coexistir con transacciones lentas o fallidas. Por eso se correlacionan métricas técnicas con métricas de aplicación: si aumenta el p95 al mismo tiempo que CPU o memoria se saturan, existe evidencia para investigar capacidad; si crecen los errores sin presión de infraestructura, el problema probablemente está en la aplicación o sus dependencias.
