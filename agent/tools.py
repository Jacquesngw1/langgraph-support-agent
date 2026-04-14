from langchain_core.tools import tool


@tool
def check_order_status(order_id: str) -> str:
    """Mock: Returns order status based on a deterministic mapping."""
    status_map = {
        "8921": "pending",
        "1234": "shipped",
        "5678": "delivered",
    }
    return status_map.get(order_id, "pending")


@tool
def generate_return_label(order_id: str) -> str:
    """Mock: Generates return link."""
    return f"https://returns.example.com/{order_id}"
