# IAI SLE-2: BFS vs DFS Profiling

## Course
02AML204 - Introduction to Artificial Intelligence

## Objective
Compare Breadth-First Search (BFS) and Depth-First Search (DFS) on the same graph using:
1. Execution time
2. Number of nodes expanded
3. `timeit` repeated execution
4. `py-spy` flame-graph profiling

## Graph
Start node: A  
Goal node: J

The graph is defined directly in `bfs_dfs.py`.

## Run the comparison

```bash
python bfs_dfs.py
```

The program performs 3 timing tests, with 10,000 executions in each test, and prints the average batch time.

## Generate flame graphs

Install `py-spy`:

```bash
python -m pip install py-spy
```

BFS:

```bash
py -m py_spy record --format flamegraph --output profiling\bfs_profile.svg -- python profiling\pyspy_target.py bfs
```

DFS:

```bash
py -m py_spy record --format flamegraph --output profiling\dfs_profile.svg -- python profiling\pyspy_target.py dfs
```

The generated files are:

- `profiling/bfs_profile.svg`
- `profiling/dfs_profile.svg`

Open the SVG files in a browser to view the flame graphs.

## Important
Execution times depend on the computer, Python version, operating system, and background processes. Therefore, do not copy a friend's timing values. Use the values printed by your own run.

The flame graph is profiling evidence: it shows where the Python program spends sampled execution time while BFS or DFS is running.

## Simple viva explanation

**BFS:** searches level by level and uses a queue.

**DFS:** goes deep along a path and backtracks, using a stack/recursion.

**Empirical profiling:** running an algorithm and measuring its actual performance.

**timeit:** Python module used to measure execution time.

**py-spy:** a Python sampling profiler that can generate a flame graph.

**Flame graph:** a visual representation of where execution time is spent.

## Project structure

```text
IAI_SLE2_BFS_DFS/
├── bfs_dfs.py
├── profiling/
│   ├── pyspy_target.py
│   ├── bfs_profile.svg      # generated after running py-spy
│   └── dfs_profile.svg      # generated after running py-spy
├── requirements.txt
├── run_profiling.bat
└── README.md
```
