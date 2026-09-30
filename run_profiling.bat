@echo off
echo Installing/checking py-spy...
py -m pip install py-spy

echo.
echo Creating BFS flame graph...
py -m py_spy record --format flamegraph --output profiling\bfs_profile.svg -- python profiling\pyspy_target.py bfs

echo.
echo Creating DFS flame graph...
py -m py_spy record --format flamegraph --output profiling\dfs_profile.svg -- python profiling\pyspy_target.py dfs

echo.
echo Done. Open:
echo profiling\bfs_profile.svg
echo profiling\dfs_profile.svg
pause
