"""MCP Server for Min-Cost Max-Flow Solver Skill."""
import json
import sys
from client import MinCostMaxFlow

def main():
    for line in sys.stdin:
        if not line.strip():
            continue
        try:
            req = json.loads(line)
            req_id = req.get("id")
            method = req.get("method")
            params = req.get("params", {})

            if method == "tools/list":
                res = {
                    "jsonrpc": "2.0",
                    "id": req_id,
                    "result": {
                        "tools": [{
                            "name": "solve_mcmf",
                            "description": "Solve Min-Cost Max-Flow problem on a directed graph",
                            "inputSchema": {
                                "type": "object",
                                "properties": {
                                    "num_nodes": {"type": "integer"},
                                    "edges": {
                                        "type": "array",
                                        "items": {
                                            "type": "object",
                                            "properties": {
                                                "u": {"type": "integer"},
                                                "v": {"type": "integer"},
                                                "capacity": {"type": "number"},
                                                "cost": {"type": "number"}
                                            },
                                            "required": ["u", "v", "capacity", "cost"]
                                        }
                                    },
                                    "source": {"type": "integer"},
                                    "sink": {"type": "integer"}
                                },
                                "required": ["num_nodes", "edges", "source", "sink"]
                            }
                        }]
                    }
                }
            elif method == "tools/call":
                args = params.get("arguments", {})
                solver = MinCostMaxFlow(args["num_nodes"])
                for edge in args["edges"]:
                    solver.add_edge(edge["u"], edge["v"], edge["capacity"], edge["cost"])
                output = solver.solve(args["source"], args["sink"])
                res = {
                    "jsonrpc": "2.0",
                    "id": req_id,
                    "result": {"content": [{"type": "text", "text": json.dumps(output)}]}
                }
            else:
                res = {"jsonrpc": "2.0", "id": req_id, "error": {"code": -32601, "message": "Method not found"}}
            print(json.dumps(res), flush=True)
        except Exception as e:
            err = {"jsonrpc": "2.0", "id": None, "error": {"code": -32000, "message": str(e)}}
            print(json.dumps(err), flush=True)

if __name__ == "__main__":
    main()
