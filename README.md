# 🏢 LeadGen & Data Capture Architecture - Real Estate

## 🎯 Resumen del Proyecto
Diseño y desarrollo *end-to-end* de un embudo de ventas digital automatizado para el sector inmobiliario. Este proyecto sustituye los formularios tradicionales por una arquitectura asíncrona que reduce la fricción del usuario y estructura los datos en tiempo real para el análisis de marketing.

## ⚙️ Arquitectura Técnica
El sistema está dividido en dos micro-entornos:

1. **Frontend (Interfaz y Conversión):**
   - Landing Page "One-Page" construida con HTML5 y CSS3 (Responsive Design).
   - Motor de captura en Vanilla JavaScript (Fetch API) para envío de datos asíncrono sin recarga de página.
   - Extracción automática de parámetros UTM de la URL para atribución de campañas publicitarias.

2. **Backend (Procesamiento y Almacenamiento):**
   - Microservicio desarrollado en **Python 3** utilizando **FastAPI**.
   - Recepción de payloads en formato JSON.
   - Estructuración y escritura automática de los *leads* en una base de datos tabular (`.csv`), organizando fechas, datos de contacto, nivel de interés y origen de la campaña (Marketing Attribution).

## 🚀 Valor de Negocio (KPIs y ROI)
- **Fricción Cero:** El prospecto experimenta una transición inmediata a WhatsApp, mientras el sistema procesa sus datos en segundo plano.
- **Data-Driven:** Almacenamiento estructurado listo para cruzar con herramientas de visualización o CRMs, permitiendo calcular el Costo por Lead (CPL) real por campaña.
- **Escalabilidad:** Código modular preparado para integrar *Lead Scoring* o conexiones vía Webhooks a herramientas de automatización empresariales.

## 🛠️ Stack Tecnológico
`Python` `FastAPI` `Uvicorn` `HTML5` `CSS3` `JavaScript` `Git`
