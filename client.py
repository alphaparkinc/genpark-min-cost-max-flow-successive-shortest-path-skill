"""Min-Cost Max-Flow (MCMF) Successive Shortest Path Engine.
100% Python Standard Library.
"""

import collections

class MinCostMaxFlow:
    """Successive Shortest Path algorithm for Min-Cost Max-Flow with SPFA."""
    class Edge:
        def __init__(self, u, v, cap, cost):
            self.u = u
            self.v = v
            self.cap = cap
            self.flow = 0
            self.cost = cost
            self.rev = None

    def __init__(self, num_nodes):
        self.n = num_nodes
        self.adj = [[] for _ in range(num_nodes)]

    def add_edge(self, u, v, cap, cost):
        e1 = self.Edge(u, v, cap, cost)
        e2 = self.Edge(v, u, 0, -cost)
        e1.rev = e2
        e2.rev = e1
        self.adj[u].append(e1)
        self.adj[v].append(e2)

    def compute_mcmf(self, s, t):
        tot_flow = 0
        tot_cost = 0

        while True:
            dist = [float("inf")] * self.n
            parent = [None] * self.n
            in_queue = [False] * self.n

            dist[s] = 0
            queue = collections.deque([s])
            in_queue[s] = True

            while queue:
                u = queue.popleft()
                in_queue[u] = False
                for edge in self.adj[u]:
                    if edge.cap - edge.flow > 0 and dist[edge.v] > dist[u] + edge.cost:
                        dist[edge.v] = dist[u] + edge.cost
                        parent[edge.v] = edge
                        if not in_queue[edge.v]:
                            queue.append(edge.v)
                            in_queue[edge.v] = True

            if dist[t] == float("inf"):
                break

            push = float("inf")
            curr = t
            while curr != s:
                edge = parent[curr]
                push = min(push, edge.cap - edge.flow)
                curr = edge.u

            curr = t
            while curr != s:
                edge = parent[curr]
                edge.flow += push
                edge.rev.flow -= push
                tot_cost += push * edge.cost
                curr = edge.u

            tot_flow += push

        return tot_flow, tot_cost
