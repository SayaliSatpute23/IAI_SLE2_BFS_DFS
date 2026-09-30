import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from bfs_dfs import GRAPH, START, GOAL, bfs, dfs


def run_bfs():
    print("Starting BFS...")
    for _ in range(1000000):
        bfs(GRAPH, START, GOAL)


def run_dfs():
    print("Starting DFS...")
    for _ in range(1000000):
        dfs(GRAPH, START, GOAL)


if __name__ == "__main__":
    algorithm = sys.argv[1].lower()

    print("PID:", os.getpid())
    print("Attach py-spy now, then press ENTER.")
    input()

    if algorithm == "bfs":
        run_bfs()
    elif algorithm == "dfs":
        run_dfs()