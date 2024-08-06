from board import draw_board
from board import calculate_reward_n_layer
from board import Edge, Square
from board import game_over

WIDTH=5
HEIGHT=3

FIRST_TURN=True

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

    # board_v[0][0].c = 1
    # board_v[0][1].c = 1
    # board_v[1][0].c = 1
    # board_v[1][1].c = 1
    # board_h[0][0].c = 1
    # board_h[2][0].c = 1

    turn = FIRST_TURN
    game_ = None
    while True:
        game_ = game_over(board_p)
        if game_:
            break
        reward = False
        if turn:
            draw_board(ls_edges, board_p)
            print("Enter the edge you choose:")
            print("Enter with this order: axis-type(horizontal(0)/vertical(1)) axis-x axis-y".format(n-1, m-1))
            t, x, y = [ int(x) for x in input().split() ]
            if t == 0:
                board_h[y][x].c = 1
            else:
                board_v[y][x].c = 1
            
            for i in board_p:
                for j in i:
                    if j.r == 0:
                        SQUARED = True
                        for k in j.ls:
                            if k.c == 0:
                                SQUARED = False
                        if SQUARED:
                            j.r = "X"
                            reward = True

        else:

            e = calculate_reward_n_layer(ls_edges, board_p)[1]

            print(e)
            t, x, y = (e.d, e.x, e.y)
            if t == 0:
                board_h[y][x].c = 1
            else:
                board_v[y][x].c = 1
            
            for i in board_p:
                for j in i:
                    if j.r == 0:
                        SQUARED = True
                        for k in j.ls:
                            if k.c == 0:
                                SQUARED = False
                        if SQUARED:
                            j.r = "O"
                            reward = True

        if not reward:
            turn = not turn

    if game_ == "X":
        print("Player Won!!!")
    elif game_ == "O":
        print("Computer Won!!!")
    else:
        print("It's a Tie!!!")