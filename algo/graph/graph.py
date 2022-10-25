"""

"""

"""

"""

from collections import deque

"""
BFS

https://cp-algorithms.com/graph/breadth-first-search.html

应用
- 在一个无权图上求从起点到其他所有点的最短路径。

--------------------------------------------------------------------------------
    Breadth First Search.
        Args :  G - Dictionary of edges
                s - Starting Node
        Vars :  vis - Set of visited nodes
                Q - Traversal Stack
--------------------------------------------------------------------------------
"""


def bfs(G, s):
    vis, Q = {s}, deque([s])
    print(s)
    while Q:
        u = Q.popleft()
        for v in G[u]:
            if v not in vis:
                print(v)
                vis.add(v)
                Q.append(v)
