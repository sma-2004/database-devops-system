import psutil
import time

def check_system():
    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory().percent

    print(f"CPU Usage: {cpu}%")
    print(f"Memory Usage: {memory}%")

    if cpu > 80 or memory > 80:
        print("⚠️ ALERT: High resource usage!")

if __name__ == "__main__":
    while True:
        check_system()
        time.sleep(10)