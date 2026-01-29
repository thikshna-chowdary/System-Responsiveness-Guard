import psutil
import time

CPU_THRESHOLD = 50

print("System Responsiveness Guard Started")

while True:
    for proc in psutil.process_iter(['pid', 'name', 'cpu_percent']):
        try:
            pid = proc.info['pid']
            name = proc.info['name']
            cpu = proc.info['cpu_percent']

            if cpu > CPU_THRESHOLD:
                print(f"\n⚠ Heavy process detected: {name} (PID {pid}) CPU={cpu}%")
                print("✅ Alert: System responsiveness may degrade")

        except (psutil.NoSuchProcess, psutil.AccessDenied):
            pass

    time.sleep(3)
