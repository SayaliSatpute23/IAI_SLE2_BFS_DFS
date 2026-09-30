# IAI SLE-2 – BFS and DFS

## Aim
To implement and compare BFS and DFS for searching a small graph.

## Problem Statement
Search for the goal node J starting from node A using BFS and DFS.

## Algorithms Used

### BFS
BFS (Breadth First Search) explores nodes level by level.
It uses a queue.

### DFS
DFS (Depth First Search) explores one path deeply before backtracking.
It uses a stack.

## Graph
The same graph is used for both BFS and DFS.

Start node: A  
Goal node: J

## Performance Measurement
Python's `timeit` module is used to measure execution time.

The algorithms are executed 10,000 times for each test.

## Profiling
`py-spy` is used for performance profiling.

Flame graphs are generated for both BFS and DFS.

Files:
- `profiling/bfs_profile.svg`
- `profiling/dfs_profile.svg`

## Results

BFS:
- Average time: 24.67 ms
- Nodes expanded: 10

DFS:
- Average time: 17.46 ms
- Nodes expanded: 9

## Conclusion
For the selected graph, DFS took less average time and expanded fewer nodes than BFS.

The result can change depending on the graph structure and goal-node location.

## Tools Used
- Python
- timeit
- py-spy
- Flame Graph
- GitHub