import psutil
import time
import logging

logging.basicConfig(
    filename="system_health.log",
    level=logging.INFO,
    format='%(asctime)s - %(message)s'
)

console_handler=logging.StreamHandler()
console_handler.setLevel(logging.INFO)

logging.getLogger().addHandler(console_handler)

CPU_THRESHOLD = 80
MEMORY_THRESHOLD = 80

print("Monitoring started...logs are being saved to system_health.log")

try:
    while True:
        cpu_usage = psutil.cpu_percent(interval=1)
        memory_usage = psutil.virtual_memory().percent
        
        logging.info(f"CPU: {cpu_usage}% | Memory: {memory_usage}%")
        
        if cpu_usage > CPU_THRESHOLD or memory_usage > MEMORY_THRESHOLD:
            print("ALERT: High system usage detected!")
            
    
except KeyboardInterrupt:
    print("\nStopping")
except Exception as e:
    print(f"An error occurred: {e}")