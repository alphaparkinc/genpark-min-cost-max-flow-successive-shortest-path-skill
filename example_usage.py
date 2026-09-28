from client import MinCostMaxFlow

mcmf = MinCostMaxFlow(4)
mcmf.add_edge(0, 1, 10, 2)
mcmf.add_edge(0, 2, 5, 1)
mcmf.add_edge(1, 3, 5, 3)
mcmf.add_edge(2, 3, 5, 2)

flow, cost = mcmf.compute_mcmf(0, 3)
print(f"Optimal Min-Cost Max-Flow: Total Flow={flow}, Total Cost={cost}")
