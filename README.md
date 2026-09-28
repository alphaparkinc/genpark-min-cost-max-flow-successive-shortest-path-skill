# Min-Cost Max-Flow (MCMF) Skill

High-efficiency, zero-dependency Python implementation of **Minimum-Cost Maximum-Flow (MCMF)** via Successive Shortest Paths and Shortest Path Faster Algorithm (SPFA).

## Features
- **Successive Augmentation**: Repeatedly routes flow along least-cost paths in residual network graphs.
- **Negative Cycle Resilience**: Maintains conservative potential invariants avoiding infinite cycling.
- **Zero External Dependencies**: Pure Python standard library.
- **Native MCP Protocol**: JSON-RPC 2.0 stdio server compatible with Claude Desktop, Cursor, and Windsurf.

## Architecture
```mermaid
graph TD
    Residual["Residual Graph (Capacities & Costs)"] --> SPFA["SPFA: Shortest Cost Augmenting Path"]
    SPFA -- Path Found --> Augment["Augment Bottleneck Flow & Update Potentials"]
    Augment --> Residual
    SPFA -- No Path Exists --> Termination["Optimal Min-Cost Max-Flow Achieved"]
```
