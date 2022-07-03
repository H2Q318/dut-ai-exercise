# import heapq
# from TreeNode import *


# def create_tree(V, E):
#     nodes = []
#     for node in V:
#         nodes.append(Node(node, 1))

#     edges = []
#     for edge in E:
#         edges.append(edge + (1, ))

#     tree = Tree()
#     tree.add_nodes(nodes)
#     tree.add_edges(edges)
#     tree.nodes[0].cost = 0

#     return tree


# def update_cost(tree, currentNode, prevNode):
#     if tree.get_edge(prevNode, currentNode):
#         cost = prevNode.cost + tree.get_edge(prevNode, currentNode)[2]
#         if currentNode.cost > cost:
#             currentNode.cost = cost


# def a_star(tree, start, end):
#     frontier = [start]
#     explored = []
#     while len(frontier) > 0:
#         state = heapq.heappop(frontier)
#         explored.append(state)
#         print(state)
#         if state == end:
#             return explored
#         for child in state.neighbors():
#             update_cost(tree, child, state)
#             if child.get_label() not in list(set(node.get_label() for node in frontier + explored)):
#                 heapq.heappush(frontier, child)
#     return False


# if __name__ == '__main__':
#     V = ['S', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
#     E = [('S', 'A'), ('S', 'B'), ('S', 'C'), ('A', 'D'), ('A', 'B'), ('C', 'B'), ('C', 'F'),
#          ('B', 'D'), ('B', 'G'), ('B', 'F'), ('D', 'E'), ('F', 'E'), ('F', 'H'), ('E', 'G'), ('H', 'G')]

#     tree = create_tree(V, E)

#     result = a_star(tree, tree.nodes[0], tree.nodes[7])
#     if result:
#         s = 'explored: '
#         for i in result:
#             s += i.label + ' '
#             print(s)
#     else:
#         print('Not Found!!')


import heapq
from TreeNode import *


def create_tree(V, E):
    nodes = []
    for node in V:
        nodes.append(Node(node[0], node[1]))

    edges = []
    for edge in E:
        edges.append(edge)

    tree = Tree()
    tree.add_nodes(nodes)
    tree.add_edges(edges)
    tree.nodes[0].cost = 0

    return tree


def update_cost(tree, currentNode, prevNode):
    if tree.get_edge(prevNode, currentNode):
        cost = prevNode.cost + tree.get_edge(prevNode, currentNode)[2]
        if currentNode.cost > cost:
            currentNode.cost = cost


def a_star(tree, start, end):
    frontier = [start]
    explored = []
    while len(frontier) > 0:
        state = heapq.heappop(frontier)
        explored.append(state)
        print(state)
        if state == end:
            return explored
        for child in state.neighbors():
            update_cost(tree, child, state)
            if child.get_label() not in list(set(node.get_label() for node in frontier + explored)):
                heapq.heappush(frontier, child)
    return False


if __name__ == '__main__':
    V = [('S', 12), ('A', 9), ('B', 8), ('C', 7), ('D', 6), ('E', 5), ('F', 4), ('G', 10),
         ('H', 10), ('K', 3), ('M', 9), ('N', 10), ('I', 6), ('J', 0), ('L', 0), ('Z', 8)]
    E = [('S', 'A', 5), ('S', 'B', 6), ('S', 'C', 5), ('A', 'D', 6), ('A', 'E', 7), ('B', 'F', 3), ('B', 'G', 4), ('C',
                                                                                                                   'H', 6), ('C', 'K', 4), ('D', 'M', 5), ('D', 'N', 8), ('E', 'I', 8), ('F', 'J', 4), ('F', 'L', 4), ('K', 'Z', 2)]

    tree = create_tree(V, E)
    
    index_array = []
    index = -1
    for i in tree.nodes:
        index += 1
        if i.goalCost == 0:
            index_array.append(index)
        
    for i in index_array:
        result = a_star(tree, tree.nodes[0], tree.nodes[i])
        if result:
            s = 'explored: '
            for i in result:
                s += i.label + ' '
                print(s)
        else:
            print('Not Found!!')