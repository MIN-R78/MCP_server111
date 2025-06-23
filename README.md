### MCP_server

This is a Multi-Component Protocol (MCP) Server implementation with a Streamlit-based inspection UI. The system allows testing basic tools via subprocess execution, simulating tool agent pipelines.

### Usage Instructions

```bash
### Step 1: Install dependencies
pip install streamlit

### Step 2: Launch the inspector interface
streamlit run inspector.py

### Step 3: In the web UI, enter:
#   Tool name:     simple_adder
#   Function name: add
#   Inputs:        x = 5, y = 7
# Click "Run Tool" to test the system.

### Example Output:
# {
#   "tool": "simple_adder",
#   "function": "add",
#   "inputs": { "x": 5, "y": 7 }
# }
# [DEBUG] add called with x=5, y=7
# {"output": 12}
