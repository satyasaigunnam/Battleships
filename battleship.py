"""
Battleship Project
Name:
Roll No:
"""

import battleship_tests as test

project = "Battleship" # don't edit this

### SIMULATION FUNCTIONS ###

from tkinter import *
import random

EMPTY_UNCLICKED = 1
SHIP_UNCLICKED = 2
EMPTY_CLICKED = 3
SHIP_CLICKED = 4


'''
makeModel(data)
Parameters: dict mapping strs to values
Returns: None
'''
def makeModel(data):
    data["rows"]=10
    data["cols"]=10
    data["boardsize"]=500
    data["celsize"]=50
    data["userboard"]=emptyGrid(data["rows"],data["cols"])
    data["computerboard"]=emptyGrid(data["rows"],data["cols"])
    data["computerboard"]=addShips(data["computerboard"],5)
    data["numberofships"]=5
    data["tempship"]= test.testShip()
    data["tempship"]=[]
    data["userships"]=0
    data["Winner"]=None
    data["max turns"]=50
    data["no of turns"]=0

    return data
    


'''
makeView(data, userCanvas, compCanvas)
Parameters: dict mapping strs to values ; Tkinter canvas ; Tkinter canvas
Returns: None
'''
def makeView(data, userCanvas, compCanvas):
    drawGrid(data,userCanvas,data["userboard"],True)
    drawGrid(data,compCanvas,data["computerboard"],False)
    drawShip(data,userCanvas,data["tempship"])
    drawGameOver(data,userCanvas)
    return


'''
keyPressed(data, events)
Parameters: dict mapping strs to values ; key event object
Returns: None
'''
def keyPressed(data, event):
    pass


'''
mousePressed(data, event, board)
Parameters: dict mapping strs to values ; mouse event object ; 2D list of ints
Returns: None
'''
def mousePressed(data, event, board):
    if data["Winner"]!=None:
        return None
    row,col=getClickedCell(data, event)
    if board=="user":
        clickUserBoard(data, row, col)
    if board=="comp":
        runGameTurn(data,row,col)
      




#### WEEK 1 ####

'''
emptyGrid(rows, cols)
Parameters: int ; int
Returns: 2D list of ints
'''
def emptyGrid(rows, cols):
    grid=[]
    for i in range(rows):
        n =[]
        for j in range(cols):
            n.append(EMPTY_UNCLICKED)
        grid.append(n)

    return grid

'''
createShip()
Parameters: no parameters
Returns: 2D list of ints
'''
def createShip():
    row = random.randint(1,8)
    column = random.randint(1,8)
    ramdomvalues = random.randint(0,1)
    if ramdomvalues == 0:
        ship=[[row-1,column],[row,column],[row+1,column]]
    else:
        ship=[[row,column-1],[row,column],[row,column+1]]


    return ship

'''
checkShip(grid, ship)
Parameters: 2D list of ints ; 2D list of ints
Returns: bool
'''
def checkShip(grid, ship):
    for i in ship:
        if grid [i [0]][i[1]] !=1:
            return False
    return True


'''
addShips(grid, numShips)
Parameters: 2D list of ints ; int
Returns: 2D list of ints
'''
def addShips(grid, numShips):
    h=0
    while h < numShips:
        c1 = createShip()
        c2 = checkShip(grid,c1)
        if c2 == True:
            for i in c1:
                grid [i[0]][i[1]]=SHIP_UNCLICKED
            h=h+1    
    return grid


