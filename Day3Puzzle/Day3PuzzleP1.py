from math import sqrt
from math import ceil

def partOne(input):

    quadraticSquare = sqrt(input)
    base = int(ceil(quadraticSquare)) #We need the smallest matrix wich includes this number
    quadraticEdge = base*base

    step = base - 1 #This step shows the value by which the edges diff from each other
    listEdges = [quadraticEdge,quadraticEdge-step,quadraticEdge-step*2,quadraticEdge-step*3]

    stepToCentralRow = base/2 - findClosesEdge(listEdges,input)

    if(base % 2 != 0): #There is a difference in the matrix if the base number is odd because 1 is not exactly at the center of the matrix
        totalNrOfSteps = stepToCentralRow + base / 2
    else:
        totalNrOfSteps = stepToCentralRow + base / 2 - 1

    print(totalNrOfSteps)


def findClosesEdge(edges,input):
    diff = abs(edges[0] - input)
    for x in edges:
        if diff > abs(x - input):
            diff = abs(x - input)
    return diff



partOne(325489)
