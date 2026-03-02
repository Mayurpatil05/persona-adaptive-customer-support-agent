import requests

OLLAMA_URL = "http://localhost:11434/api/generate"

def detect_persona(query: str):

    prompt = f"""
    You are a customer persona classifier.

    Classify the customer into ONE category:

    1. Technical Expert (mentions API, logs, integration, errors)
    2. Frustrated User (angry tone, complaints, emotional)
    3. Business Executive (mentions SLA, ROI, revenue impact)

    Customer message:
    "{query}"

    Only return:
    Technical Expert
    OR
    Frustrated User
    OR
    Business Executive
    """

    response = requests.post(OLLAMA_URL, json={
        "model": "llama3:latest",
        "prompt": prompt,
        "stream": False
    })

    return response.json()["response"].strip()