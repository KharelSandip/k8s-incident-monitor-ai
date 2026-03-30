import requests

alert_file = "monitor/reports/alerts.txt"


def get_latest_alert(file_path):
    """
    Read the latest alert from the alerts file.
    Return the last non-empty line, or None if no alerts exist.
    """
    try:
        with open(file_path, "r") as file:
            lines = [line.strip() for line in file.readlines() if line.strip()]

        return lines[-1]

    except FileNotFoundError:
        print("Alert file not found.")
        return None


def analyze_alert_with_ai(alert_text):
    url = "http://10.0.0.42:11434/api/generate"

    prompt = f"""
Analyze this incident alert:

{alert_text}

Give your answer in this format:
1. What happened and what caused the issue
2. What is the suggested fix
3. What is the quick fix for now

Keep it short and practical.
"""

    data = {
        "model": "llama3.2",
        "prompt": prompt,
        "stream": False
    }

    try:
        res = requests.post(url, json=data, timeout=20)
        res.raise_for_status()
        result = res.json()
        return result.get("response", "No response from model")

    except requests.exceptions.RequestException as e:
        print(f"Ollama Connection Error: {e}")
        return None


def main():
    latest_alert = get_latest_alert(alert_file)

    if not latest_alert:
        return

    print("\nAI INCIDENT TRIAGE\n")
    print(f"ALERT: {latest_alert}\n")

    ai_result = analyze_alert_with_ai(latest_alert)

    if ai_result:
        print("AI ANALYSIS:")
        print(ai_result)
    else:
        print("No AI analysis returned.")


if __name__ == "__main__":
    main()