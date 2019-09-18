#################################################
# Hw5
# Your andrewID:
# Your section: 
#################################################

#################################################
# Hw5 problems
#################################################

#### #1: COLLABORATIVE: removeRowAndCol ####
#Collaborators: (list andrewIDs) 

def nondestructiveRemoveRowAndCol(lst, row, col):
    rowList = lst[:row] + lst[(row+1) :] #contrusct a new list with remaining rows
    rows = len(rowList)
    colList = []
    for row in range(rows):
        colList += [rowList[row][:col] + rowList[row][(col+1) :]]
    return colList

def destructiveRemoveRowAndCol(lst, row, col):
    lst.pop(row)
    rows = len(lst)
    for row in range(rows):
        lst[row].pop(col)

#### #2: COLLABORATIVE: wordSearchWithWildcards(board, word) ####
#Collaborators: (list andrewIDs)

def wordSearchWithWildcards(board, word):
    return

#### #3: Sudoku Logic ####

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

######################################################################
# GRAPHICS/ANIMATION PROBLEMS
# ignore_rest
# The autograder will ignore all code below here
# (But we won't!  This is where all tkinter problems go!)
######################################################################
newinput = [ ([0] * (3**2)) for i in range(3**2)]
print(newinput)
from tkinter import *

#### #4: Sudoku Animation ####

#this helper function works for translate GRB code into colors
def rgbString(red, green, blue):
    return "#%02x%02x%02x" % (red, green, blue)

def winGame(board):
    for row in range(len(board)):
        for col in range(len(board)):
            if board[row][col] == 0:
                return False
            else:
                continue
    return True

#Draw N*N rectangles
def drawBoard(canvas, data):
    margin = 20
    n = len(data.board)

    colorBackground = [
             [rgbString(226, 225, 228), rgbString(17, 101, 154), rgbString(122, 115, 116)],
             [rgbString(210, 53, 125), rgbString(173, 101, 152), rgbString(32, 137, 77)],
             [rgbString(26, 148, 188), rgbString(205, 98, 39),rgbString(128, 118, 163),]]
    colorHighlight = [rgbString(232, 176, 4)]
    colorInput = [rgbString(192, 44, 56)]

    # draw different colors for each blocks
    blockN = int(n ** 0.5)
    for row in range(blockN):
        for col in range(blockN):
            blockLeftX = margin + col * data.cellSize * blockN
            blockLeftY = margin + row * data.cellSize * blockN
            blockrightX = blockLeftX + data.cellSize * blockN
            blockrightY = blockLeftY + data.cellSize * blockN
            canvas.create_rectangle((blockLeftX, blockLeftY), (blockrightX, blockrightY),
                                    fill = colorBackground[row][col])

    #calculate points for each rectangle then draw basic rectangles
    for row in range(len(data.board)):
        for col in range(len(data.board[row])):
            leftX = margin + col * data.cellSize
            leftY = margin + row * data.cellSize
            rightX = leftX + data.cellSize
            rightY = leftY + data.cellSize
            canvas.create_rectangle((leftX, leftY), (rightX, rightY))
            if [row, col] == data.highlight:
                canvas.create_rectangle((leftX, leftY), (rightX, rightY), fill = colorHighlight)

            if data.board[row][col] == 0:
                continue
            elif data.newinput[row][col] == 1:
                canvas.create_text((leftX + 0.5 * data.cellSize, leftY + 0.5 * data.cellSize),
                                   font='Helvetica 26 bold', text=data.board[row][col], fill = colorInput)
            else:
                canvas.create_text((leftX + 0.5 * data.cellSize, leftY + 0.5 * data.cellSize),
                               font='Helvetica 26', text=data.board[row][col])

#draw twice the block to ensure the outline of block show correctly
    for row in range(blockN):
        for col in range(blockN):
            blockLeftX = margin + col * data.cellSize * blockN
            blockLeftY = margin + row * data.cellSize * blockN
            blockrightX = blockLeftX + data.cellSize * blockN
            blockrightY = blockLeftY + data.cellSize * blockN
            canvas.create_rectangle((blockLeftX, blockLeftY), (blockrightX, blockrightY),
                                    width = 5)

    if winGame(data.board):
        canvas.create_text((data.width / 2, data.height / 2), text = 'You Win!',
                           font = 'Helvetica 60', fill = 'yellow')



