import time
import random
import os

OUTPUT_DIR = "/tmp/temperatura_stream"
os.makedirs(OUTPUT_DIR, exist_ok=True)

sensores = ["sensor_01", "sensor_02", "sensor_03", "sensor_04", "sensor_05"]

batch = 0
while True:
    batch += 1
    filename = f"{OUTPUT_DIR}/batch_{batch:04d}.txt"
    
    lecturas = []
    for _ in range(random.randint(5, 10)):
        sensor = random.choice(sensores)
        temp = round(random.gauss(30, 8), 2)
        lecturas.append(f"{sensor},{temp}")
    
    with open(filename, "w") as f:
        f.write("\n".join(lecturas) + "\n")
    
    print(f"[generador] Batch {batch} escrito con {len(lecturas)} lecturas en {filename}")
    time.sleep(2)
