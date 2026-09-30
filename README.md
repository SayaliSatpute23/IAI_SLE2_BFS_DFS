```markdown
# SLE-2: BFS vs DFS Profiling

## Student Details

- **Course:** 02AML204 – Introduction to Artificial Intelligence
- **PRN:** 26UAM311
- **Name:** Sayali Madhukar Satpute
- **Division:** A
- **Experiment:** SLE-2 – Profiling Report

## Objective

The objective of this SLE-2 experiment is to perform empirical performance analysis of two uninformed search algorithms:

- Breadth-First Search (BFS)
- Depth-First Search (DFS)

Both algorithms were implemented and tested on the same graph to compare their practical performance in terms of execution time and nodes expanded.

## Problem Used

- **Problem:** Small graph search
- **Start Node:** A
- **Goal Node:** J

Both BFS and DFS search for the goal node J starting from node A using the same graph.

## Algorithms Used

### Breadth-First Search (BFS)

BFS explores the graph level by level. It uses a queue to store nodes that are yet to be explored.

BFS continues exploring nodes until the goal node is found or there are no more nodes to explore.

### Depth-First Search (DFS)

DFS explores a branch of the graph as deeply as possible before backtracking.

It uses a stack to store nodes that are yet to be explored.

DFS continues until the goal node is found or there are no more nodes to explore.

## Graph Used

The same graph was used for both BFS and DFS.

```text
        A
       / \
      B   C
     / \   \
    D   E   I
    |
    F
    |
    G
    |
    H
    |
    J
```

- **Start Node:** A
- **Goal Node:** J

Using the same graph makes the comparison between BFS and DFS consistent.

## Profiling Method

The following methods and tools were used:

- **Execution Time:** Python `timeit` module
- **Node Measurement:** Manual node counting
- **Profiler:** `py-spy`
- **Time Measurement Runs:** 10,000 runs
- **Number of Tests:** 3 tests
- **Flame Graph:** Generated using `py-spy`

The same graph, start node, and goal node were used for both algorithms.

## Results

| **Metric** | **BFS** | **DFS** |
|---|---:|---:|
| Average Time | 24.67 ms | 17.46 ms |
| Nodes Expanded | 10 | 9 |

## Observation

For the selected graph, DFS recorded a lower average execution time than BFS.

DFS also expanded fewer nodes than BFS for this particular graph.

- BFS expanded **10 nodes**.
- DFS expanded **9 nodes**.
- BFS average time was **24.67 ms**.
- DFS average time was **17.46 ms**.

The result is specific to the selected graph and the location of the goal node. Different graph structures or goal locations may produce different results.

## Time Measurement

Python's `timeit` module was used to measure the execution time of BFS and DFS.

Each algorithm was executed 10,000 times, and the average execution time was calculated from 3 tests.

This provides a practical comparison of the execution time of both algorithms.

## Node Measurement

The number of expanded nodes was measured manually during the search.

For the selected graph:

- BFS expanded 10 nodes.
- DFS expanded 9 nodes.

Node expansion gives an idea of how many nodes each algorithm visits before reaching the goal.

## py-spy Profiling

`py-spy` was used to profile the Python programs and generate flame graphs for BFS and DFS.

The flame graphs help visualize the functions that were active during program execution.

### BFS Flame Graph

The generated BFS profiling file is:

```text
profiling/bfs_profile.svg
```

### DFS Flame Graph

The generated DFS profiling file is:

```text
profiling/dfs_profile.svg
```

## Profiling Target

A separate profiling target was used to repeatedly execute BFS and DFS so that `py-spy` could collect enough samples for the flame graph.

The profiling target is:

```text
profiling/pyspy_target.py
```

## Project Structure

```text
IAI_SLE2_BFS_DFS/
│
├── bfs_dfs.py
│
├── profiling/
│   ├── bfs_profile.svg
│   ├── dfs_profile.svg
│   └── pyspy_target.py
│
├── run_profiling.bat
├── requirements.txt
├── README.md
└── .gitignore
```

## Tools Used

- Python
- `timeit`
- `py-spy`
- Flame Graph
- Git
- GitHub
- Visual Studio Code

## Conclusion

BFS and DFS were implemented and profiled on the same graph.

For the selected graph, DFS recorded a lower average execution time and expanded fewer nodes than BFS.

The profiling results are specific to this graph and search condition. The performance of BFS and DFS can change depending on the graph structure and the location of the goal node.
```