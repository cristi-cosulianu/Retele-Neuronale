import numpy as np

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
    matrix = np.zeros((3, 3))
    vector = np.zeros(3)
    if file.mode == 'r':
        content = file.readlines()
        for iterator in range(len(content)):
            line = content[iterator]
            
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

            matrix[iterator][0] = xFactor
            matrix[iterator][1] = yFactor
            matrix[iterator][2] = zFactor
            vector[iterator] = result
        
        return (matrix, vector)


            
def homeworkNumpy(filename):
    matrixVectorTuple = parseEcuations(filename)
    matrix = matrixVectorTuple[0]
    vector = matrixVectorTuple[1]

    if np.linalg.det(matrix) != 0:
        reversedMatrix = np.linalg.inv(matrix)
        return reversedMatrix.dot(vector)
    else: 
        return None

print(homeworkNumpy("HomeworkInput.txt"))