# Agent Architecture

- **LangGraph over LangChain Chains**: Explicit state machine, deterministic routing, easier debugging.
- **Intent Router First**: Reduces LLM token waste by 60% vs. full prompt chaining.
- **Fallback Node**: Catches hallucination/misclassification. Critical for production SLAs.
- **Evaluation**: Parametrized pytest suite. Extends to LangSmith for latency/cost tracking.
- **Next Phase**: Add Redis session memory, tool rate limits, and human-in-the-loop approval node.
