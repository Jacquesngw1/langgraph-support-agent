from typing import TypedDict, Annotated
import operator

from agent.tools import check_order_status, generate_return_label


class AgentState(TypedDict):
    messages: Annotated[list, operator.add]
    intent: str
    response: str


def route_intent(state: AgentState) -> dict:
    """Classify user intent using keyword heuristics (no LLM needed)."""
    msg = state["messages"][-1].lower()
    if "status" in msg or "check" in msg or "order" in msg:
        return {"intent": "status_check"}
    if "return" in msg or "refund" in msg:
        return {"intent": "return"}
    return {"intent": "other"}


def tool_router(state: AgentState) -> str:
    if state["intent"] == "status_check":
        return "check_status"
    if state["intent"] == "return":
        return "generate_return"
    return "fallback"


def check_status_node(state: AgentState) -> dict:
    last = state["messages"][-1]
    order_id = last.split()[-1]
    result = check_order_status.invoke({"order_id": order_id})
    return {"response": result}


def generate_return_node(state: AgentState) -> dict:
    last = state["messages"][-1]
    order_id = last.split()[-1]
    result = generate_return_label.invoke({"order_id": order_id})
    return {"response": result}


def fallback_node(state: AgentState) -> dict:
    return {
        "response": "I didn't understand. Please rephrase or say 'status <ID>' or 'return <ID>'."
    }
