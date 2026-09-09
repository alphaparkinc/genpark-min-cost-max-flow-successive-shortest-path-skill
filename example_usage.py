"""Example usage for Min-Cost Max-Flow Solver Skill."""
from client import MinCostMaxFlow

def main():
    print("Executing Min-Cost Max-Flow Solver...")
    mcmf = MinCostMaxFlow(4)
    mcmf.add_edge(0, 1, 3.0, 1.0)
    mcmf.add_edge(0, 2, 2.0, 2.0)
    mcmf.add_edge(1, 3, 2.0, 2.0)
    mcmf.add_edge(1, 2, 1.0, 1.0)
    mcmf.add_edge(2, 3, 3.0, 3.0)

    res = mcmf.solve(source=0, sink=3)
    print("Result:", res)
    assert res["max_flow"] == 5.0, f"Expected 5.0 max flow, got {res['max_flow']}"
    assert res["min_cost"] == 21.0, f"Expected 21.0 min cost, got {res['min_cost']}"
    print("Min-Cost Max-Flow Solver verified successfully!")

if __name__ == "__main__":
    main()