'''
drawGrid(data, canvas, grid, showShips)
Parameters: dict mapping strs to values ; Tkinter canvas ; 2D list of ints ; bool
Returns: None
'''
def drawGrid(data, canvas, grid, showShips):
    for row in range(data["rows"]):
         for cols in range(data["cols"]):
            if grid[row][cols]==SHIP_UNCLICKED:
                if showShips==True:
                    canvas.create_rectangle(cols*data["celsize"],row*data["celsize"],(cols+1)*data["celsize"], (row+1)*data["celsize"], fill="yellow")
                else:
                    canvas.create_rectangle(cols*data["celsize"],row*data["celsize"],(cols+1)*data["celsize"], (row+1)*data["celsize"], fill="blue")
            elif grid[row][cols]==SHIP_CLICKED:
                canvas.create_rectangle(cols*data["celsize"],row*data["celsize"],(cols+1)*data["celsize"], (row+1)*data["celsize"], fill="red")
            elif grid[row][cols]==EMPTY_CLICKED:
                canvas.create_rectangle(cols*data["celsize"],row*data["celsize"],(cols+1)*data["celsize"], (row+1)*data["celsize"], fill="white")
            else:
                canvas.create_rectangle(cols*data["celsize"],row*data["celsize"],(cols+1)*data["celsize"], (row+1)*data["celsize"], fill="blue")

    return

### WEEK 2 ###

'''
isVertical(ship)
Parameters: 2D list of ints
Returns: bool
'''
def isVertical(ship):
    row=0
    if ship[row][1]==ship[row+1][1]==ship[row+2][1]:
        ship.sort()
        if ship[row+1][0]-ship[row][0]==1 and ship[row+2][0]-ship[row+1][0]==1:
            return True
    return False


'''
isHorizontal(ship)
Parameters: 2D list of ints
Returns: bool
'''
def isHorizontal(ship):
    row=0
    if ship[row][0]==ship[row+1][0]==ship[row+2][0]:
        ship.sort()
        if ship[row+1][1]-ship[row][1]==1 and ship[row+2][1]-ship[row+1][1]==1:
            return True
    return False
 


'''
getClickedCell(data, event)
Parameters: dict mapping strs to values ; mouse event object
Returns: list of ints
'''
def getClickedCell(data, event):
    d = data["celsize"]
    data=[int(event.y/d),int(event.x/d)]

    
    return  data 


'''
drawShip(data, canvas, ship)
Parameters: dict mapping strs to values ; Tkinter canvas; 2D list of ints
Returns: None
'''
def drawShip(data, canvas, ship):
    for i in ship:
        row=i[0]
        cols=i[1] 
        canvas.create_rectangle(cols*data["celsize"],row*data["celsize"],(cols+1)*data["celsize"], (row+1)*data["celsize"], fill="white")
    

    return
'''
shipIsValid(grid, ship)
Parameters: 2D list of ints ; 2D list of ints
Returns: bool
'''
def shipIsValid(grid, ship):
    if checkShip(grid,ship):
        if isVertical(ship)==True or isHorizontal(ship)==True:
      
          return True
    return False


'''
placeShip(data)
Parameters: dict mapping strs to values
Returns: None
'''
def placeShip(data):
    g=data["userboard"]
    if shipIsValid(g, data["tempship"]):
        for i in data["tempship"]:
            g[i[0]][i[1]]=SHIP_UNCLICKED
        data["userships"]=data["userships"]+1
    else:
        print("Ship is not Valid")
    data["tempship"]=[]
    return


'''
clickUserBoard(data, row, col)
Parameters: dict mapping strs to values ; int ; int
Returns: None
'''
def clickUserBoard(data, row, col):
    g=data["tempship"]
    if [row,col] in g or data["userships"]==5:
        return
    data["tempship"].append([row,col])
    if len(data["tempship"])==3:
        placeShip(data)
    if data["userships"]==5:
        print("You can start the game")


### WEEK 3 ###

'''
updateBoard(data, board, row, col, player)
Parameters: dict mapping strs to values ; 2D list of ints ; int ; int ; str
Returns: None
'''
def updateBoard(data, board, row, col, player):

    if  board[row][col]== SHIP_UNCLICKED:
        board[row][col]=SHIP_CLICKED
    elif board[row][col]==EMPTY_UNCLICKED:
        board[row][col]=EMPTY_CLICKED  
    
    if isGameOver(board)== True:
        data["Winner"] = player

         

    return


