class Solution(object):
    def dfs(self, graph, start):
        visited = set()
        self._dfs_helper(graph, start, visited)

    def _dfs_helper(self, graph, node, visited):
        if node not in visited:
            print(node)  # Process the current node
            visited.add(node)

        for neighbor in graph[node]:
            if neighbor not in visited:
                self._dfs_helper(graph, neighbor, visited)

if __name__ == "__main__":
    solution = Solution()
    graph = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F'],
        'D': [],
        'E': ['F'],
        'F': []
    }
    
    start_node = 'A'
    print(f"DFS traversal starting from node {start_node}:")
    solution.dfs(graph, start_node)