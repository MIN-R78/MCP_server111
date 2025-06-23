###
from typing import Dict, Any, List
from stdio_server import stdio_server

class SimpleAdder:
    name: str = "simple_adder"

    inputSchema: Dict[str, Any] = {
        "type": "object",
        "properties": {
            "x": {"type": "integer"},
            "y": {"type": "integer"}
        },
        "required": ["x", "y"]
    }

    functions: List[str] = ["add"]

    def add(self, x: int, y: int) -> int:
        print(f"[DEBUG] add called with x={x}, y={y}")
        return x + y

if __name__ == "__main__":
    print("Starting MCP server...")
    print("Calling stdio_server...")
    stdio_server(SimpleAdder)

