#Name: Sadie Shank, individual project
#Date: 05/26/23
#Project 1
#Sources: https://github.com/javacodingcommunity/TicTacToeAI-with-Minimax/blob/main/ticTacToeAI.py
#JavaCodingCommunity: Some of the names of the functions are the same as provided here, but I used them to check which functions I was missing. 
#The functions that were heavily inspired (meaning I used their functions and heavily modified them to fit my environment) by JavaCodingCommunity in this program are as follows: compMove, minimax, checkWhichMarkWon, GameOver
#The functions that were inspired (meaning they were referenced as I wrote this code, but were heavily modified) by JavaCodingCommunity are as follows: InsertLetter, spaceIsFree
board = ['-', '-', '-', '-', '-', '-', '-', '-', '-']

print("Welcome to Tic-Tac-Toe! You are playing on a 3x3 gameboard where each cell corresponds to a number. These are the corresponding numbers: ")
print(" 1 2 3 ")
print(" 4 5 6 ")
print(" 7 8 9 ")
print("When a cell is blank, it will instead print '-' where the X or O would normally go. Let's begin!")
player = input("Which side would you like to play ('X' or 'O'): ")

# This is checking to ensure that the side that the player chose is valid.
# If it isn't, it reruns the question and tells them to input it again.
# It then sets the bot to whatever was not chosen.
def checkinput(player):
    if player not in ['X', 'O', 'x', 'o']:
        player = input("That is an invalid selection, please try again. Which side would you like to play: ")
        checkinput(player)

    return player

# This gets the move from the player and puts in the letter to the corresponding space.
def getMove(player):
    move = input("It's your turn! Input the number corresponding to the square that you would like to place an " + player + " in: ")
    if move in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
        move = int(move)
        if spaceIsFree(move - 1):
            board[move - 1] = player
        else:
            print("That cell is already filled. Please try again.")
            getMove(player)
    else:
        print("That is not a valid move. Please try again.")
        getMove(player)
    #printboard(board)

# Print the board itself
def printboard(board):
    print(board[0] + ' ' + board[1] + ' ' + board[2])
    print(board[3] + ' ' + board[4] + ' ' + board[5])
    print(board[6] + ' ' + board[7] + ' ' + board[8])

# Pick the move
def compMove(bot):
    bestScore = -800
    bestMove = 0
    for key in range(9):
        if board[key] == '-':
            board[key] = bot
            score = minimax(board, 0, False)
            board[key] = '-'
            if score > bestScore:
                bestScore = score
                bestMove = key

    insertLetter(bot, bestMove)
    return

# Decide which move is the best
def minimax(board, depth, isMaximizing):
    if checkWhichMarkWon(bot):
        return 1
    elif checkWhichMarkWon(player):
        return -1
    elif checkDraw():
        return 0

    if isMaximizing:
        bestScore = -800
        for key in range(9):
            if board[key] == '-':
                board[key] = bot
                score = minimax(board, depth + 1, False)
                board[key] = '-'
                if score > bestScore:
                    bestScore = score
        return bestScore
    else:
        bestScore = 800
        for key in range(9):
            if board[key] == '-':
                board[key] = player
                score = minimax(board, depth + 1, True)
                board[key] = '-'
                if score < bestScore:
                    bestScore = score
        return bestScore

# Looks to see who won the game
def checkWhichMarkWon(mark):
    if board[0] == board[1] == board[2] == mark:
        return True
    elif board[3] == board[4] == board[5] == mark:
        return True
    elif board[6] == board[7] == board[8] == mark:
        return True
    elif board[0] == board[3] == board[6] == mark:
        return True
    elif board[1] == board[4] == board[7] == mark:
        return True
    elif board[2] == board[5] == board[8] == mark:
        return True
    elif board[0] == board[4] == board[8] == mark:
        return True
    elif board[6] == board[4] == board[2] == mark:
        return True
    else:
        return False

# Looks to see if there has been a tie
def checkDraw():
    for key in range(9):
        if board[key] == '-':
            return False
    return True

# Checks to see if the game has ended
def gameover():
    if board[0] == board[1] == board[2] != '-':
        return True
    elif board[3] == board[4] == board[5] != '-':
        return True
    elif board[6] == board[7] == board[8] != '-':
        return True
    elif board[0] == board[3] == board[6] != '-':
        return True
    elif board[1] == board[4] == board[7] != '-':
        return True
    elif board[2] == board[5] == board[8] != '-':
        return True
    elif board[0] == board[4] == board[8] != '-':
        return True
    elif board[6] == board[4] == board[2] != '-':
        return True
    else:
        return False

# Give the ending message and see who won the game.
def ending(bot):
    if checkWhichMarkWon(bot):
        print("The computer won!")
    elif checkWhichMarkWon(player):
        print("You won!")
    else:
        print("It's a tie!")
        printboard(board)

# Inserts the letter into the tic-tac-toe board
def insertLetter(letter, position):
    if spaceIsFree(position):
        board[position] = letter
        printboard(board)
    else:
        print("Can't insert there!")

def spaceIsFree(position):
    return board[position] == '-'

# *****************DRIVER********************
player = checkinput(player)
if player == 'X' or player == 'x':
    bot = 'O'
    player = 'X'
else:
    bot = 'X'
    player = 'O'

while not gameover() and not checkDraw():
    getMove(player)
    if not gameover() and not checkDraw():
        compMove(bot)

ending(bot)