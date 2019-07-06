from graphics import *

class GraphicGame:
    def __init__(self, plain_game, window):
        self.plain_game = plain_game
        self.window = window
        self.pointList = []
        self.pointList.append(Point(100, 200))
        self.pointList.append(Point(300, 200))
        self.pointList.append(Point(500, 200))
        self.pointList.append(Point(100, 400))
        self.pointList.append(Point(300, 400))
        self.pointList.append(Point(500, 400))
        self.pointList.append(Point(100, 600))
        self.pointList.append(Point(300, 600))
        self.pointList.append(Point(500, 600))

    def updateWindow(self, gridNum):
        self.pointList[int(gridNum) - 1].draw(self.window)


def initializeBoard(window):
    line1 = Line(Point(0, 300), Point(600, 300))
    line2 = Line(Point(0, 500), Point(600, 500))
    line3 = Line(Point(200, 100), Point(200, 700))
    line4 = Line(Point(400, 100), Point(400, 700))
    topBorder = Line(Point(0, 100), Point(600, 100))
    textBox = Text(Point(300, 50), "Tic-Tac-Toe has started!")
    line1.draw(window)
    line2.draw(window)
    line3.draw(window)
    line4.draw(window)
    topBorder.draw(window)
    textBox.draw(window)

def translateCoordinatesToGrid(coordinates):
    x = coordinates.getX()
    y = coordinates.getY()

    if y < 100:
        raise ValueError
    elif (y <= 300 and y >= 100):
        if (x <= 200 and x >= 0):
            return 1
        elif (x <= 400 and x > 200):
            return 2
        elif (x <= 600 and x > 400):
            return 3
    elif (y <= 500 and y > 300):
        if (x <= 200 and x >= 0):
            return 4
        elif (x <= 400 and x > 200):
            return 5
        elif (x <= 600 and x > 400):
            return 6
    elif (y <= 700 and y > 500):
        if (x <= 200 and x >= 0):
            return 7
        elif (x <= 400 and x > 200):
            return 8
        elif (x <= 600 and x > 400):
            return 9

def runWithGraphics():
    window = GraphWin('Tic-Tac-Toe', 600, 700)
    initializeBoard(window)
    plain_game = PlainGame()
    currentGame = GraphicGame(plain_game, window)


    for i in range(9):
        currentGame.plain_game.printRoundInfo()
        currentGame.plain_game.printGrid()
        while True:
            try:
                #playerGridChoice = input('Player ' + str(((currentGame.roundNum%2)+1)) + ', pick a number.\n')
                choiceCoordinates = currentGame.window.getMouse()
                playerGridChoice = str(translateCoordinatesToGrid(choiceCoordinates))
                if isValidGridChoice(playerGridChoice, currentGame.plain_game.grid): # Consider rewriting this function to take in an int
                    break
                else:
                    raise ValueError
            except: # Consider refactoring/restructuring
                print('Invalid choice, please pick an available number.')
        currentGame.plain_game.update(playerGridChoice)
        currentGame.updateWindow(playerGridChoice)
        if currentGame.plain_game.hasAWin(playerGridChoice):
            loser = currentGame.plain_game.getCurrentPlayerNum()
            if loser == '1':
                currentGame.plain_game.winner = '2'
            else:
                currentGame.plain_game.winner = '1'
            break
    displayWinScreen(currentGame.plain_game)


    window.getMouse()
    window.close()


class Grid:
    def __init__(self, sym):
        self.sym = sym

    def __str__(self):
        return str(self.sym)

class Row:
    def __init__(self):
        self.lst = []

    def checkForWin(self):
        if self.lst[0].sym == self.lst[1].sym and self.lst[1].sym == self.lst[2].sym:
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

        self.roundNum = 1
        self.winner = None

    def printRoundInfo(self):
        print('===============INFO==============')
        print('Player 1: X\tPlayer 2: O')
        print('Round ' + str(self.roundNum) + ', Player ' + self.getCurrentPlayerNum() + '\'s turn')
        print('=================================')

    def printGrid(self):
        print('=================================')
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
        if self.roundNum % 2 == 0:
            return '2'
        else:
            return '1'

    def getCurrentToken(self):
        if self.getCurrentPlayerNum() == '1':
            return 'O'
        else:
            return 'X'

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
    print('===========END OF GAME===========')
    if game.winner is not None:
        print('The winner is Player ' + game.winner + '!')
    else:
        print('The game is a draw!')
    game.printGrid()
    print('=================================')

def runWithoutGraphics():
    print('Tic-Tac-Toe without graphics is starting, enjoy!')
    currentGame = PlainGame()
    for i in range(9):
        currentGame.printRoundInfo()
        currentGame.printGrid()
        while True:
            try:
                playerGridChoice = input('Player ' + str(((currentGame.roundNum%2)+1)) + ', pick a number.\n')
                if isValidGridChoice(playerGridChoice, currentGame.grid):
                    break
                else:
                    raise ValueError
            except: # Consider refactoring/restructuring
                print('Invalid choice, please pick an available number.')
        currentGame.update(playerGridChoice)
        if currentGame.hasAWin(playerGridChoice):
            loser = currentGame.getCurrentPlayerNum()
            if loser == '1':
                currentGame.winner = '2'
            else:
                currentGame.winner = '1'
            break
    displayWinScreen(currentGame)


def main():
    print('Tic-Tac-Toe is starting...\n')
    while True:
        try:
            choice = input('Would you like to play with graphics?\nY/N\n')
            if choice.lower() != 'y' and choice.lower() != 'n':
                raise ValueError
            else:
                break
        except:
            print('Sorry, please enter \'Y\' or \'N\'.')

    if choice.lower() == 'y':
        runWithGraphics()
    else:
        runWithoutGraphics()

if __name__ == '__main__':
    main()
