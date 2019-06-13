from graphics import *

def runWithGraphics():
    print('Tic-Tac-Toe with graphics is starting, enjoy!')
    # Run game with graphics

class Grid:
    def __init__(self, sym):
        self.sym = sym

    def __str__(self):
        return str(self.sym)

class Row:
    def __init__(self):
        self.lst = []

    def checkForWin(self):
        if self.lst[0] == self.lst[1] and self.lst[1] == self.lst[2]:
            return True
        else:
            return False

class PlainGame:
    def __init__(self):
        self.grid = [[], [], []]
        num = 1
        for i in range(3):
            for j in range(3):
                self.grid[i].append(Grid(str(num)))
                num += 1
        self.rows = {}
        for i in range(8):
            self.rows[i+1] = Row()

        # Top horizontal row, row 1
        self.rows[1].lst.append(self.grid[0][0])
        self.rows[1].lst.append(self.grid[0][1])
        self.rows[1].lst.append(self.grid[0][2])

        # Middle horizontal row, row 2
        self.rows[2].lst.append(self.grid[1][0])
        self.rows[2].lst.append(self.grid[1][1])
        self.rows[2].lst.append(self.grid[1][2])

        # Bottom horizontal row, row 3
        self.rows[3].lst.append(self.grid[2][0])
        self.rows[3].lst.append(self.grid[2][1])
        self.rows[3].lst.append(self.grid[2][2])

        # Left vertical row, row 4
        self.rows[4].lst.append(self.grid[0][0])
        self.rows[4].lst.append(self.grid[1][0])
        self.rows[4].lst.append(self.grid[2][0])

        # Middle vertical row, row 5
        self.rows[5].lst.append(self.grid[0][1])
        self.rows[5].lst.append(self.grid[1][1])
        self.rows[5].lst.append(self.grid[2][1])

        # Right vertical row, row 6
        self.rows[6].lst.append(self.grid[0][2])
        self.rows[6].lst.append(self.grid[1][2])
        self.rows[6].lst.append(self.grid[2][2])

        # Top-left to bottom-right diagonal row, row 7
        self.rows[7].lst.append(self.grid[0][0])
        self.rows[7].lst.append(self.grid[1][1])
        self.rows[7].lst.append(self.grid[2][2])

        # Top-right to bottom-left diagonal row, row 8
        self.rows[8].lst.append(self.grid[0][2])
        self.rows[8].lst.append(self.grid[1][1])
        self.rows[8].lst.append(self.grid[2][0])

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

    def hasAWin(self, currentGridChoice):
        gridNum = int(currentGridChoice)
        if gridNum == 1:
            row1Win = self.rows[1].checkForWin()
            row4Win = self.rows[4].checkForWin()
            row7Win = self.rows[7].checkForWin()
            return row1Win or row4Win or row7Win
        elif gridNum == 2:
            row1Win = self.rows[1].checkForWin()
            row5Win = self.rows[5].checkForWin()
            return row1Win or row5Win
        elif gridNum == 3:
            row1Win = self.rows[1].checkForWin()
            row6Win = self.rows[6].checkForWin()
            row8Win = self.rows[8].checkForWin()
            return row1Win or row6Win or row8Win
        elif gridNum == 4:
            row2Win = self.rows[2].checkForWin()
            row4Win = self.rows[4].checkForWin()
            return row2Win or row4Win
        elif gridNum == 5:
            row2Win = self.rows[2].checkForWin()
            row5Win = self.rows[5].checkForWin()
            row7Win = self.rows[7].checkForWin()
            row8Win = self.rows[8].checkForWin()
            return row2Win or row5Win or row7Win or row8Win
        elif gridNum == 6:
            row2Win = self.rows[2].checkForWin()
            row6Win = self.rows[6].checkForWin()
            return row2Win or row6Win
        elif gridNum == 7:
            row3Win = self.rows[3].checkForWin()
            row4Win = self.rows[4].checkForWin()
            row8Win = self.rows[8].checkForWin()
            return row3Win or row4Win or row8Win
        elif gridNum == 8:
            row3Win = self.rows[3].checkForWin()
            row5Win = self.rows[5].checkForWin()
            return row3Win or row5Win
        elif gridNum == 9:
            row3Win = self.rows[3].checkForWin()
            row6Win = self.rows[6].checkForWin()
            row7Win = self.rows[7].checkForWin()
            return row3Win or row6Win or row7Win



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
        if currentGame.hasAWin(playerGridChoice):
            break
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