'''
runGameTurn(data, row, col)
Parameters: dict mapping strs to values ; int ; int
Returns: None
'''
def runGameTurn(data, row, col):
    i = data["computerboard"]
    u = data["userboard"]
    if i[row][col]==SHIP_CLICKED or i[row][col]==EMPTY_CLICKED:
        return
    else:
        updateBoard(data, i, row, col, "user")
    row,col=getComputerGuess(u)
    updateBoard(data, u, row, col, "comp")
    data["no of turns"]+=1
    if data["no of turns"]==data["max turns"]:
        data["Winner"]="draw"

    return
    


'''
getComputerGuess(board)
Parameters: 2D list of ints
Returns: list of ints
'''
def getComputerGuess(board):
    
    while True:
        row = random.randint(0,9)
        col = random.randint(0,9)
        if board[row][col]==SHIP_UNCLICKED or board[row][col]==EMPTY_UNCLICKED:
            return [row, col]
    


'''
isGameOver(board)
Parameters: 2D list of ints
Returns: bool
'''
def isGameOver(board):
    for i in range (len(board)):
        for j in range (len(board)):
            if board[i][j]==SHIP_UNCLICKED:
                return False
    return True
 

'''
drawGameOver(data, canvas)
Parameters: dict mapping strs to values ; Tkinter canvas
Returns: None
'''
def drawGameOver(data, canvas):
    if data["Winner"]=="user":
        canvas.create_text(300, 50, text="congratulations", fill="black", font=('Helvetica 15 bold'))
    elif data["Winner"]=="comp":
        canvas.create_text(300, 50, text="you lost", fill="black", font=('Helvetica 15 bold'))
    elif data["Winner"]=="draw":
        canvas.create_text(200, 200, text="Out of moves and reached Draw", font=('Arial',18,'bold italic'),anchor="center")

    return


### SIMULATION FRAMEWORK ###

from tkinter import *

def updateView(data, userCanvas, compCanvas):
    userCanvas.delete(ALL)
    compCanvas.delete(ALL)
    makeView(data, userCanvas, compCanvas)
    userCanvas.update()
    compCanvas.update()

def keyEventHandler(data, userCanvas, compCanvas, event):
    keyPressed(data, event)
    updateView(data, userCanvas, compCanvas)

def mouseEventHandler(data, userCanvas, compCanvas, event, board):
    mousePressed(data, event, board)
    updateView(data, userCanvas, compCanvas)

def runSimulation(w, h):
    data = { }
    makeModel(data)

    root = Tk()
    root.resizable(width=False, height=False) # prevents resizing window

    # We need two canvases - one for the user, one for the computer
    Label(root, text = "USER BOARD - click cells to place ships on your board.").pack()
    userCanvas = Canvas(root, width=w, height=h)
    userCanvas.configure(bd=0, highlightthickness=0)
    userCanvas.pack()

    compWindow = Toplevel(root)
    compWindow.resizable(width=False, height=False) # prevents resizing window
    Label(compWindow, text = "COMPUTER BOARD - click to make guesses. The computer will guess on your board.").pack()
    compCanvas = Canvas(compWindow, width=w, height=h)
    compCanvas.configure(bd=0, highlightthickness=0)
    compCanvas.pack()

    makeView(data, userCanvas, compCanvas)

    root.bind("<Key>", lambda event : keyEventHandler(data, userCanvas, compCanvas, event))
    compWindow.bind("<Key>", lambda event : keyEventHandler(data, userCanvas, compCanvas, event))
    userCanvas.bind("<Button-1>", lambda event : mouseEventHandler(data, userCanvas, compCanvas, event, "user"))
    compCanvas.bind("<Button-1>", lambda event : mouseEventHandler(data, userCanvas, compCanvas, event, "comp"))

    updateView(data, userCanvas, compCanvas)

    root.mainloop()


### RUN CODE ###

# This code runs the test cases to check your work
if __name__ == "__main__":

    ## Finally, run the simulation to test it manually ##
    runSimulation(500, 500)
    
