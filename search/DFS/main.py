def create_graph(V, E):
    graph = {}
    for key in V:
        graph[key] = []
        graph[key] = [x[1] for x in E if key == x[0] and key in graph]
    return graph


def DFS(graph, initState, goal):
    frontier = [initState]
    explored = []
    while frontier:
        state = frontier.pop(len(frontier) - 1)
        explored.append(state)
        if state == goal:
            return explored
        for neighbor in graph[state]:
            if neighbor not in (explored and frontier):
                frontier.append(neighbor)
    return False


if __name__ == "__main__":
    V = ['S', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
    E = [('S', 'A'), ('S', 'B'), ('S', 'C'), ('A', 'D'), ('A', 'B'), ('C', 'B'), ('C', 'F'),
         ('B', 'D'), ('B', 'G'), ('B', 'F'), ('D', 'E'), ('F', 'E'), ('F', 'H'), ('E', 'G'), ('H', 'G')]

    graph = create_graph(V, E)

    result = DFS(graph, 'S', 'G')
    if result:
        s = 'explored: '
        for i in result:
            s += i + ' '
            print(s)
    else:
        print('Not Found!')
