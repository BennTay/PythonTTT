from graphics import *

def runWithGraphics():
    print('Tic-Tac-Toe with graphics is starting, enjoy!')
    # Run game with graphics

class Grid:
    def __init__(self, sym):
        self.sym = sym

    def __str__(self):
        return str(self.sym)

class PlainGame:
    def __init__(self):
        """
        self.grid = [['1', '2', '3'], 
        ['4', '5', '6'], 
        ['7', '8', '9']]
        """
        self.grid = [[], [], []]
        num = 1
        for i in range(3):
            for j in range(3):
                self.grid[i].append(Grid(str(num)))
                num += 1
        self.roundNum = 0
        self.winner = None

    def printGrid(self):
        print('=================================')
        print('Player 1: X\tPlayer 2: O')
        print('Round ' + str(self.roundNum + 1) + ', Player ' + self.getCurrentPlayerNum() + '\'s turn')
        print('         |         |         ')
        print('    ' + self.grid[0][0].__str__() + '    |    ' + self.grid[0][1].__str__() + '    |    ' + self.grid[0][2].__str__() + '    ')
        print('_________|_________|_________')
        print('         |         |         ')
        print('    ' + self.grid[1][0].__str__() + '    |    ' + self.grid[1][1].__str__() + '    |    ' + self.grid[1][2].__str__() + '    ')
        print('_________|_________|_________')
        print('         |         |         ')
        print('    ' + self.grid[2][0].__str__() + '    |    ' + self.grid[2][1].__str__() + '    |    ' + self.grid[2][2].__str__() + '    ')
        print('         |         |         ')
        print('=================================')

    def getCurrentPlayerNum(self):
        return str(((self.roundNum%2)+1))

    def getCurrentToken(self):
        if self.getCurrentPlayerNum() == '1':
            return 'X'
        else:
            return 'O'

    def checkForWin(self):
        print('checking for win')
        # use recursion to check horizontal, vertical and diagonal for 3 in a row

    def update(self, currentGridChoice):
        self.roundNum += 1
        gridList = []
        for i in range(3):
            gridList += self.grid[i]
        gridList[int(currentGridChoice) - 1].sym = self.getCurrentToken()


def isValidGridChoice(choiceStr, grid):
    choiceNum = int(choiceStr)
    if choiceNum < 1 or choiceNum > 9:
        return False
    gridList = []
    for i in range(3):
        gridList += grid[i]
    if gridList[choiceNum - 1].__str__() == choiceStr:
        return True
    else:
        return False

def displayWinScreen(game):
    print('End of game!') # Declare winner 
    game.printGrid()

def runWithoutGraphics():
    print('Tic-Tac-Toe without graphics is starting, enjoy!')
    currentGame = PlainGame()
    for i in range(9):
        currentGame.printGrid()
        while True:
            playerGridChoice = input('Player ' + str(((currentGame.roundNum%2)+1)) + ', pick a number.\n')
            if isValidGridChoice(playerGridChoice, currentGame.grid):
                break
            print('Invalid choice, please pick an available number.')
        currentGame.update(playerGridChoice)
    displayWinScreen(currentGame)


def main():
    print('Tic-Tac-Toe is starting...\n')
    while True:
        choice = input('Would you like to play with graphics?\nY/N\n')
        if choice.lower() == 'y' or choice.lower() == 'n':
            break
        else:
            print('Sorry, please try again.')

    if choice.lower() == 'y':
        runWithGraphics()
    else:
        runWithoutGraphics()

if __name__ == '__main__':
    main()
