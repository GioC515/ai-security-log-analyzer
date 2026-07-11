import os
from openai import OpenAI

# Set your API key as an environment variable before running
# export OPENAI_API_KEY="your_key_here"

client = OpenAI()

def read_logs(file_path):
    with open(file_path, "r") as file:
        return file.read()

def analyze_logs(log_data):
    prompt = f"""
    You are a cybersecurity analyst. Analyze the following logs and identify any suspicious activity.
    Highlight anomalies, potential threats, and explain why they are concerning.

    Logs:
    {log_data}
    """

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role": "system", "content": "You are a cybersecurity expert."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.3
    )

    return response.choices[0].message.content

def main():
    logs = read_logs("sample_logs.txt")
    result = analyze_logs(logs)

    print("\n🔍 AI Security Analysis:\n")
    print(result)

if __name__ == "__main__":
    main()
