from collections import deque
from timeit import repeat

GRAPH = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["I"],
    "D": ["F"],
    "E": [],
    "F": ["G"],
    "G": ["H"],
    "H": ["J"],
    "I": [],
    "J": [],
}

START = "A"
GOAL = "J"


def bfs(graph, start, goal):
    queue = deque([start])
    visited = set()
    expanded = []

    while queue:
        node = queue.popleft()

        if node in visited:
            continue

        visited.add(node)
        expanded.append(node)

        if node == goal:
            return expanded

        for neighbour in graph[node]:
            if neighbour not in visited:
                queue.append(neighbour)

    return expanded


def dfs(graph, start, goal):
    stack = [start]
    visited = set()
    expanded = []

    while stack:
        node = stack.pop()

        if node in visited:
            continue

        visited.add(node)
        expanded.append(node)

        if node == goal:
            return expanded

        # Reverse so the first neighbour in GRAPH is explored first.
        for neighbour in reversed(graph[node]):
            if neighbour not in visited:
                stack.append(neighbour)

    return expanded


def main():
    bfs_result = bfs(GRAPH, START, GOAL)
    dfs_result = dfs(GRAPH, START, GOAL)

    bfs_times = repeat(lambda: bfs(GRAPH, START, GOAL), repeat=3, number=10000)
    dfs_times = repeat(lambda: dfs(GRAPH, START, GOAL), repeat=3, number=10000)

    bfs_avg_ms = (sum(bfs_times) / len(bfs_times)) * 1000
    dfs_avg_ms = (sum(dfs_times) / len(dfs_times)) * 1000

    print("=== BFS vs DFS Profiling ===")
    print(f"Start node : {START}")
    print(f"Goal node  : {GOAL}")
    print()
    print("BFS")
    print("Expanded   :", bfs_result)
    print("Nodes      :", len(bfs_result))
    print(f"Average time for 10,000 runs: {bfs_avg_ms:.2f} ms")
    print()
    print("DFS")
    print("Expanded   :", dfs_result)
    print("Nodes      :", len(dfs_result))
    print(f"Average time for 10,000 runs: {dfs_avg_ms:.2f} ms")


if __name__ == "__main__":
    main()
