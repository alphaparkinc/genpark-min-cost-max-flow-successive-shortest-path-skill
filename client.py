"""
Autonomous Agent Min-Cost Max-Flow (MCMF) Solver Skill
Pure Python Standard Library implementation using Successive Shortest Path & SPFA.
"""
from typing import List, Dict, Any

class MinCostMaxFlow:
    """
    Min-Cost Max-Flow Solver using Successive Shortest Path with SPFA.
    """
    def __init__(self, num_nodes: int):
        self.n = num_nodes
        self.adj = [[] for _ in range(num_nodes)]
        self.edges = []

    def add_edge(self, u: int, v: int, cap: float, cost: float):
        idx1 = len(self.edges)
        idx2 = idx1 + 1
        e1 = {"from": u, "to": v, "cap": float(cap), "flow": 0.0, "cost": float(cost), "rev": idx2}
        e2 = {"from": v, "to": u, "cap": 0.0, "flow": 0.0, "cost": -float(cost), "rev": idx1}
        self.adj[u].append(idx1)
        self.edges.append(e1)
        self.adj[v].append(idx2)
        self.edges.append(e2)

    def solve(self, source: int, sink: int) -> Dict[str, Any]:
        max_flow = 0.0
        min_cost = 0.0

        while True:
            dist = [float("inf")] * self.n
            parent_edge = [-1] * self.n
            in_queue = [False] * self.n
            queue = [source]
            dist[source] = 0.0
            in_queue[source] = True

            head = 0
            while head < len(queue):
                u = queue[head]
                head += 1
                in_queue[u] = False

                for e_idx in self.adj[u]:
                    e = self.edges[e_idx]
                    if e["cap"] - e["flow"] > 1e-9 and dist[e["to"]] > dist[u] + e["cost"] + 1e-9:
                        dist[e["to"]] = dist[u] + e["cost"]
                        parent_edge[e["to"]] = e_idx
                        if not in_queue[e["to"]]:
                            queue.append(e["to"])
                            in_queue[e["to"]]: True

            if dist[sink] == float("inf"):
                break

            bottleneck = float("inf")
            curr = sink
            while curr != source:
                e_idx = parent_edge[curr]
                e = self.edges[e_idx]
                bottleneck = min(bottleneck, e["cap"] - e["flow"])
                curr = e["from"]

            curr = sink
            while curr != source:
                e_idx = parent_edge[curr]
                self.edges[e_idx]["flow"] += bottleneck
                rev_idx = self.edges[e_idx]["rev"]
                self.edges[rev_idx]["flow"] -= bottleneck
                min_cost += bottleneck * self.edges[e_idx]["cost"]
                curr = self.edges[e_idx]["from"]

            max_flow += bottleneck

        flow_details = []
        for i in range(0, len(self.edges), 2):
            e = self.edges[i]
            if e["flow"] > 1e-9:
                flow_details.append({
                    "from": e["from"],
                    "to": e["to"],
                    "flow": round(e["flow"], 4),
                    "capacity": e["cap"],
                    "cost_per_unit": e["cost"]
                })

        return {
            "max_flow": round(max_flow, 4),
            "min_cost": round(min_cost, 4),
            "flow_paths": flow_details
        }