def init(data):
    data.board = [
  [ 1, 2, 3, 4, 5, 6, 7, 8, 9],
  [ 5, 0, 8, 1, 3, 9, 6, 2, 4],
  [ 4, 9, 6, 8, 7, 2, 1, 5, 3],
  [ 9, 5, 2, 3, 8, 1, 4, 6, 7],
  [ 6, 4, 1, 2, 9, 7, 8, 3, 5],
  [ 3, 8, 7, 5, 6, 4, 0, 9, 1],
  [ 7, 1, 9, 6, 2, 3, 5, 4, 8],
  [ 8, 6, 4, 9, 1, 5, 3, 7, 2],
  [ 2, 3, 5, 7, 4, 8, 9, 1, 6]
]
    import copy
    data.originalBoard = copy.deepcopy(data.board)
    n = len(data.board)
    margin = 20
    data.cellWidth = (data.width - 2 * margin) // n
    data.cellHeigth = (data.height - 2 * margin) // n #assume always get N*N data input
    data.cellSize = min(data.cellWidth, data.cellHeigth)

    #highlight cell
    data.highlight = [0,0]
    data.newinput = [ ([0]* n**2)for i in range(n**2)]

def mousePressed(event, data):
    if not winGame(data.board):
        margin = 20
        row = (event.y - margin) // data.cellSize
        col = (event.x - margin) // data.cellSize
        if row >= 0 and row <= len(data.board) and col >= 0 and col <= len(data.board):
            data.highlight = [row, col]
        else:
            data.highlight = [0, 0]



def keyPressed(event, data):
    if not winGame(data.board):
        n = len(data.board)
        row = data.highlight[0]
        col = data.highlight[1]
    #control keypress move
        if event.keysym == "Up":
            row -= 1
            if row < 0: row = n-1
        elif event.keysym == "Down":
            row += 1
            if row >= n: row = 0
        elif event.keysym == "Right":
            col += 1
            if col >= n: col = 0
        elif event.keysym == "Left":
            col -= 1
            if col < 0: col = n-1
        data.highlight = [row, col]

    #control keypress input values
        legalValues = [str(i) for i in range(n ** 2 + 1)]
        import copy
        if data.originalBoard[row][col] == 0: #cannot change original board
            if event.char in legalValues:
                newBoard = copy.deepcopy(data.board)
                newBoard[row][col] = int(event.char)
                if isLegalSudoku(newBoard):
                    data.newinput[row][col] = 1
                    data.board = newBoard
            elif event.keysym == 'BackSpace':
                data.board[row][col] = 0

def redrawAll(canvas, data):
    drawBoard(canvas, data)

def runSudoku(width=300, height=300):
    def redrawAllWrapper(canvas, data):
        canvas.delete(ALL)
        canvas.create_rectangle(0, 0, data.width, data.height,
                                fill='white', width=0)
        redrawAll(canvas, data)
        canvas.update()    

    def mousePressedWrapper(event, canvas, data):
        mousePressed(event, data)
        redrawAllWrapper(canvas, data)

    def keyPressedWrapper(event, canvas, data):
        keyPressed(event, data)
        redrawAllWrapper(canvas, data)

    # Set up data and call init
    class Struct(object): pass
    data = Struct()
    data.width = width
    data.height = height
    root = Tk()
    root.resizable(width=False, height=False) # prevents resizing window
    init(data)
    # create the root and the canvas
    canvas = Canvas(root, width=data.width, height=data.height)
    canvas.configure(bd=0, highlightthickness=0)
    canvas.pack()
    # set up events
    root.bind("<Button-1>", lambda event:
                            mousePressedWrapper(event, canvas, data))
    root.bind("<Key>", lambda event:
                            keyPressedWrapper(event, canvas, data))
    redrawAll(canvas, data)
    # and launch the app
    root.mainloop()  # blocks until window is closed

#### Bonus: Sokoban Animation ####
'''
def initSokoban(data):
    pass

def mousePressedSokoban(event, data):
    pass

def keyPressedSokoban(event, data):
    pass

def redrawAllSokoban(canvas, data):
    pass

def runSokoban(width=300, height=300):
    def redrawAllWrapper(canvas, data):
        canvas.delete(ALL)
        canvas.create_rectangle(0, 0, data.width, data.height,
                                fill='white', width=0)
        redrawAllSokoban(canvas, data)
        canvas.update()    

    def mousePressedWrapper(event, canvas, data):
        mousePressedSokoban(event, data)
        redrawAllWrapper(canvas, data)

    def keyPressedWrapper(event, canvas, data):
        keyPressedSokoban(event, data)
        redrawAllWrapper(canvas, data)

    # Set up data and call init
    class Struct(object): pass
    data = Struct()
    data.width = width
    data.height = height
    root = Tk()
    root.resizable(width=False, height=False) # prevents resizing window
    initSokoban(data)
    # create the root and the canvas
    canvas = Canvas(root, width=data.width, height=data.height)
    canvas.configure(bd=0, highlightthickness=0)
    canvas.pack()
    # set up events
    root.bind("<Button-1>", lambda event:
                            mousePressedWrapper(event, canvas, data))
    root.bind("<Key>", lambda event:
                            keyPressedWrapper(event, canvas, data))
    redrawAllSokoban(canvas, data)
    # and launch the app
    root.mainloop()  # blocks until window is closed
'''
#################################################
# Hw5 Test Functions
# NOTE: starting this week, we will not provide any tests in the test functions.
# You need to write your own tests!
#################################################
# This is a test case for a non-destructive function.
# The input list and output list
lst = [ [ 2, 3, 4, 5],
        [ 8, 7, 6, 5],
        [ 0, 1, 2, 3] ]
