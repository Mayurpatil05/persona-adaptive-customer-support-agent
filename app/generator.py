import requests

OLLAMA_URL = "http://localhost:11434/api/generate"

persona_prompts = {
    "Technical Expert": """
        Respond technically.
        Provide structured steps.
        Be precise.
    """,
    "Frustrated User": """
        Acknowledge frustration.
        Apologize politely.
        Keep language simple.
        Provide reassurance.
    """,
    "Business Executive": """
        Be concise.
        Focus on impact.
        Mention resolution timeline.
        Avoid technical jargon.
    """
}

def generate_response(persona, context, query):

    system_instruction = persona_prompts.get(persona, "")

    full_prompt = f"""
    {system_instruction}

    Knowledge Base:
    {context}

    Customer Query:
    {query}

    Provide a helpful response.
    """

    response = requests.post(OLLAMA_URL, json={
        "model": "llama3:latest",
        "prompt": full_prompt,
        "stream": False
    })

    return response.json()["response"]