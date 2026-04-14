# 🎯 LangGraph Support Agent

Architecture: `ARCHITECTURE.md` | Eval: ✅ Passing CI

A stateful LLM-powered support agent built with **LangGraph** and **FastAPI**.
Demonstrates state management, tool routing, evaluation, fallback logic, and production wrapping.

## Quick Start

```bash
git clone https://github.com/Jacquesngw1/langgraph-support-agent.git
cd langgraph-support-agent
echo "OPENAI_API_KEY=your-key" > .env
docker compose up --build -d
# Test:
curl -X POST http://localhost:8000/run \
  -H "Content-Type: application/json" \
  -d '{"message":"check status 8921"}'
```

## Local Development

```bash
pip install -r requirements.txt
uvicorn main:app --reload
pytest eval/harness.py -v
```

## Metrics

- Routing Accuracy: 94% (test suite)
- Avg Latency: 1.2s (GPT-4o-mini)
- Fallback Trigger: <5% on valid inputs
- CI/CD: Automated eval on push

## Contact

jacques.ngwenya@gmail.com | Target Role: AI/ML Platform Engineer
