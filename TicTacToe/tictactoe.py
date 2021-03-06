gamemat = [0] * 4
for i in range(4):
    gamemat[i] = [0] * 4
player = 1
gameEnd = False
gameResult = None

def readInput(currentPlayer):
    print("Player " + str(currentPlayer) + " (input x and y, seperated with a space): ", end = "")
    try:
        x,y = input().split()
        x = int(x)
        y = int(y)
    except ValueError:
        print("Invalid move")
        readInput(currentPlayer)
        return
    if x >= 4 or y >= 4 or x <= 0 or y <= 0:
        print("Invalid move")
        readInput(currentPlayer)
        return
    if gamemat[x][y] != 0:
        # Occupied
        print("Invalid move")
        readInput(currentPlayer)
        return
    else:
        gamemat[x][y] = currentPlayer # 0 => blank / 1 => player 1 / 2 => player 2
    global player
    player = int(not bool(currentPlayer-1)) +1

    print("player: " + str(player))
    renderGamemat()


def printPos(x, y):
    toPrint = None
    if gamemat[x][y]:
        toPrint = "X" if gamemat[x][y] == 1 else "O"
    else:
        toPrint = " "
    return str(toPrint)

def renderGamemat():
    print("     1 | 2 | 3 => x-axis")
    print("   -------------")
    print(" 1 | " + printPos(1, 1) + " | " + printPos(2, 1) + " | " + printPos(3 ,1) + " |")
    print("   -------------")
    print(" 2 | " + printPos(1, 2) + " | " + printPos(2, 2) + " | " + printPos(3, 2) + " |")
    print("   -------------")
    print(" 3 | " + printPos(1, 3) + " | " + printPos(2, 3) + " | " + printPos(3, 3) + " |")
    print(" |")
    print("y-axis")
    print()

def checkWiningConditions():
    g = gamemat
    # algorithm to be improved later :P
    for i in range(1,4):
        # check column
        if(g[i][1] != 0 and g[i][1] == g[i][2] and g[i][2] == g[i][3] and g[i][1] == g[i][3]):
            return g[i][1]
        # check row
        if(g[1][i] != 0 and g[1][i] == g[2][i] and g[2][i] == g[3][i] and g[1][i] == g[3][i]):
            return g[1][i]
    # check diagonal
    if(g[1][1] != 0 and g[1][1] == g[2][2] and g[2][2] == g[3][3] and g[1][1] == g[3][3]):
        return g[1][1]
    if(g[1][3] != 0 and g[1][3] == g[2][2] and g[2][2] == g[3][1] and g[1][3] == g[3][1]):
        return g[1][3]
    return 0


def resetAllVar():
    global gamemat, player, gameEnd, gameResult
    gamemat = [0] * 4
    for i in range(4):
        gamemat[i] = [0] * 4
    player = 1
    gameEnd = False
    gameResult = None

def gameInit():
    resetAllVar()
    gameEnd = False
    while not gameEnd:
        for i in range(5):
            print()
        renderGamemat()
        readInput(player)
        gameResult = checkWiningConditions()
        if gameResult != 0:
            gameEnd = True
    # Game ends
    print("Player " + str(gameResult) + " wins!")
    print()
    print("Do you want to play again? Yes/No/Y/N")
    tmp = input().lower()
    if tmp == "yes" or tmp == "y":
        main()
        return
    else:
        exit()




def main():
    for i in range(10):
        print()
    print("Welcome to Tic Tac Toe")
    print("This game needs 2 players")
    print("Press enter to start!")
    input()
    gameInit()

main()