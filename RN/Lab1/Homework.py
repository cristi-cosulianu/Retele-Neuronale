def extractFactor(line):
    factor = 0
    sign = 1

    foundFactor = False

    for i in range(len(line)):
        char = line[i]
        if char == '-':
            sign = -1
        elif char in "0123456789":
            foundFactor = True
            factor = factor * 10 + int(char)
        elif char.isalpha():
            if (factor == 0) & (foundFactor == False):
                factor = 1
            return (line[i+1:], factor * sign, char)

    return (line, factor * sign, 'Equal')

def parseEcuations(filename):
    file = open(filename, 'r')
    matrix = []
    vector = []
    if file.mode == 'r':
        content = file.readlines()
        for line in content:
            line = line.replace(' ', '')
            
            xFactor = 0
            yFactor = 0
            zFactor = 0
            result = 0

            while line[0] != '=':
                factorTuple = extractFactor(line)
                line = factorTuple[0]
                factor = factorTuple[1]
                variable = factorTuple[2]

                if variable == 'x':
                    xFactor = factor
                elif variable == 'y':
                    yFactor = factor
                elif variable == 'z':
                    zFactor = factor
            
            factorTuple = extractFactor(line)
            result = factorTuple[1]

            matrix.append([xFactor, yFactor, zFactor])
            vector.append(result)
        
        return (matrix, vector)

def iterateDetIndex(j, matrix):
    j += 1
    if j >= len(matrix):
        j = j - len(matrix)
    return j

def calculateDeterminant(matrix):
    determinant = 0
    matrixSize = len(matrix)
    if matrixSize == 2:
        matrixSize -= 1 
    for i in range(matrixSize):
        j = i
        product = 1
        for column in range(len(matrix)):
            product *= matrix[j][column]
            j = iterateDetIndex(j, matrix)
        determinant += product

        j = i
        product = 1
        for column in range(len(matrix)-1, -1, -1):
            product *= matrix[j][column]
            j = iterateDetIndex(j, matrix)
        determinant += product * (-1)

    return determinant
        

def extractColumn(matrix, column):
    columnElements = []
    for line in matrix:
        columnElements.append(line[column])
    return columnElements

def copyOldMatrix(matrix):
    newMatrix = []
    for line in matrix:
        newLine = []
        for column in line:
            newColumn = column
            newLine.append(newColumn)
        newMatrix.append(newLine)
    return newMatrix

def removeLineAndColumn(matrix, line, column):
    minorMatrix = copyOldMatrix(matrix)
    del(minorMatrix[line])
    for line in minorMatrix:
        del(line[column])
    return minorMatrix

def transposeMatrix(matrix):
    transposedMatrix = []
    for column in range(len(matrix)):
        transposedMatrix.append(extractColumn(matrix, column))
    return transposedMatrix


def createAdjuncMatrix(matrix):
    transposedMatrix = transposeMatrix(matrix)
    adjunctMatrix = []
    for line in range(len(transposedMatrix)):
        adjuncLine = []
        for column in range(len(transposedMatrix)):
            minorMatrix = removeLineAndColumn(transposedMatrix, line, column)
            minorDeterminant = calculateDeterminant(minorMatrix)
            if (line + column) % 2 != 0:
                minorDeterminant *= (-1)
            adjuncLine.append(minorDeterminant)
        adjunctMatrix.append(adjuncLine)
    return adjunctMatrix
                
def reverseMatrix(matrixDeterminant, adjunctMatrix):
    for i in range(len(adjunctMatrix)):
        line = adjunctMatrix[i]
        for j in range(len(adjunctMatrix[i])):
            adjunctMatrix[i][j] = adjunctMatrix[i][j] * (float(1) / matrixDeterminant)
    return adjunctMatrix

def multiplyMatrixWitVector(matrix, vector):
    result = [0] * len(matrix)
    for lineIterator in range(len(matrix)):
        line = matrix[lineIterator]
        for columnIterator in range(len(line)):
            result[lineIterator] += matrix[lineIterator][columnIterator] * vector[columnIterator]
    return result
            
def homework(filename):
    matrixVectorTuple = parseEcuations(filename)
    matrix = matrixVectorTuple[0]
    vector = matrixVectorTuple[1]

    matrixDeterminant = calculateDeterminant(matrix)
    if matrixDeterminant != 0:
        adjunctMatrix = createAdjuncMatrix(matrix)
        reversedMatrix = reverseMatrix(matrixDeterminant, adjunctMatrix)

        result = multiplyMatrixWitVector(reversedMatrix, vector)
        return result
    else:
        return "No solution!"

print(homework("HomeworkInput.txt"))

