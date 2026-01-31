import mysql.connector
import random
import time

# ================================
# DATABASE CONNECTION
# ================================
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Ganesh@123"   # change to your MySQL password
)

cursor = db.cursor()

# ================================
# SQL SETUP (DATABASE + TABLES)
# ================================

cursor.execute("CREATE DATABASE IF NOT EXISTS VehicleFireSafety")
cursor.execute("USE VehicleFireSafety")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Vehicle (
    vehicle_id INT PRIMARY KEY,
    vehicle_type VARCHAR(20),
    registration_no VARCHAR(20)
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS SensorData (
    data_id INT AUTO_INCREMENT PRIMARY KEY,
    vehicle_id INT,
    temperature FLOAT,
    gas_level FLOAT,
    smoke_level FLOAT,
    recorded_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS AlertLog (
    alert_id INT AUTO_INCREMENT PRIMARY KEY,
    vehicle_id INT,
    alert_message VARCHAR(200),
    alert_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
""")

# Insert vehicle if not exists
cursor.execute("""
INSERT IGNORE INTO Vehicle VALUES (1, 'Bus', 'AP-21-K-3456')
""")

db.commit()

# ================================
# SAFETY THRESHOLDS
# ================================
MAX_TEMP = 70     # Celsius
MAX_GAS = 300     # ppm
MAX_SMOKE = 200   # units
VEHICLE_ID = 1

# ================================
# FUNCTIONS
# ================================
def log_sensor_data(temp, gas, smoke):
    cursor.execute("""
    INSERT INTO SensorData(vehicle_id, temperature, gas_level, smoke_level)
    VALUES (%s, %s, %s, %s)
    """, (VEHICLE_ID, temp, gas, smoke))
    db.commit()

def raise_alert(message):
    cursor.execute("""
    INSERT INTO AlertLog(vehicle_id, alert_message)
    VALUES (%s, %s)
    """, (VEHICLE_ID, message))
    db.commit()
    print("🔥 ALERT:", message)

def check_fire_risk(temp, gas, smoke):
    if temp > MAX_TEMP:
        raise_alert("High temperature detected – Fire risk")

    if gas > MAX_GAS:
        raise_alert("Gas leakage detected – Fire risk")

    if smoke > MAX_SMOKE:
        raise_alert("Smoke detected – Possible fire")

# ================================
# MAIN MONITORING LOOP
# ================================
print("🚍 Vehicle Fire Accident Prevention System Started")
print("Monitoring sensors...\n")

while True:
    temperature = random.randint(40, 100)
    gas = random.randint(100, 500)
    smoke = random.randint(50, 300)

    print(f"Temp: {temperature}°C | Gas: {gas} | Smoke: {smoke}")

    log_sensor_data(temperature, gas, smoke)
    check_fire_risk(temperature, gas, smoke)

    time.sleep(5)
