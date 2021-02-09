board = ['-', '-', '-', '-', '-', '-', '-',
         '-', '-', '-', '-', '-', '-', '-',
         '-', '-', '-', '-', '-', '-', '-',
         '-', '-', '-', '-', '-', '-', '-',
         '-', '-', '-', '-', '-', '-', '-',
         '-', '-', '-', '-', '-', '-', '-']


def printBoard():
    print(" | " + board[0] + " | " + " | " + board[1] + " | " + " | " + board[2] + " | " + " | " + board[3] + " | " + " | " + board[4] + " | " + " | " + board[5] + " | " + " | " + board[6] + " | ")
    print(" | " + board[7] + " | " + " | " + board[8] + " | " + " | " + board[9] + " | " + " | " + board[10] + " | " + " | " + board[11] + " | " + " | " + board[12] + " | " + " | " + board[13] + " | ")
    print(" | " + board[14] + " | " + " | " + board[15] + " | " + " | " + board[16] + " | " + " | " + board[17] + " | " + " | " + board[18] + " | " + " | " + board[19] + " | " + " | " + board[20] + " | ")
    print(" | " + board[21] + " | " + " | " + board[22] + " | " + " | " + board[23] + " | " + " | " + board[24] + " | " + " | " + board[25] + " | " + " | " + board[26] + " | " + " | " + board[27] + " | ")
    print(" | " + board[28] + " | " + " | " + board[29] + " | " + " | " + board[30] + " | " + " | " + board[31] + " | " + " | " + board[32] + " | " + " | " + board[33] + " | " + " | " + board[34] + " | ")
    print(" | " + board[35] + " | " + " | " + board[36] + " | " + " | " + board[37] + " | " + " | " + board[38] + " | " + " | " + board[39] + " | " + " | " + board[40] + " | " + " | " + board[41] + " | ")

def checkWin(ind1,ind2,ind3,ind4):

    if board[ind1] == board[ind2] == board[ind3] == board[ind4] and board[ind1] != '-':
        return True

def confirmRowWin(ind1,ind2,ind3,ind4,ind5,ind6,ind7):
    if checkWin(ind1,ind2,ind3,ind4) or checkWin(ind2,ind3,ind4,ind5) or checkWin(ind3,ind4,ind5,ind6) or checkWin(ind4,ind5,ind6,ind7):
        return True

def confirmWin(ind1,ind2,ind3,ind4,ind5,ind6):
    if checkWin(ind1,ind2,ind3,ind4) or checkWin(ind2,ind3,ind4,ind5) or checkWin(ind3,ind4,ind5,ind6):
        return True

def checkRows():

    if confirmRowWin(0,1,2,3,4,5,6) or confirmRowWin(7,8,9,10,11,12,13) or confirmRowWin(14,15,16,17,18,19,20) or confirmRowWin(21,22,23,24,25,26,27) or confirmRowWin(28,29,30,31,32,33,34) or confirmRowWin(35,36,37,38,39,40,41):
        return True

def checkColumns():
    if confirmWin(0,7,14,21,28,35) or confirmWin(1,8,15,22,29,36) or confirmWin(2,9,16,23,30,37) or confirmWin(3,10,17,24,31,38) or confirmWin(4,11,18,25,32,39) or confirmWin(5,12,19,26,33,40) or confirmWin(6,13,20,27,34,41):
        return True

def checkDiagonalsRightToLeft():
    if checkWin(3,9,15,21) or checkWin(4,10,16,22) or checkWin(20,26,32,38) or checkWin(10,16,22,28) or checkWin(13,19,25,31) or checkWin(19,25,31,37):
        return True

    if confirmWin(5,11,17,23,29,35) or confirmWin(6,12,18,24,30,36):
        return True

def checkDiagonalLeftToRight():
    if checkWin(3,11,19,27) or checkWin(14,22,30,38) or checkWin(2,10,18,26) or checkWin(10,18,26,34) or checkWin(7,15,23,31) or checkWin(15,23,31,39):
        return True

    if confirmWin(1,9,17,25,33,41) or confirmWin(0,8,16,24,32,40):
        return True

def flipPlayer(player):
    if player == "R":
        player = "Y"
    else:
        player = "R"
    return player


def inputOnBoard(player):
    while True:
        inp = int(input("Enter a position "))
        inp -= 1

        if inp < 0 or inp > 41 or board[inp] != '-':
            print("Invalid choice")
        else:
            board[inp] = player
            break

plyer = "R"

while True:

    printBoard()
    inputOnBoard(plyer)

    if checkRows() or checkColumns() or checkDiagonalLeftToRight() or checkDiagonalsRightToLeft():
        printBoard()
        print("Player "+plyer+" wins")
        break

    if '-' not in board:
        print("GAME DRAW")
        break

    plyer = flipPlayer(plyer)
