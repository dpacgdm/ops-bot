import psutil
import time
import logging
from prometheus_client import start_http_server, Gauge

# 1. Configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

# 2. Define Prometheus Metrics
# 'system_cpu_usage' is the name of the metric in Prometheus
CPU_GAUGE = Gauge('system_cpu_usage', 'Current CPU usage percentage')
MEMORY_GAUGE = Gauge('system_memory_usage', 'Current Memory usage percentage')

def monitor_system():
    # 3. Start the metrics server on port 8000
    # Prometheus will look at http://localhost:8000/metrics to get the data
    print("Starting Prometheus Metrics Server on port 8000...")
    start_http_server(8000)

    print("Monitoring started...")
    
    try:
        while True:
            cpu_usage = psutil.cpu_percent(interval=1)
            memory_usage = psutil.virtual_memory().percent

            # 4. Update the Prometheus Gauges with the new numbers
            CPU_GAUGE.set(cpu_usage)
            MEMORY_GAUGE.set(memory_usage)

            # Log to console just for verify
            logging.info(f"Updated Metrics -> CPU: {cpu_usage}% | Memory: {memory_usage}%")
            
            # Note: We don't need sleep here because cpu_percent(interval=1) blocks for 1s
            
    except KeyboardInterrupt:
        print("\nStopping...")

if __name__ == "__main__":
    monitor_system()