board = [
            ["player", "--", "--", "--", "--", "--", "--", "--",],
            ["--", "--", "--", "--", "--", "--", "--", "--",],
            ["--", "--", "--", "--", "mummy", "--", "--", "--",],
            ["--", "--", "--", "--", "--", "--", "--", "--",],
            ["--", "--", "--", "--", "--", "--", "--", "--",],
            ["--", "--", "--", "--", "--", "--", "--", "--",],
            ["--", "--", "--", "--", "--", "--", "--", "--",],
            ["--", "--", "--", "--", "--", "--", "--", "--",]
        ]


def index_2d(myList, v):
    for i, x in enumerate(myList):
        if v in x:
            return [i, x.index(v)]
    
    return [-1,-1]

def indexToString(index):
    node = "n"
    node = node + str(index[0]) + str(index[1])
    return node


def stringToIndex(node):
    n = int(node.replace('n',''))
    r = n//10
    c = n-(r*10) 
    return((r,c))



def moveLeft():
    position = index_2d(board , 'player')
    if position[1] != 0:
        board[position[0]][position[1]] = "--"
        board[position[0]] [(position[1]-1)] = "player"

def moveRight():
    position = index_2d(board , 'player')
    if position[1] != 7:
        board[position[0]][position[1]] = "--"
        board[position[0]] [(position[1]+1)] = "player"

def moveUp():
    position = index_2d(board , 'player')
    if position[0] != 0:
        board[position[0]][position[1]] = "--"
        board[position[0]-1] [(position[1])] = "player"

def moveDown():
    position = index_2d(board , 'player')
    if position[0] != 7:
        board[position[0]][position[1]] = "--"
        board[position[0]+1] [(position[1])] = "player"


def mummyMovement(path):
    print("path", path)
    position = index_2d(board , 'mummy')
    move = stringToIndex(path[1])
    board[position[0]][position[1]] = "--"
    board[move[0]][move[1]] = "mummy"
    

    # prev = stringToIndex(path[0])
    # board[prev[0]][prev[1]] = "--"