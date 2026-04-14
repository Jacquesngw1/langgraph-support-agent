import pytest
from agent.graph import build_graph

graph = build_graph()

TEST_CASES = [
    ("check status 8921", "pending"),
    ("return 4410", "https://returns.example.com/4410"),
    ("hello", "I didn't understand"),
]


@pytest.mark.parametrize("msg, expected_kw", TEST_CASES)
def test_agent_flow(msg, expected_kw):
    state = {"messages": [msg], "intent": "", "response": ""}
    res = graph.invoke(state)
    assert expected_kw.lower() in res["response"].lower()
