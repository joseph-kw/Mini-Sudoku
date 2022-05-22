## Filling Rows
SIZE = 4
board1 = [[1, 0, 3, 0], [3, 0, 0, 2], [4, 3, 2, 1], [0, 0, 0, 3]]
board2 = [[0, 1, 3, 2], [2, 0, 1, 0], [1, 0, 0, 3], [3, 4, 2, 1]]
board3 = [[0, 0, 0, 0], [0, 1, 2, 4], [0, 3, 4, 1], [0, 4, 0, 2]]
def fill_row(board):
    checkTF = False
    for i in range(len(board)):
        if board[i].count(0) == 1:
            for j in range(len(board[i])):
                if board[i][j] == 0:
                    board[i][j] = 10 -sum(board[i])
                    checkTF = True
    return checkTF

## Filling Columns
def fill_col(board):
    lst = []
    countZ = 0
    count = 0
    idx = 0
    checkTF =False
    while idx<len(board):
        for i in range(len(board)):
            lst += str(board[i][idx])
        for j in lst:
            if j == '0':
                countZ+=1
            else:
                count+=int(j)
        if countZ==1:
            for z in range(len(board)):
                if board[z][idx] == 0:
                    board[z][idx] = 10 -count
                    checkTF = True
        lst =[]
        countZ=0
        count = 0
        idx+=1
    return checkTF

## Filling Sections
def fill_section(board):
    a = 0
    b = 2
    lst = []
    check = False
    for i in range(2): ## top left
        lst += board[i][a:b]
    if lst.count(0) == 1:
        for k in range(b):
            if board[0][k] == 0:
                board[0][k] = 10 - sum(lst)
                check = True
            elif board[1][k] == 0:
                board[1][k] = 10 - sum(lst)
                check = True
    lst = []
    for j in range(2,4): ## bottom left
        lst += board[j][a:b]
    if lst.count(0) == 1:
        for k in range(b):
            if board[2][k] == 0:
                board[2][k] = 10 -sum(lst)
                check = True
            elif board[2][k] == 0:
                board[2][k] = 10 - sum(lst)
                check = True
    lst = []
    a,b = 2,4
    for x in range(a): ## top right
        lst += board[x][a:b]
    if lst.count(0) == 1:
        for k in range(2,4):
            if board[0][k] == 0:
                board[0][k] = 10 -sum(lst)
                check = True
            elif board[1][k] == 0:
                board[1][k] = 10 -sum(lst)
                check = True
    lst = []
    for y in range(2,4): ## bottom right
        lst += board[y][a:b]
    if lst.count(0) == 1:
        for k in range(2,4):
            if board[2][k] == 0:
                board[2][k] = 10 -sum(lst)
                check = True
            elif board[3][k] == 0:
                board[3][k] = 10 - sum(lst)
                check = True
    return check

## Filling the Board
def fill_board(board):
    fillable = True  # indicate if a board is still fillable
    while fillable == True:
        fill_row(board)
        fill_col(board)
        fill_section(board)
        lst =[]
        for i in range(len(board)):
            lst += [board[i].count(0)]
        if lst == [0,0,0,0]:
            fillable = False                
    return board
