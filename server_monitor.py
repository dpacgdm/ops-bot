import psutil
import time
from datetime import datetime

CPU_THRESHOLD = 80
MEMORY_THRESHOLD = 80

print("Starting system monitor...(Press Ctrl+C to stop)")

try:
    while True:
        cpu_usage = psutil.cpu_percent(interval=1)
        memory_usage = psutil.virtual_memory().percent
        
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        print(f"CPU Usage: {cpu_usage}%")
        print(f"Memory Usage: {memory_usage}%")
        
        if cpu_usage > CPU_THRESHOLD or memory_usage > MEMORY_THRESHOLD:
            print("ALERT: High system usage detected!")
            
    
except KeyboardInterrupt:
    print("\nSystem monitor stopped.")
except Exception as e:
    print(f"An error occurred: {e}")