from Tree import *


def max_value(node):
    if len(node.children) == 0:
        return node
    node.value = -100000
    for child in node.children:
        temp = min_value(child)
        if temp.value > node.value:
            node.value = temp.value
    return node


def min_value(node):
    if len(node.children) == 0:
        return node
    node.value = 100000
    for child in node.children:
        temp = max_value(child)
        if temp.value < node.value:
            node.value = temp.value
    return node


def minimax_search(state):
    max_value(state)


if __name__ == "__main__":
    A = Tree("A")
    B = Tree("B")
    C = Tree("C")
    D = Tree("D")
    E = Tree("E")
    F = Tree("F")
    G = Tree("G")
    H = Tree("H")
    I = Tree("I")
    J = Tree("J")
    K = Tree("K")
    L = Tree("L")
    M = Tree("M")
    N = Tree("N")
    Z = Tree("Z")
    A.add_child(B)
    A.add_child(C)
    B.add_child(D)
    B.add_child(E)
    C.add_child(F)
    C.add_child(G)
    D.add_child(H)
    D.add_child(I)
    E.add_child(J)
    E.add_child(K)
    F.add_child(M)
    F.add_child(N)
    G.add_child(L)
    G.add_child(Z)
    H.value = 2
    I.value = 9
    J.value = 7
    K.value = 4
    M.value = 8
    N.value = 9
    L.value = 3
    Z.value = 5
    minimax_search(A)
    print(A.value)