result = [ [ 2, 3, 5],
           [ 0, 1, 3] ]

def testNondestructiveRemoveRowAndCol():
    print("Testing nondestructiveRemoveRowAndCol(): ", end = '')
    import copy
    lstCopy = copy.deepcopy(lst)
    assert(nondestructiveRemoveRowAndCol(lst, 1, 2) == result)
    assert(lst == lstCopy)
    print('Passed.')
    return

def testDestructiveRemoveRowAndCol():
    print("Testing destructiveRemoveRowAndCol(): ", end='')
    assert (destructiveRemoveRowAndCol(lst, 1, 2) == None)
    assert (lst == result), "input list should be changed"
    print('Passed.')
    return

def testWordSearchWithWildcards():
    print("Write your own tests for wordSearchWithWildcards!")

value1 = [1,3,3,4]
value2 = [1,5,7,9]
value3 = [1,2]
value4 = [0,0,0,0,0,0,0,0,0]
value5 = [ 5, 3, 1, 0, 7, 0, 0, 0, 0 ]
value6 = [ -6, 0, 0, 1, 9, 5, 0, 0, 0 ]

def testAreLegalValues():
    print ("Testing areLegalValues(): ", end = '')
    assert (areLegalValues(value1, 2) == False)
    assert (areLegalValues(value2, 2) == False)
    assert (areLegalValues(value3, 2) == False)
    assert (areLegalValues(value4, 3) == True)
    assert (areLegalValues(value5, 3) == True)
    assert (areLegalValues(value6, 3) == False)
    assert (value1 == [1,3,3,4]) #test if it's non-desctructive
    print ('Passed.')
    return

testRowBoard = [
  [ 5, 3, 0, 0, 7, 0, 0, 0, 10 ], #not legal row
  [ 6, 0, 0, 1, 9, 5, 0, 0, 0 ],
  [ 9, 9, 8, 0, 0, 0, 0, 6, 0 ],#not legal row
  [ 8, 0, 0, 0, 6, 0, 0, 0, 3 ],
  [ 4, 0, 0, 8, 0, 3, 0, 0, 1 ],
  [ 7, 0, 0, 0, 2, 0, 0, 0, 6 ],
  [ 0, 6, 0, 0, 0, 0, 2, 8, 0 ],
  [ 0, 0, 0, 4, 1, 9, 0, 0, 5 ],
  [ 0, 0, 0, 0, 8, 0, 0, 7, 9 ]
]

def testIsLegalRow():
    print ("Testing isLegalRow(): ", end = '')
    assert (isLegalRow(testRowBoard, 0 ,3) == False)
    assert (isLegalRow(testRowBoard, 8, 3) == True)
    assert (isLegalRow(testRowBoard, 2, 3) == False)
    assert (testRowBoard == [
  [ 5, 3, 0, 0, 7, 0, 0, 0, 10 ],
  [ 6, 0, 0, 1, 9, 5, 0, 0, 0 ],
  [ 9, 9, 8, 0, 0, 0, 0, 6, 0 ],
  [ 8, 0, 0, 0, 6, 0, 0, 0, 3 ],
  [ 4, 0, 0, 8, 0, 3, 0, 0, 1 ],
  [ 7, 0, 0, 0, 2, 0, 0, 0, 6 ],
  [ 0, 6, 0, 0, 0, 0, 2, 8, 0 ],
  [ 0, 0, 0, 4, 1, 9, 0, 0, 5 ],
  [ 0, 0, 0, 0, 8, 0, 0, 7, 9 ]]) # test non-destructive
    print ('Passed.')
    return

#first, second and fourth cols are not legal
testColBoard = [
  [ 5, -3, 0, 1, 7, 0, 0, 0, 0 ],
  [ 6, 0, 0, 1, 9, 5, 0, 0, 0 ],
  [ 0, 9, 8, 0, 0, 0, 0, 6, 0 ],
  [ 18, 0, 0, 0, 6, 0, 0, 0, 3 ],
  [ 4, 0, 0, 8, 0, 3, 0, 0, 1 ],
  [ 7, 0, 0, 0, 2, 0, 0, 0, 6 ],
  [ 0, 6, 0, 0, 0, 0, 2, 8, 0 ],
  [ 0, 0, 0, 4, 1, 9, 0, 0, 5 ],
  [ 0, 0, 0, 0, 8, 0, 0, 7, 9 ]
]

