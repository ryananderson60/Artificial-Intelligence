Part 1:
Initial State: '123456789ABC DFE'
BFS: 3, 11, 6, 4
DFS: 3, 22, 7, 10
GBFS, h1: 3, 8, 3, 4
GBFS, h2: 3, 302, 100, 95
AStar, h1: 3, 8, 3, 4
AStar, h2: 3, 8, 3, 4
DLS: 3, 8, 3, 4
Initial State: '123456789AB DEFC'
BFS: 1, 3, 0, 0
DFS: 1, 3, 1, 3
GBFS, h1: 1, 3, 1, 3
GBFS, h2: -1, -1, -1, -1
AStar, h1: 1, 3, 1, 3
AStar, h2: 1, 3, 1, 3
DLS: 1, 3, 1, 4

Part 2:

Time complexities:
BFS graph: O(V+E) V is vertex, E is edges
DFS graph: O(V+E) V is vertex, E is edges
GBFS graph: O(nlogn) where n is number of nodes
AStar graph: O(b^d) d is depth
DLS: O(b^l) where l is the cutoff
