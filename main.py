from fastapi import FastAPI
from pydantic import BaseModel
from agent.graph import build_graph

app = FastAPI(title="Support Agent API")
graph = build_graph()


class Query(BaseModel):
    message: str


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/run")
def run_agent(q: Query):
    state = {"messages": [q.message], "intent": "", "response": ""}
    result = graph.invoke(state)
    return {"response": result["response"], "intent": result["intent"]}