def testIsLegalCol():
    print("Testing isLegalCol(): ", end = '')
    assert (isLegalCol(testColBoard, 0, 3) == False)
    assert (isLegalCol(testColBoard, 1, 3) == False)
    assert (isLegalCol(testColBoard, 2, 3) == True)
    assert (isLegalCol(testColBoard, 3, 3) == False)
    print('Passed.')
    return

testBlockBoard = [
  [ 5, 3, 3, 10, 7, 0, 0, 0, 0 ],
  [ 6, 0, 0, 1, 9, 5, 0, 0, 0 ],
  [ 0, 9, 8, 0, 0, 0, 0, 6, 0 ],
  [ 8, 0, 0, 0, 6, 0, 0, 0, 3 ],
  [ 4, 0, 0, 8, 0, 3, 0, 0, 1 ],
  [ 7, 0, 0, 0, 2, 0, 0, 0, 6 ],
  [ 0, 6, 0, 0, 0, 0, 2, 8, 0 ],
  [ 0, 0, 0, 4, 1, 9, 0, 0, 5 ],
  [ 0, 0, 0, 0, 8, 0, 0, 7, 9 ]
]

def testIsLegalBlock():
    print("Testing isLegalBlock(): ", end = '')
    assert (isLegalBlock(testBlockBoard, 0, 3) == False)
    assert (isLegalBlock(testBlockBoard, 1, 3) == False)
    assert (isLegalBlock(testBlockBoard, 8, 3) == True)
    print('Passed.')
    return

testBoard1 = [
  [ 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
  [ 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
  [ 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
  [ 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
  [ 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
  [ 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
  [ 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
  [ 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
  [ 0, 0, 0, 0, 0, 0, 0, 0, 0 ]]

testBoard2 = [
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

testBoard3 = [
  [ 5, 3, 3, 0, 7, 0, 0, 0, 0 ],
  [ 6, 0, 0, 1, 9, 5, 0, 0, 0 ],
  [ 0, 9, 8, 0, 0, 0, 10, 6, 0 ],
  [ 8, 0, 0, 0, 6, 0, 0, 0, 3 ],
  [ 4, 0, 0, 8, 0, 3, 0, 0, 1 ],
  [ 7, 0, 0, 0, 2, 0, 0, 0, 6 ],
  [ 0, 6, 0, 0, 0, 0, 2, 8, 0 ],
  [ 0, 0, 0, 4, 1, 9, 0, 0, 5 ],
  [ 0, 0, 0, 0, 8, 0, 0, 7, 9 ]
]

testBoard4 = [
  [ 1, 2, 3, 4, 5, 6, 7, 8, 9],
  [ 5, 0, 8, 1, 3, 9, 6, 2, 4],
  [ 4, 9, 6, 8, 7, 2, 1, 5, 3],
  [ 9, 5, 2, 3, 8, 1, 4, 6, 7],
  [ 6, 4, 1, 2, 9, 7, 8, 3, 5],
  [ 3, 8, 7, 5, 6, 4, 3, 9, 1],
  [ 7, 1, 9, 6, 2, 3, 5, 4, 8],
  [ 8, 6, 4, 9, 1, 5, 3, 7, 2],
  [ 2, 3, 5, 7, 4, 8, 9, 1, 6]
]
def testIsLegalSudoku():
    print("Testing isLegalSudoku(): ", end = '')
    assert (isLegalSudoku(testBoard1) == True)
    assert (isLegalSudoku(testBoard2) == True)
    assert (isLegalSudoku(testBoard3) == False)
    assert (isLegalSudoku(testBoard4) == False)
    print('Passed.')
    return

def testSudokuAnimation():
    print("Running Sudoku Animation...", end="")
    # Feel free to change the width and height!
    width = 500
    height = 500
    runSudoku(width, height)
    print("Done!")

def testSokobanAnimation():
    print("Running Sokoban Animation...", end="")
    # Feel free to change the width and height!
    width = 500
    height = 500
    runSokoban(width, height)
    print("Done!")

#################################################
# Hw5 Main
#################################################

def testAll():
    testNondestructiveRemoveRowAndCol()
    testDestructiveRemoveRowAndCol()
    testWordSearchWithWildcards()
    testAreLegalValues()
    testIsLegalRow()
    testIsLegalCol()
    testIsLegalBlock()
    testIsLegalSudoku()
    testSudokuAnimation()
    #testSokobanAnimation() # this is bonus- un-comment if you want to try!

def main():
    testAll()

if __name__ == '__main__':
    main()