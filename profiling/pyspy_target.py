import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from bfs_dfs import GRAPH, START, GOAL, bfs, dfs


def run_bfs():
    for _ in range(1_000_000):
        bfs(GRAPH, START, GOAL)


def run_dfs():
    for _ in range(1_000_000):
        dfs(GRAPH, START, GOAL)


if __name__ == "__main__":
    algorithm = sys.argv[1].lower()

    if algorithm == "bfs":
        run_bfs()
    elif algorithm == "dfs":
        run_dfs()
    else:
        print("Usage: python pyspy_target.py [bfs|dfs]")