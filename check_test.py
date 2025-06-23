###
import subprocess
import json
import os

input_data = {
    "tool": "simple_adder",
    "function": "add",
    "inputs": {"x": 5, "y": 7}
}

current_dir = os.path.dirname(os.path.abspath(__file__))
env = os.environ.copy()
env["PYTHONPATH"] = current_dir + os.pathsep + env.get("PYTHONPATH", "")

proc = subprocess.Popen(
    ["python", "mcp_server.py"],
    stdin=subprocess.PIPE,
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
    text=True,
    encoding="utf-8",
    cwd=current_dir,
    env=env
)

stdout, stderr = proc.communicate(json.dumps(input_data) + "\n")

print("------ STDOUT ------")
print(stdout)
print("------ STDERR ------")
print(stderr)
