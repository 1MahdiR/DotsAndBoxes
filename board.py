
n = 5 # width
m = 7 # height

class Edge:
    def __init__(self, d, x, y, c):
        self.d = d
        self.x = x
        self.y = y
        self.c = c
    
    def __repr__(self):
        return "<Edge: %d, x=%d, y=%d, c=%d>" % (self.d, self.x, self.y, self.c)
    
    def __str__(self):
        return self.__repr__()

class Square:
    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r
        self.ls = []

    def __repr__(self):
        return "<Square: x=%d, y=%d, r=%d, edges=%s>" % (self.x, self.y, self.r, str(self.ls))
    
    def __str__(self):
        return self.__repr__()
    
def draw_board(board_x, board_y, board_p):
    ls = []
    i_x = 0
    i_y = 0
    for i in range(len(board_x) + len(board_y)):
        if i % 2 == 0:
            ls.append(board_x[i_x])
            i_x += 1
        else:
            ls.append(board_y[i_y])
            i_y += 1
    
    table = []

    t = 0
    for i in ls:
        if t % 2 == 0:
            st = ""
            st += "#"
            for j in i:
                if j.c == 1:
                    st += "---#"
                else:
                    st += "   #"
            table.append(st)
        else:
            st = ""
            for j in i:
                if j.c == 1:
                    st += "|   "
                else:
                    st += "    "
            table.append(st)
            table.append(st)
            table.append(st)
        t += 1

    get_str_index = lambda x, y: (x * 4 + 2, y * 4 + 2)

    for i in board_p:
        for j in i:
            if j.r == "X":
                x_i, y_i = get_str_index(j.x, j.y)
                table[y_i] = table[y_i][:x_i] + "X" + table[y_i][x_i+1:]
            elif j.r == "O":
                x_i, y_i = get_str_index(j.x, j.y)
                table[y_i] = table[y_i][:x_i] + "O" + table[y_i][x_i+1:]

    for i in table:
        print(i)

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

for i in range(n-1):
    ls = []
    for j in range(m-1):
        edge_0 = board_h[j][i]
        edge_1 = board_h[j+1][i]
        edge_2 = board_v[j][i]
        edge_3 = board_v[j][i+1]
        square = Square(i, j, 0)
        square.ls.extend([edge_0, edge_1, edge_2, edge_3])
        ls.append(square)
    board_p.append(ls)

draw_board(board_h, board_v, board_p)