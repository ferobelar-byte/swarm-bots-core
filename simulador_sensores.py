import random
import datetime
import json

def simular_lectura_sensor(tipo_robot, ubicacion):
    """Simula datos de un sensor de robot"""
    
    sensores = ["temperatura", "vibracion", "presion", "humedad"]
    sensor_elegido = random.choice(sensores)
    
    # Valores aleatorios según el sensor
    if sensor_elegido == "temperatura":
        valor = round(random.uniform(25, 65), 2)
        unidad = "°C"
        limite = 40
    elif sensor_elegido == "vibracion":
        valor = round(random.uniform(0, 10), 2)
        unidad = "mm/s"
        limite = 5
    elif sensor_elegido == "presion":
        valor = round(random.uniform(80, 120), 2)
        unidad = "PSI"
        limite = 100
    else:  # humedad
        valor = round(random.uniform(30, 90), 2)
        unidad = "%"
        limite = 70
    
    # Determinar estado
    estado = "NORMAL" if valor <= limite else "ALERTA"
    
    # Crear diccionario con los datos
    lectura = {
        "timestamp": datetime.datetime.now().isoformat(),
        "robot_id": f"{tipo_robot}_{random.randint(100, 999)}",
        "ubicacion": ubicacion,
        "sensor": sensor_elegido,
        "valor": valor,
        "unidad": unidad,
        "limite": limite,
        "estado": estado
    }
    
    return lectura

# Generar 5 lecturas de ejemplo
print("=== SIMULADOR DE SENSORES SWARM BOTS ===")
print("")

lecturas = []
for i in range(5):
    tipos = ["DRONE", "CRAWLER", "AQUABOT"]
    ubicaciones = ["Torre A", "Depósito B", "Tanque C", "Ducto D", "Campo E"]
    
    lectura = simular_lectura_sensor(random.choice(tipos), random.choice(ubicaciones))
    lecturas.append(lectura)
    
    print(f"Lectura {i+1}:")
    print(f"  Robot: {lectura['robot_id']}")
    print(f"  Sensor: {lectura['sensor']} = {lectura['valor']} {lectura['unidad']}")
    print(f"  Estado: {lectura['estado']}")
    print("")

# Guardar en JSON para usar después
with open('datos_sensores.json', 'w', encoding='utf-8') as f:
    json.dump(lecturas, f, indent=2, ensure_ascii=False)

print("✅ Datos guardados en: datos_sensores.json")
print(f"📊 Total de lecturas: {len(lecturas)}")
alertas = sum(1 for l in lecturas if l['estado'] == "ALERTA")
print(f"⚠️ Alertas detectadas: {alertas}")