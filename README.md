# ai-security-log-analyzer
AI-powered Python application for detecting suspicious security events from system logs


# AI Security Log Analyzer

A Python application that analyzes system log files using OpenAI to identify suspicious behavior and summarize potential cybersecurity threats.

## Features

- Detects failed login attempts
- Flags suspicious login times
- Identifies unknown IP addresses
- Uses AI to explain why activity is suspicious
- Generates easy-to-read threat summaries

## Technologies

- Python
- OpenAI API
- VS Code

## Example

Input:

User login from IP 45.33.32.1 at 3:12 AM

Output:

Possible brute force attack detected.

The login occurred outside normal business hours and follows multiple failed login attempts.

## Installation

```bash
pip install -r requirements.txt
```

Run

```bash
python log_analyzer.py
```

## Future Improvements

- Streamlit dashboard
- PDF reports
- VirusTotal integration
- Risk scoring
