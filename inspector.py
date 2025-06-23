###
import subprocess
import json
import os
import streamlit as st

st.title("MCP Inspector")

### Input fields
tool = st.text_input("Tool name", "simple_adder")
func = st.text_input("Function name", "add")
x = st.number_input("x", value=5)
y = st.number_input("y", value=7)

if st.button("Run Tool"):
    request = {
        "tool": tool,
        "function": func,
        "inputs": {"x": x, "y": y}
    }

    st.subheader("Request")
    st.json(request)

    cwd = os.getcwd()
    env = os.environ.copy()
    env["PYTHONPATH"] = cwd + os.pathsep + env.get("PYTHONPATH", "")

    ### Launch subprocess for MCP server
    proc = subprocess.Popen(
        ["python", "mcp_server.py"],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        cwd=cwd,
        env=env
    )

    stdout, stderr = proc.communicate(json.dumps(request) + "\n")

    st.subheader("Output")
    try:
        st.json(json.loads(stdout))
    except:
        st.code(stdout)

    if stderr.strip():
        st.subheader("Error")
        st.code(stderr)
