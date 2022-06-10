def create_graph(V, E):
    graph = {}
    for key in V:
        graph[key] = []
        graph[key] = [x[1] for x in E if key == x[0] and key in graph]
    return graph


def DLS(graph, start, goal, path, level, maxD):
    print('\nCurrent level-->', level)
    print('Goal node testing for', start)
    path.append(start)
    if start == goal:
        print("Goal test successful")
        return path
    print('Goal node testing failed')
    if level == maxD:
        return False
    print('\nExpanding the current node', start)
    for child in graph[start]:
        if DLS(graph, child, goal, path, level+1, maxD):
            return path
        path.pop()
    return False


if __name__ == "__main__":
    V = ['S', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
    E = [('S', 'A'), ('S', 'B'), ('S', 'C'), ('A', 'D'), ('A', 'B'), ('C', 'B'), ('C', 'F'),
         ('B', 'D'), ('B', 'G'), ('B', 'F'), ('D', 'E'), ('F', 'E'), ('F', 'H'), ('E', 'G'), ('H', 'G')]

    graph = create_graph(V, E)
    start = 'S'
    goal = input('Enter the goal node:-')
    maxD = int(input("Enter the maximum depth limit:-"))
    print()
    path = list()
    res = DLS(graph, start, goal, path, 0, maxD)
    if(res):
        print("Path to goal node available")
        print("Path", path)
    else:
        print("No path available for the goal node in given depth limit")
