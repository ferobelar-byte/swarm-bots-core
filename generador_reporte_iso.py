from docx import Document
from datetime import datetime

# Crear un nuevo documento Word
doc = Document()

# Título del reporte
doc.add_heading('REPORTE DE INSPECCIÓN ISO 9001', 0)

# Información básica
doc.add_paragraph(f'Fecha: {datetime.now().strftime("%d/%m/%Y %H:%M")}')
doc.add_paragraph('Proyecto: Swarm Bots')
doc.add_paragraph('Tipo: Inspección de Infraestructura')

# Sección de hallazgos
doc.add_heading('Hallazgos de la Inspección', level=1)

# Simular datos de un robot
datos_robot = {
    "robot_id": "DRONE-001",
    "ubicacion": "Torre A - Nivel 3",
    "temperatura": 45.5,
    "estado": "ALERTA"
}

doc.add_paragraph(f'Robot ID: {datos_robot["robot_id"]}')
doc.add_paragraph(f'Ubicación: {datos_robot["ubicacion"]}')
doc.add_paragraph(f'Temperatura detectada: {datos_robot["temperatura"]}°C')
doc.add_paragraph(f'Estado: {datos_robot["estado"]}')

# Sección de no conformidades
doc.add_heading('No Conformidades', level=1)

if datos_robot["temperatura"] > 40:
    doc.add_paragraph('⚠️ NO CONFORMIDAD: Temperatura excede el límite permitido (40°C)', style='Intense Quote')
    doc.add_paragraph('Acción correctiva: Verificar sistema de refrigeración')
else:
    doc.add_paragraph('✅ Sin no conformidades detectadas')

# Sección de recomendaciones
doc.add_heading('Recomendaciones', level=1)
doc.add_paragraph('1. Programar mantenimiento preventivo en 30 días')
doc.add_paragraph('2. Instalar sensores adicionales en la zona')
doc.add_paragraph('3. Documentar en el registro de mantenimiento ISO 9001')

# Guardar el documento
nombre_archivo = 'reporte_iso_001.docx'
doc.save(nombre_archivo)

print(f'✅ Reporte generado exitosamente: {nombre_archivo}')
print(f'📄 Ubicado en: {datos_robot["ubicacion"]}')
print(f'🤖 Robot: {datos_robot["robot_id"]}')
print(f'⚠️ No conformidades: 1 (Temperatura)')