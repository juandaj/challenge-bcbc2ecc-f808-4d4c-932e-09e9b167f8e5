# Preguntas y Respuestas para Sustentación

## ¿Qué son los pilares de monitoreo?
Son perspectivas complementarias para conocer la salud de un sistema. Infraestructura observa recursos y disponibilidad; Log Management centraliza eventos; APM observa comportamiento y rendimiento de aplicaciones. En este reto se implementan Infraestructura y APM.

## ¿Por qué Prometheus y Grafana?
Prometheus es apropiado para métricas de series temporales, scraping y consultas PromQL. Grafana aporta visualización y dashboards. Se separan responsabilidades: Prometheus recolecta/consulta y Grafana presenta.

## ¿Qué diferencia hay entre monitoreo y observabilidad?
Monitoreo responde preguntas conocidas mediante métricas y alertas predefinidas. Observabilidad busca poder inferir el estado interno del sistema a partir de sus señales y facilita investigar preguntas no previstas usando métricas, logs y trazas.

## ¿Qué es APM?
Application Performance Monitoring consiste en medir disponibilidad, rendimiento y errores de una aplicación y sus transacciones para detectar degradaciones y entender su impacto en los usuarios.

## ¿Qué es RED?
Rate, Errors y Duration. Es un enfoque útil para servicios: cuántas solicitudes llegan, cuántas fallan y cuánto tardan.

## ¿Qué es USE?
Utilization, Saturation y Errors. Es un enfoque para recursos de infraestructura: cuánto se utiliza el recurso, qué tan cerca está de su capacidad y qué errores presenta.

## ¿Por qué usar p95 y no solo promedio?
El promedio puede ocultar solicitudes muy lentas. p95 indica que el 95% de las observaciones están por debajo de ese valor y evidencia mejor la experiencia de usuarios afectados por la cola de latencia.

## ¿Qué significa `up` en Prometheus?
Es una métrica generada por Prometheus. Vale `1` si el último scrape del target fue exitoso y `0` si falló. No garantiza por sí sola que toda la funcionalidad de negocio esté correcta.

## ¿Qué es scraping?
Es el proceso mediante el cual Prometheus consulta periódicamente un endpoint HTTP de métricas, normalmente `/metrics`, y almacena las muestras obtenidas.

## ¿Qué es PromQL?
Es el lenguaje de consulta de Prometheus para seleccionar, agregar y calcular series temporales. Permite construir dashboards y reglas de alerta.

## ¿Cómo se calcula una tasa de errores?
Se divide el rate de solicitudes fallidas entre el rate total de solicitudes dentro de una ventana temporal. Para HTTP suelen considerarse 5xx como errores del servicio.

## ¿Por qué no alertar inmediatamente ante un pico?
Los picos pueden ser transitorios. Utilizar una ventana y una cláusula `for` reduce falsos positivos y fatiga de alertas.

## ¿Qué error común existe con las etiquetas?
Agregar valores de alta cardinalidad, por ejemplo un `userId`, `transactionId` o URL única. Esto multiplica las series temporales y puede degradar Prometheus.

## ¿Cuál es la diferencia entre métrica, log y traza?
Una métrica resume comportamiento numérico en el tiempo; un log registra eventos discretos con contexto; una traza sigue una solicitud a través de varios componentes o servicios.

## ¿Qué son SLI, SLO y SLA?
SLI es el indicador medido, por ejemplo disponibilidad. SLO es el objetivo interno, por ejemplo 99.9%. SLA es el compromiso contractual y puede incluir consecuencias por incumplimiento.

## ¿Cómo escalarías esta solución?
Usaría service discovery en lugar de targets estáticos, Alertmanager, retención remota o una solución escalable como Thanos/Mimir según la necesidad, Grafana con autenticación corporativa y OpenTelemetry para trazas y correlación entre señales.

## ¿Por qué seleccionamos Infraestructura + APM?
Porque permiten correlacionar causa técnica y experiencia de usuario. Infraestructura muestra presión de recursos; APM evidencia si las transacciones se vuelven lentas o fallan. Juntas dan una visión más útil que cualquiera de las dos de forma aislada.

# Preguntas alineadas con las dimensiones evaluadas

## queEs — ¿Qué son los pilares de monitoreo y por qué son importantes?
Son enfoques complementarios para observar diferentes capas del sistema. Infraestructura permite conocer la salud y capacidad de los recursos; APM permite conocer rendimiento, errores y experiencia de las transacciones de aplicación; Log Management centraliza eventos y contexto. Son importantes porque un servidor aparentemente saludable no garantiza que una transacción de negocio esté funcionando correctamente.

## paraQueSirve — ¿Para qué sirven las métricas seleccionadas en el negocio?
CPU y memoria permiten anticipar saturación de capacidad. Throughput muestra la carga que recibe la aplicación. Error rate evidencia transacciones fallidas y latencia p95 permite detectar degradación en la experiencia de los usuarios. La disponibilidad confirma si los componentes pueden ser observados y están accesibles.

## comoSeUsa — ¿Cómo está implementado el monitoreo en este reto?
Node Exporter y la aplicación exponen métricas HTTP. Prometheus las recolecta cada 15 segundos mediante scraping, las almacena como series temporales y permite consultarlas con PromQL. Grafana utiliza Prometheus como datasource y presenta un dashboard provisionado automáticamente. Prometheus también evalúa reglas de alerta definidas en `alerts.yml`.

## erroresComunes — ¿Qué errores evitarías al implementar esta solución?
Evitaría alta cardinalidad de labels, alertas sin ventanas o sin `for`, métricas sin relación con impacto de negocio, credenciales por defecto en producción, retención insuficiente, targets estáticos en ambientes dinámicos y considerar `up=1` como prueba de que toda la funcionalidad de negocio está sana.

## queDecisionesImplica — ¿Qué decisiones tuvimos que tomar?
Se eligieron Infraestructura y APM porque permiten correlacionar recursos y experiencia del usuario. Se seleccionaron Prometheus y Grafana por su modelo de series temporales, PromQL y visualización. Los umbrales de alerta del reto son demostrativos; en producción deben derivarse de SLO, históricos y tolerancia al riesgo del negocio. También se decidió usar percentil p95 en lugar de depender solo del promedio.
