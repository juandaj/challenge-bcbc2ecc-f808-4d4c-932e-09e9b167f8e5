# Validación funcional de la solución

## Estado verificado

La solución fue levantada con Docker Compose y se verificó el flujo completo de recolección, consulta, visualización y alertamiento.

### Targets de Prometheus

En `Status -> Target health` se comprobaron tres targets en estado **UP**:

- `apm` -> `app:8000/metrics`
- `infraestructura` -> `node-exporter:9100/metrics`
- `prometheus` -> `prometheus:9090/metrics`

Esto confirma que Prometheus puede realizar scraping correctamente sobre las fuentes configuradas.

## Validación APM

Se generó tráfico controlado contra los endpoints `/work`, `/error` y `/health`.

Prometheus recibió series de la forma:

```text
http_requests_total{endpoint="/work",method="GET",status="200"}
http_requests_total{endpoint="/error",method="GET",status="500"}
http_requests_total{endpoint="/health",method="GET",status="200"}
```

También se verificaron consultas PromQL para:

- throughput HTTP;
- tasa de errores 5xx;
- latencia p95.

Durante la prueba se observó una tasa de errores superior al umbral configurado y la regla `HighHttpErrorRate` pasó a estado **FIRING**, demostrando que las reglas de alerta se evalúan sobre datos reales.

## Validación de infraestructura

Node Exporter expuso métricas reales de la VM Linux, entre ellas:

- `node_cpu_seconds_total`;
- `node_memory_MemAvailable_bytes`;
- `node_memory_MemTotal_bytes`;
- `node_filesystem_*`;
- `node_network_*`.

El dashboard de Grafana mostró utilización de CPU, utilización de memoria y disponibilidad de targets junto con las métricas APM.

## Dashboard

Grafana se provisiona automáticamente con:

- datasource `Prometheus`;
- carpeta `Assessment`;
- dashboard `Assessment - Infraestructura y APM`.

El dashboard integra en una sola vista:

1. CPU utilizada %.
2. Memoria utilizada %.
3. Throughput HTTP (req/s).
4. Tasa de errores 5xx %.
5. Latencia HTTP p95.
6. Disponibilidad de targets.

## Alertas verificadas

Reglas incluidas:

| Pilar | Regla | Condición |
|---|---|---|
| Infraestructura | `HighCpuUsage` | CPU > 85% durante 2 min |
| Infraestructura | `LowAvailableMemory` | memoria disponible < 15% durante 2 min |
| APM | `HighHttpErrorRate` | errores 5xx > 5% durante 1 min |
| APM | `HighP95Latency` | p95 > 1 s durante 2 min |

Los estados esperados son `INACTIVE`, `PENDING` o `FIRING`, según la condición y el tiempo definido con `for`.

## Conclusión

La implementación cubre los dos pilares seleccionados y demuestra el ciclo completo:

```text
Fuente de métricas -> Prometheus -> PromQL -> Grafana / reglas de alerta
```

La solución es reproducible mediante Docker Compose y puede extenderse en un entorno productivo con service discovery, Alertmanager, almacenamiento de larga retención, trazas distribuidas y correlación con logs.
