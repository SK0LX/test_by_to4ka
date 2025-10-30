import sys
from collections import deque


def solve(edges: list[tuple[str, str]]) -> list[str]:
    """
    Решение задачи об изоляции вируса

    Args:
        edges: список коридоров в формате (узел1, узел2)

    Returns:
        список отключаемых коридоров в формате "Шлюз-узел"
    """
    graph = build_graph(edges)
    targets = {node for node in graph if node.isupper()}
    result = bfs_from_targets(graph, targets)
    return list(result)

def build_graph(edges):
    graph = {}
    for node1, node2 in edges:
        graph.setdefault(node1, []).append(node2)
        graph.setdefault(node2, []).append(node1)
    return graph


def bfs_from_targets(graph, targets):
    queue = deque()
    visited = {}
    start_node = 'a'
    queue.append(start_node)
    visited[start_node] = 0
    answer = set()
    while queue:
        current = queue.popleft()
        current_distance = visited[current]
        for neighbor in graph.get(current, []):
            if neighbor not in visited:
                visited[neighbor] = current_distance + 1
                queue.append(neighbor)
            if neighbor in targets:
                for node in graph[neighbor]:
                    if node not in targets:
                        answer.add((visited[node], f"{neighbor}-{node}"))
    sorted_answer = sorted(answer)
    return [edge for dist, edge in sorted_answer]


def main():
    edges = []
    for line in sys.stdin:
        line = line.strip()
        if line:
            node1, sep, node2 = line.partition('-')
            if sep:
                edges.append((node1, node2))

    result = solve(edges)
    for edge in result:
        print(edge)


if __name__ == "__main__":
    main()