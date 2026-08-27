# Implementación de monitoreo en un sistema de infraestructura distribuida

Solución del reto de **Pilares de Monitoreo** implementando dos pilares: **Infraestructura** y **APM**.

## Arquitectura

```text
Host Linux -> Node Exporter ----\
                                -> Prometheus -> Grafana
Aplicación /metrics ------------/
```

## Componentes

- `app/`: aplicación Flask instrumentada con métricas Prometheus.
- `prometheus/`: scraping y reglas de alertas.
- `grafana/`: datasource y dashboard provisionados automáticamente.
- `monitoreo-infraestructura/`: YAML requerido por el entregable de infraestructura.
- `monitoreo-apm/`: YAML requerido por el entregable de APM.
- `documentacion/`: selección de métricas, implementación y preguntas de sustentación.

## Ejecución

Requisitos: Docker y Docker Compose.

```bash
docker compose up -d --build
docker compose ps
```

Servicios:

- Aplicación: http://localhost:8000
- Métricas de aplicación: http://localhost:8000/metrics
- Prometheus: http://localhost:9090
- Grafana: http://localhost:3000 (`admin` / `admin`)
- Node Exporter: http://localhost:9100/metrics

## Validación rápida

1. En Prometheus abrir `Status -> Target health` y verificar los jobs `prometheus`, `infraestructura` y `apm` en estado **UP**.
2. Generar tráfico:

```bash
for i in $(seq 1 30); do curl -s http://localhost:8000/work > /dev/null; done
for i in $(seq 1 5); do curl -s http://localhost:8000/error > /dev/null; done
```

3. Abrir Grafana y entrar a `Dashboards -> Assessment -> Assessment - Infraestructura y APM`.
4. Revisar alertas en Prometheus en `Alerts`.

## Detener

```bash
docker compose down
```

Para eliminar también los datos persistidos:

```bash
docker compose down -v
```

## Métricas principales

**Infraestructura:** CPU, memoria y disponibilidad.

**APM:** throughput, tasa de errores 5xx, latencia p95 y disponibilidad.

## Evidencia y sustentación

La validación funcional está documentada en `documentacion/validacion-resultados.md` y las preguntas de preparación en `documentacion/preguntas-respuestas.md`.

### Nota sobre permisos al extraer el ZIP

Si Grafana inicia pero no provisiona el dashboard y sus logs muestran `permission denied` sobre `/etc/grafana/provisioning`, asegurar permisos de lectura/ejecución:

```bash
find grafana -type d -exec chmod 755 {} \;
find grafana -type f -exec chmod 644 {} \;
docker compose restart grafana
```

En producción no se deben conservar las credenciales `admin/admin`; se usan aquí únicamente para simplificar la demostración local.
