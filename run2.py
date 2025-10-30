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
    result = bfs_from_gateways(graph, targets)
    return list(result)

def build_graph(edges):
    graph = {}
    for node1, node2 in edges:
        graph.setdefault(node1, []).append(node2)
        graph.setdefault(node2, []).append(node1)
    return graph


def bfs_from_gateways(graph, targets):
    queue = deque()
    visited = {}
    for target in targets:
        queue.append((target, target))
        visited[target] = (0, target)
    answer = set()
    while queue:
        current, source_target = queue.popleft()
        current_distance, _ = visited[current]
        for neighbor in graph.get(current, []):
            if neighbor in targets and current not in targets:
                answer.add(f"{neighbor}-{current}")
            elif neighbor not in visited and neighbor not in targets:
                visited[neighbor] = (current_distance + 1, source_target)
                queue.append((neighbor, source_target))
            if current in targets and neighbor not in targets:
                answer.add(f"{current}-{neighbor}")
    return sorted(list(answer))


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