board = {
    '7': ' ' , '8': ' ' , '9': ' ' ,
    '4': ' ' , '5': ' ' , '6': ' ' ,
    '1': ' ' , '2': ' ' , '3': ' ' 
}

keys = []

def displayBoard(board):
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['1'] + '|' + board['2'] + '|' + board['3'])

displayBoard(board)

def play(): 
    move = "x"
    count = 0

    for i in range(10):
        displayBoard(board)
        print("your turn" + move + " where do you want to go? ")

