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
        return "<Square: x=%s, y=%d, r=%s, edges=%s>" % (self.x, self.y, str(self.r), str(self.ls))
    
    def __str__(self):
        return self.__repr__()
    
def draw_board(edges, board_p):
    ls = edges
    
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

def calculate_reward(board_p:list, edge:Edge):
    edge.c = 1
    
    changed_squares = []
    reward = 0
    for i in board_p:
        for j in i:
            if j.r == 0:
                SQUARED = True
                for k in j.ls:
                    if k.c == 0:
                        SQUARED = False
                if SQUARED:
                    j.r = "X"
                    reward += 1
                    changed_squares.append(j)
    
    edge.c = 0
    for i in changed_squares:
        i.r = 0

    return reward

def calculate_reward_n_layer(edges, board_p:list, depth=0, turn=True, reward=0):
    max_reward = (0, None)

    ls = edges
    current_depth = depth
    current_turn = turn

    if depth == 3:
        for i in ls:
            for j in i:
                if j.c == 0:
                    r = calculate_reward(board_p, j)
                    if r > max_reward[0]:
                        max_reward = (r, j)
                        #print("k", max_reward)
        if turn:
            #print(depth, max_reward, turn)
            return max_reward
        else:
            #print(depth, (-max_reward[0], max_reward[1]), turn)
            return (-max_reward[0], max_reward[1])

    r_ls = []
    for i in ls:
        for j in i:
            if j.c == 0:
                re = calculate_reward(board_p, j)
                #print(re)
                if re:
                    j.c = 1
                    changed_squares = []
                    for k in board_p:
                        for l in k:
                            if l.r == 0:
                                SQUARED = True
                                for m in l.ls:
                                    if m.c == 0:
                                        SQUARED = False
                                if SQUARED:
                                    m.r = "X"
                                    changed_squares.append(l)
                    reward = calculate_reward_regret_0_layer(ls, board_p, depth=current_depth+1, turn=(current_turn))[0]
                    for m in changed_squares:
                        m.r = 0
                    j.c = 0
                else:
                    j.c = 1
                    reward = calculate_reward_regret_0_layer(ls, board_p, depth=current_depth+1, turn=(not current_turn))[0]
                    j.c = 0

                r_ls.append((reward, j))
    if turn:
        m = max(r_ls, key=lambda x: x[0])
    else:
        m = min(r_ls, key=lambda x: x[0])
    #print(r_ls)
    #if depth == 0:
    #    print(depth, sorted(r_ls, key=lambda x: x[0], reverse=True), turn)
    return m