from collections import defaultdict

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if source == destination:
            return True
        graph = defaultdict(list)
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = set()
        stack = [source]
        visited.add(source)

        while stack:
            node = stack.pop()
            for neighbour in graph[node]:
                if neighbour == destination:
                    return True
                if neighbour not in visited:
                    stack.append(neighbour)
                    visited.add(neighbour)
        
        return False