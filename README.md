# Implementación de monitoreo en un sistema de infraestructura distribuida

El sistema de infraestructura distribuida de una empresa fintech necesita ser monitoreado para asegurar su rendimiento y disponibilidad. El equipo de DevOps ha identificado que es necesario implementar al menos dos de los tres pilares de monitoreo: Infraestructura, Log Management y APM. El objetivo es monitorear las métricas más impactantes para el negocio y garantizar la escalabilidad y fiabilidad del sistema.

## Informacion General

| Campo | Valor |
|-------|-------|
| **Tema** | Pilares de monitoreo |
| **Nivel** | senior-l2 |
| **Tipo** | practical |
| **Tiempo estimado** | 4-5 horas |

## Fases del Reto

### Fase 0: Configuración del Proyecto

**Objetivo:** Obtener el proyecto base funcional enviando el Código Base a un asistente de IA, que lo analizará, corregirá errores y generará un ZIP listo para usar.

**Tiempo estimado:** 15-30 minutos

**Instrucciones:**

- Asegúrate de tener instalado para ejecutar el proyecto: Un IDE o editor de código.
- Copia todo el contenido del campo **Código Base** de este reto — incluyendo el texto de instrucciones que aparece al inicio.
- Abre un asistente de IA (Claude en claude.ai, ChatGPT o Gemini — se recomienda Claude), pega el contenido copiado en el chat y envíalo.
- El asistente analizará los archivos, corregirá errores y generará un archivo ZIP descargable. Descárgalo y extráelo en la carpeta donde quieras trabajar.
- Verifica que el proyecto arranca sin errores.

**Entregable:** El proyecto compila/arranca sin errores.

<details>
<summary>Pistas de conocimiento</summary>

- Copia el Código Base completo incluyendo el texto de instrucciones al inicio — esas instrucciones le indican al asistente exactamente qué hacer con los archivos.
- Si el asistente no genera el ZIP automáticamente al terminar el análisis, escríbele: "genera el ZIP ahora".
- Si el proyecto tiene errores al arrancar, comparte el mensaje de error con el mismo asistente para que lo corrija.

</details>

### Fase 1: Exploración del sistema y definición de métricas

**Objetivo:** Identificar las métricas más relevantes para el negocio y definir cómo se monitorearán.

**Tiempo estimado:** 1 hora

**Instrucciones:**

- Analiza el sistema de infraestructura distribuida y determina cuáles son las métricas más críticas para el negocio.
- Define al menos dos métricas que se monitorearán utilizando los pilares de monitoreo seleccionados.

**Entregable:** Documento con las métricas seleccionadas y la justificación de su elección.

<details>
<summary>Pistas de conocimiento</summary>

- Considera el impacto de cada métrica en el negocio y la escalabilidad del sistema.
- Piensa en cómo los diferentes pilares de monitoreo pueden complementar cada uno.

</details>

### Fase 2: Implementación del monitoreo de infraestructura

**Objetivo:** Implementar el monitoreo de la infraestructura utilizando uno de los pilares seleccionados.

**Tiempo estimado:** 2 horas

**Instrucciones:**

- Selecciona uno de los pilares de monitoreo y diseña la implementación para monitorear la infraestructura.
- Configura las herramientas necesarias para recopilar y visualizar las métricas seleccionadas.

**Entregable:** Configuración y documentación de la implementación del monitoreo de infraestructura.

<details>
<summary>Pistas de conocimiento</summary>

- Considera la escalabilidad y la fiabilidad del sistema al implementar el monitoreo.
- Piensa en cómo puedes aprovechar las herramientas disponibles para recopilar y visualizar las métricas.

</details>

### Fase 3: Implementación del monitoreo de APM

**Objetivo:** Implementar el monitoreo de APM utilizando uno de los pilares seleccionados.

**Tiempo estimado:** 2 horas

**Instrucciones:**

- Selecciona uno de los pilares de monitoreo y diseña la implementación para monitorear las transacciones y rendimiento de las aplicaciones.
- Configura las herramientas necesarias para recopilar y visualizar las métricas seleccionadas.

**Entregable:** Configuración y documentación de la implementación del monitoreo de APM.

<details>
<summary>Pistas de conocimiento</summary>

- Considera el impacto de las métricas en el rendimiento y la disponibilidad de las aplicaciones.
- Piensa en cómo puedes aprovechar las herramientas disponibles para recopilar y visualizar las métricas.

</details>

## Dimensiones Evaluadas

- **queEs**: ¿Qué son los pilares de monitoreo y por qué son importantes para el sistema?
- **paraQueSirve**: ¿Para qué sirven las métricas seleccionadas en el contexto del negocio?
- **comoSeUsa**: ¿Cómo se implementa el monitoreo de infraestructura y APM utilizando los pilares seleccionados?
- **erroresComunes**: ¿Cuáles son los errores comunes al implementar el monitoreo y cómo se pueden evitar?
- **queDecisionesImplica**: ¿Qué decisiones implica la selección de los pilares de monitoreo y las métricas?

## Criterios de Evaluacion

- Identificación de las métricas más relevantes para el negocio.
- Implementación del monitoreo de infraestructura utilizando uno de los pilares seleccionados.
- Implementación del monitoreo de APM utilizando uno de los pilares seleccionados.
- Documentación clara y completa de las implementaciones.

---

*Reto generado automaticamente por Challenge Generator - Pragma*
