import os
from openai import OpenAI

alert_file = "monitor/reports/alerts.txt"

def get_latest_alert(file_path):
    """
    Read the latest alert from the alerts file.
    Return the last non-empty line, or None if no alerts exist.
    """
    with open(file_path, "r") as file:
        lines = [line.strip() for line in file.readlines() if line.strip()]

    if not lines:
        print("No alerts found.")
        return None

    return lines[-1]


def analyze_alert_with_ai(alert_text):
    """
    Send the latest alert to OpenAI and return the AI response.
    """
    api_key = os.getenv("OPENAI_API_KEY")

    if not api_key:
        print("Open api key is not set.")
        return None

    client = OpenAI(api_key=api_key)

    prompt = f"""
Analyze this incident alert:

{alert_text}

Give your answer in this format:
1. What happened and what casue the issue
2. What is the suggested fix 
3. What is the quick fix for now

Keep the answer short, clear, and practical.
"""

    try:
        response = client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=[
                {"role": "system", "content": "You are a SRE incident triage assistant."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.2
        )

        return response.choices[0].message.content

    except Exception as e:
        print(f"OpenAI API Error: {e}")
        return None


def main():
    latest_alert = get_latest_alert(alert_file)

    if not latest_alert:
        return

    print("\nAI INCIDENT TRIAGE \n")
    print(f"ALERT:   {latest_alert}\n")

    ai_result = analyze_alert_with_ai(latest_alert)

    if ai_result:
        print("AI ANALYSIS:")
        print(ai_result, "\n")


if __name__ == "__main__":
    main()
