###
import json
import sys

def stdio_server(tool_class):
    instance = tool_class()
    while True:
        try:
            line = sys.stdin.readline()
            if not line:
                break
            data = json.loads(line)
            if data.get("tool") != instance.name:
                continue
            func = data.get("function")
            if func not in getattr(instance, "functions", []):
                continue
            inputs = data.get("inputs", {})
            result = getattr(instance, func)(**inputs)
            print(json.dumps({"output": result}))
        except Exception as e:
            print(json.dumps({"error": str(e)}), file=sys.stderr)

