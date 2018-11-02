# [0][0] - vectorul pentru prima imagine
# [1][0] - label-ul corect pentru acea imagine

import cPickle, gzip, numpy

class Perceptron:
    def __init__(self, weightsLength):
        self.weights = [0] * numberOfWeights()
        self.bias = 0

def numberOfWeights():
    return 784

def learnigRate():
    return 0.1

def getTrainSet():
    f = gzip.open('mnist.pkl.gz', 'rb')
    train_set, valid_set, test_set = cPickle.load(f)
    f.close()
    images = train_set[0]
    labels = train_set[1]
    return images, labels

def getValidSet():
    f = gzip.open('mnist.pkl.gz', 'rb')
    train_set, valid_set, test_set = cPickle.load(f)
    f.close()
    return valid_set

def getTestSet():
    f = gzip.open('mnist.pkl.gz', 'rb')
    train_set, valid_set, test_set = cPickle.load(f)
    f.close()
    return test_set

def createPerceptrons(length):
    listOfPerceptrons = []
    for iterator in range(length):
        perceptron = Perceptron(numberOfWeights())
        listOfPerceptrons.append(perceptron)
    return listOfPerceptrons

def initializeTargetLabel(label, digit):
    if label == digit:
        return 1
    else:
        return 0

def weightsSum(perceptron, image):
    sum = 0
    weights = perceptron.weights
    bias = perceptron.bias
    for iterator in range(len(weights)):
        sum += weights[iterator] * image[iterator]
    sum += bias
    return sum
        
def activation(netInput):
    if netInput > 0:
        return 1
    else:
        return 0

def adjustWeights(perceptron, image, targetLabel, output):
    for iterator in range(len(perceptron.weights)):
        perceptron.weights[iterator] += (targetLabel - output) * image[iterator] * learnigRate()

def adjustBias(perceptron, targetLabel, output):
    return perceptron.bias + (targetLabel - output) * learnigRate()

def trainPerceptronForDigit(perceptron, digit):
    allClasified = False
    iterationsNr = 1
    trainSet = getTrainSet()
    images = trainSet[0]
    labels = trainSet[1]

    while (not allClasified and iterationsNr > 0):
        allClasified = True
        print("For digit: {}".format(digit))
        for iterator in range(len(images)):
            label = labels[iterator]
            image = images[iterator]
            targetLabel = initializeTargetLabel(label, digit)
            netInput = weightsSum(perceptron, image)
            output = activation(netInput)
            adjustWeights(perceptron, image, targetLabel, output)
            adjustBias(perceptron, targetLabel, output)
            if output != targetLabel:
                allClasified = False
        iterationsNr -= 1

def testPerceptronForDigit(perceptron, digit):
    allClasified = False
    iterationsNr = 1
    testSet = getTestSet()
    images = testSet[0]
    labels = testSet[1]

    goodResults = 0

    while (not allClasified and iterationsNr > 0):
        allClasified = True
        for iterator in range(len(images)):
            label = labels[iterator]
            image = images[iterator]
            targetLabel = initializeTargetLabel(label, digit)
            netInput = weightsSum(perceptron, image)
            output = activation(netInput)
            if output != targetLabel:
                allClasified = False
                goodResults += 1
        iterationsNr -= 1

    return goodResults / 100


def main():
    # Create list of 10 perceptrons.
    listOfPerceptrons = createPerceptrons(10)
    digit = 0

    # Train each perceptron to recognise a specific digit.
    for perceptron in listOfPerceptrons:
        trainPerceptronForDigit(perceptron, digit)
        digit = digit + 1
    digit = 0
    for perceptron in listOfPerceptrons:
        testPerceptronForDigit(perceptron, digit)
        digit = digit + 1
    return 0

main()