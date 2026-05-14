## Implementation approach

We will implement the Floyd-Warshall algorithm to calculate the shortest paths between all pairs of nodes in a weighted graph represented by an adjacency matrix. The algorithm will iteratively update the distance matrix to find the shortest paths.

## File list

- solution.py

## Data structures and interfaces:

classDiagram
    class FloydWarshall {
        +floyd_warshall(graph: List[List[float]]) -> List[List[float]]
    }

## Program call flow:

sequenceDiagram
    participant F as FloydWarshall
    participant G as Graph
    F->>G: floyd_warshall(graph)
    G-->>F: return distance matrix