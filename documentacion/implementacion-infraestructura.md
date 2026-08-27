# Implementación del Monitoreo de Infraestructura

## Herramientas utilizadas

- **Node Exporter:** expone métricas del host Linux, como CPU, memoria, filesystem y red.
- **Prometheus:** recopila las métricas mediante un modelo pull cada 15 segundos y almacena series temporales.
- **Grafana:** consulta Prometheus y presenta los indicadores en un dashboard.

## Flujo

`Host Linux -> Node Exporter (:9100) -> Prometheus (:9090) -> Grafana (:3000)`

## Configuración

La configuración solicitada por el reto se conserva en `monitoreo-infraestructura/configuracion-infraestructura.yaml`. Para la demostración ejecutable con Docker Compose, Prometheus utiliza `prometheus/prometheus.yml`.

El job `infraestructura` consulta `node-exporter:9100` cada 15 segundos. El dashboard muestra CPU, memoria y disponibilidad.

## Alertas

En `prometheus/alerts.yml` se incluyen dos ejemplos:

- **HighCpuUsage:** CPU superior al 85% durante 2 minutos.
- **LowAvailableMemory:** memoria disponible inferior al 15% durante 2 minutos.

El uso de una condición durante un periodo (`for`) evita alertar por picos breves y reduce ruido operacional.

## Escalabilidad y fiabilidad

En un ambiente real se usaría descubrimiento dinámico de servicios en lugar de targets estáticos, almacenamiento persistente o remoto para retención prolongada, alta disponibilidad de Prometheus cuando el RTO lo exija, y Alertmanager para enrutar notificaciones.

## Validación

```bash
docker compose up -d --build
docker compose ps
```

Abrir Prometheus en `http://localhost:9090/targets`. Los jobs `prometheus`, `infraestructura` y `apm` deben aparecer con estado **UP**.

Consultas útiles:

```promql
up
100 - (avg(rate(node_cpu_seconds_total{mode="idle"}[5m])) * 100)
(1 - node_memory_MemAvailable_bytes / node_memory_MemTotal_bytes) * 100
```
