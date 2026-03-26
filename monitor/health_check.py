import time
def checker():
    log_file = "./monitor/reports/alerts.txt"

    while True:
        with open(log_file, "r") as logs:
            line = logs.readlines()
            
            if len(line) == 0:
                print("HEALTHY: NO ALERT FOUND")
            else:
                print(f"UNHEALTHY: {len(line)} ERRORS FOUND.")
        time.sleep(5)

if __name__ == "__main__":
    checker()
    