class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        
        n = len(graph)
        vis = [False] * n
        color = [0] * n
        
        def dfs(u):
            vis[u] = True
            for v in graph[u]:
                if color[v] != 0 and color[u] == color[v]:
                    return False
                if not vis[v]:
                    color[v] = color[u] * -1
                    if not dfs(v):
                        return False
            return True
        is_bipartite = True
        for start_node in range(n):
            if len(graph[start_node]) and not vis[start_node] > 0:
                color[start_node] = 1
                is_bipartite &= dfs(start_node)
        return is_bipartite
