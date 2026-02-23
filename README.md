# 🤖 Swarm Bots Core

**Sistema de enjambres de robots con generación automática de reportes ISO 9001**

> *"Transformando datos de sensores en decisiones auditables para PYMES"*

---

## 🎯 Visión

Desarrollar un sistema de **enjambres de robots heterogéneos** (aéreos, terrestres, acuáticos) de bajo costo que puedan inspeccionar infraestructura industrial, agrícola y logística, generando automáticamente **documentación auditables** bajo normas ISO 9001/19011.

### 💡 ¿Por qué existe este proyecto?

Las PYMES necesitan:
- ✅ Inspecciones más rápidas y económicas
- ✅ Documentación automática para auditorías ISO
- ✅ Soluciones que funcionen con conectividad limitada
- ✅ Tecnología accesible sin sacrificar calidad

---

## 🚀 Características Principales

| Característica | Descripción |
|----------------|-------------|
| 🤖 **Multi-Robot** | Soporta drones, robots terrestres y acuáticos |
| 📋 **ISO 9001/19011** | Genera reportes automáticamente alineados a normas ISO |
| 🌐 **Global-Ready** | Diseñado para operar en mercados emergentes |
| 💾 **Edge-AI** | Funciona con conectividad limitada o nula |
| 🔧 **Modular** | Arquitectura escalable y personalizable |
| 📊 **Simulación** | Permite probar antes de implementar hardware real |

---

## 📁 Estructura del Proyecto

---

## 🛠️ Instalación y Uso

### Requisitos previos

- Python 3.8 o superior
- pip (gestor de paquetes de Python)

### Paso 1: Clonar el repositorio

```bash
git clone https://github.com/ferobelar-byte/swarm-bots-core.git
cd swarm-bots-core
pip install python-docx
# Simular sensores de robots
py simulador_sensores.py

# Generar reporte ISO manualmente
py generador_reporte_iso.py

# Sistema completo integrado
py swarm_bots_v1.py

# Menú interactivo
py menu.py
# El dron escanea una torre
Robot: DRONE-001
Ubicación: Torre A - Nivel 3
Sensor: temperatura = 45.5°C
Estado: ALERTA (excede límite de 40°C)

# El sistema genera automáticamente:
✅ Reporte ISO 9001
✅ No conformidad detectada
✅ Recomendaciones de mantenimiento
# Enjambre monitorea un campo
- Drones: Detectan plagas en cultivos
- Terrestres: Miden humedad de suelo
- Sistema: Genera informe de estado del campo
# Robot crawler inspecciona ductos internos
- Detecta corrosión
- Mide espesores
- Genera documentación para auditoría ISO

© 2026 Fernando Obelar. Todos los derechos reservados.
Licencia GPL-3.0: Debe mencionar al autor original.
