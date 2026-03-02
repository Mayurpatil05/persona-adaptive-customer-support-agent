from fastapi import FastAPI
from pydantic import BaseModel

from app.persona import detect_persona
from app.retriever import retrieve_context
from app.generator import generate_response
from app.escalation import should_escalate

app = FastAPI()

class QueryRequest(BaseModel):
    message: str

@app.post("/support")
def support_agent(request: QueryRequest):

    query = request.message

    persona = detect_persona(query)
    context = retrieve_context(query)

    if should_escalate(query):
        return {
            "escalated": True,
            "persona": persona,
            "summary": f"Escalation required. Persona: {persona}. Query: {query}",
            "context": context
        }

    response = generate_response(persona, context, query)

    return {
    "escalated":False,
    "persona": persona,
    "response": response
}