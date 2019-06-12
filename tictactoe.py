from graphics import *

class PlainGame:
    def __init__(self):
        self.grid1 = '1'
        self.grid2 = '2'
        self.grid3 = '3'
        self.grid4 = '4'
        self.grid5 = '5'
        self.grid6 = '6'
        self.grid7 = '7'
        self.grid8 = '8'
        self.grid9 = '9'
        self.roundNum = 0

    def printGrid(self):
        print('=================================')
        print('Player 1: X\tPlayer 2: O')
        print('Round ' + str(self.roundNum + 1) + ', Player ' + str(((self.roundNum%2)+1)) + '\'s turn')
        print('         |         |         ')
        print('    ' + self.grid1 + '    |    ' + self.grid2 + '    |    ' + self.grid3 + '    ')
        print('_________|_________|_________')
        print('         |         |         ')
        print('    ' + self.grid4 + '    |    ' + self.grid5 + '    |    ' + self.grid6 + '    ')
        print('_________|_________|_________')
        print('         |         |         ')
        print('    ' + self.grid7 + '    |    ' + self.grid8 + '    |    ' + self.grid9 + '    ')
        print('         |         |         ')
        print('=================================')


def runWithGraphics():
    print('Tic-Tac-Toe with graphics is starting, enjoy!')
    # Run game with graphics

def runWithoutGraphics():
    print('Tic-Tac-Toe without graphics is starting, enjoy!')
    currentgame = PlainGame()
    for i in range(9):
        currentgame.printGrid()
        playerGridChoice = input('Player ' + str(((currentgame.roundNum%2)+1)) + ', pick a number.')

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