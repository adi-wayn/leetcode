class Solution(object):
    def bfs(self, graph, start):
        visited = set()
        queue = deque([start])
        visited.add(start)

        while queue:
            current = queue.popleft()
            print(current)  # Process the current node

            for neighbor in graph[current]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)


if __name__ == "__main__":
    from collections import deque

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
    print(f"BFS traversal starting from node {start_node}:")
    solution.bfs(graph, start_node)