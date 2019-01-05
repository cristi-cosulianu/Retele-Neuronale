import copy, numpy as np

bigValue = 99999999999

class Node:
    def __init__(self, gameBoard, cost, states):
        self.gameBoard = gameBoard
        self.cost = cost
        self.states = states

class Stack:
    def __init__(self):
        self.items = []

    def __init__(self, items):
        self.items = items

    def __repr__(self):
        string = "["
        for i in range(len(self.items)):
            string += str(self.items[i]) + " "
        string += "]"
        return string

    def push(self, item):
        self.items.append(item)
        
    def top(self):
        if(len(self.items) > 0):
            return self.items[len(self.items) - 1]
        else: 
            return bigValue

    def pop(self):
        if(len(self.items) > 0):
            return self.items.pop()
        else: 
            return None

    def content(self):
        itemsCopy = self.items.copy()
        return itemsCopy

    def is_empty(self):
        return (self.items == [])

def copyState(state):
    newState = []
    for stack in state:
        newStack = Stack(stack.content())
        newState.append(newStack)
    return newState


def initGameBoard(numOfDisks, numOfRods, rodPosition):
    gameBoard = []
    for i in range(numOfRods):
        gameBoard.append(Stack([]))
    for i in range(numOfDisks):
        gameBoard[rodPosition - 1].push(numOfDisks - i)
    return gameBoard

def resetGameBoard(listOfStates):
    return listOfStates[0]

def resetListOfStates(gameBoard):
    newListOfStates = [gameBoard]
    return newListOfStates

def statesAreEqual(firstState, secondState):
    numOfRods = len(firstState)
    for rod in range(numOfRods):
        if (firstState[rod].content() != secondState[rod].content()):
            return False
    return True

def notInFinalState(gameBoard, numOfRods, numOfDisks):
    for i in range(2, numOfRods):
        finalGameBoard = initGameBoard(numOfDisks,numOfRods, i)
        if (statesAreEqual(gameBoard, finalGameBoard)):
            return False
    return True

def findPossibleMoves(gameBoard):
    possibleMoves = []
    top = []
    for stack in gameBoard:
        top.append(stack.top())
    for fromTower in range(len(top)):
        for toTower in range(len(top)):
            if (fromTower != toTower):
                if fromTower != bigValue and top[fromTower] < top[toTower]:
                    possibleMoves.append([fromTower,toTower])
    return possibleMoves

def applyMove(gameBoard, chosenMove):
    boardCopy = copyState(gameBoard)
    disk = boardCopy[chosenMove[0]].pop()
    if (disk != None):
        boardCopy[chosenMove[1]].push(disk)
    return boardCopy

def isCancelingLastMove(newGameBoard, listOfStates):
    if len(listOfStates) > 2 and statesAreEqual(newGameBoard, listOfStates[-2]):
        return True
    return False

def isRepeating(newGameBoard, listOfStates):
    for state in listOfStates:
        if statesAreEqual(state, newGameBoard):
            return True
    return False

def towerOfHanoi(gameBoard, numOfDisks, numOfRods):
    # [0] -> Current game state.
    # [1] -> The cost to reach the current game state.
    # [2] -> The states to reach the current game state.  
    currentNode = Node(copyState(gameBoard), 0, [])

    # A tail of nodes.
    tail = []
    tail.append(currentNode)
    while(notInFinalState(currentNode.gameBoard, numOfRods, numOfDisks)):
        # print(currentNode.gameBoard)
        possibleMoves = findPossibleMoves(currentNode.gameBoard)
        for move in possibleMoves:
            newGameBoard = applyMove(currentNode.gameBoard, move)
            if not isRepeating(newGameBoard, currentNode.states) and len(currentNode.states) < (2**numOfDisks - 1) * 1.3:
                states = copy.deepcopy(currentNode.states)
                states.append(newGameBoard)
                newNode = Node(newGameBoard, currentNode.cost + 1, states)
                tail.append(newNode)

        # Find node with the minimum cost.
        argmin = np.argmin([state.cost for state in tail])
        # Update current node.
        currentNode = tail[argmin]
        # Remove node from tail.
        tail.pop(argmin)

    return currentNode.states


def main():
    numOfDisks = int(input("Insert number of disks: "))
    numOfRods = int(input("Insert number of rods: "))
    gameBoard = initGameBoard(numOfDisks, numOfRods, 1)
    listOfStates = towerOfHanoi(gameBoard, numOfDisks, numOfRods)
    print("\n\n")
    print("I FOUND AN SOLUTION!")
    print("\n\n")
    for state in listOfStates:
        print(state)

main()