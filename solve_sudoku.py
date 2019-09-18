###########################
#hw10
###########################

### Sudoku Logic ####

def areLegalValues(values,n):
    length = len(values)
    compareList = [i+1 for i in range(n**2)]
    if length == n**2:
        for i in range(length):
            value = values[i]
            if value == 0:
                continue
            elif value >0:
                if value in compareList:
                    compareList.remove(value)
                else:
                    return False
            else:
                return False
        return True
    else:
        return False

def isLegalRow(board, row, n):
    testRow = board[row]
    if areLegalValues(testRow, n):
        return True
    else:
        return False

def isLegalCol(board, col, n):
    testCol = []
    rows = len(board)
    for row in range(rows):
        testCol.append(board[row][col])
    if areLegalValues(testCol, n):
        return True
    else:
        return False

def isLegalBlock(board, block, n):
    testBlock = []
    startRow = (block // n) * n
    startCol = (block % n ) * n
    for i in range(n):
        testBlock += board[startRow + i][startCol: startCol + n]
    if areLegalValues(testBlock, n):
        return True
    else:
        return False

def isLegalSudoku(board):
    length = int(len(board) ** 0.5)
    for i in range(len(board)):
        if not isLegalRow(board, i, length):
            return False
    for i in range(len(board)):
        if not isLegalCol(board, i, length):
            return False
    for i in range(len(board)):
        if not isLegalBlock(board, i, length):
            return False
    return True

def winGame(board):
    for row in range(len(board)):
        for col in range(len(board)):
            if board[row][col] == 0:
                return False
            else:
                continue
    return True

#find the zero cell
def findZeroCell(board):
    for row in range(len(board)):
        for col in range(len(board)):
            if board[row][col] == 0:
                return [row, col]
            else:
                continue
    return None

#given a zero cell with row and col number, try numbers to see if it's legal
def isValid(board, cell, number):
    cellRow = cell[0]
    cellCol = cell[1]
    board[cellRow][cellCol] = number
    if isLegalSudoku(board):
        return True
    else:
        return False

def solveSudoku(board):
    if isLegalSudoku(board) and winGame(board):
        #base case
        return board
    else:
        #recursive case
        cell = findZeroCell(board)
        row = cell[0]
        col = cell[1]
        for number in range(1, len(board)+1):
            if isValid(board, cell, number):
                board[row][col] = number
                tmpSolution = solveSudoku(board)
                if tmpSolution != None:
                    return tmpSolution
        board[row][col] = 0
        return None

board1 = [
              [ 5, 3, 0, 0, 7, 0, 0, 0, 0 ],
              [ 6, 0, 0, 1, 9, 5, 0, 0, 0 ],
              [ 0, 9, 8, 0, 0, 0, 0, 6, 0 ],
              [ 8, 0, 0, 0, 6, 0, 0, 0, 3 ],
              [ 4, 0, 0, 8, 0, 3, 0, 0, 1 ],
              [ 7, 0, 0, 0, 2, 0, 0, 0, 6 ],
              [ 0, 6, 0, 0, 0, 0, 2, 8, 0 ],
              [ 0, 0, 0, 4, 1, 9, 0, 0, 5 ],
              [ 0, 0, 0, 0, 8, 0, 0, 7, 9 ]
            ]

print(solveSudoku(board1))

if __name__ == '__main__':
    main()
