from random import random

from board import draw_board
from board import calculate_reward_n_layer
from board import Edge, Square

WIDTH=4
HEIGHT=3

if __name__ == "__main__":
    n = WIDTH
    m = HEIGHT
    
    board_h = []

    board_v = []

    board_p = []

    for i in range(m):
        ls = []
        for j in range(n - 1):
            e = Edge(0, j, i, 0)
            ls.append(e)
        board_h.append(ls)

    for i in range(m-1):
        ls = []
        for j in range(n):
            e = Edge(1, j, i, 0)
            ls.append(e)
        board_v.append(ls)

    for i in range(m-1):
        ls = []
        for j in range(n-1):
            edge_0 = board_h[i][j]
            edge_1 = board_h[i+1][j]
            edge_2 = board_v[i][j]
            edge_3 = board_v[i][j+1]
            square = Square(j, i, 0)
            square.ls.extend([edge_0, edge_1, edge_2, edge_3])
            ls.append(square)
        board_p.append(ls)

    i_x = 0
    i_y = 0
    ls_edges = []
    for i in range(len(board_h) + len(board_v)):
        if i % 2 == 0:
            ls_edges.append(board_h[i_x])
            i_x += 1
        else:
            ls_edges.append(board_v[i_y])
            i_y += 1

    draw_board(ls_edges, board_p)