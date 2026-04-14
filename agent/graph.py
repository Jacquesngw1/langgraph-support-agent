from langgraph.graph import StateGraph, END

from agent.nodes import (
    AgentState,
    route_intent,
    tool_router,
    check_status_node,
    generate_return_node,
    fallback_node,
)


def build_graph():
    graph = StateGraph(AgentState)
    graph.add_node("route", route_intent)
    graph.add_node("check_status", check_status_node)
    graph.add_node("generate_return", generate_return_node)
    graph.add_node("fallback", fallback_node)

    graph.set_entry_point("route")
    graph.add_conditional_edges(
        "route",
        tool_router,
        {
            "check_status": "check_status",
            "generate_return": "generate_return",
            "fallback": "fallback",
        },
    )
    graph.add_edge("check_status", END)
    graph.add_edge("generate_return", END)
    graph.add_edge("fallback", END)
    return graph.compile()
