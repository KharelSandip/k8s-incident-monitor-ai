import subprocess
from datetime import datetime

log_file = "./monitor/reports/alerts.txt"
pod_label = "app=incident-monitor-container"
keywords = ["ERROR", "CRITICAL"]


def monitor_logs():
    command = ["kubectl", "logs", "-f", "-l", pod_label]

    process = subprocess.Popen(
        command,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
     )

    for line in process.stdout:
        line = line.strip()

        if not line:
            continue

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        if any(keyword in line for keyword in keywords):
            with open(log_file, "a") as log:
                log.write(f"{timestamp} ALERT: {line}\n")
                print(f"{timestamp} ALERT: {line}\n")
        else:
            print(f"{timestamp} LOG: {line}")


if __name__ == "__main__":
    monitor_logs()