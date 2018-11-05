import _pickle, gzip, numpy as np
learningRate = 1
firstLayerSize = 100
lastLayerSize = 10

def getTrainSet():
    f = gzip.open('mnist.pkl.gz', 'rb')
    train_set, valid_set, test_set = _pickle.load(f , encoding = "latin1")
    f.close()
    images = train_set[0]
    labels = train_set[1]
    return images, labels

def getTestSet():
    f = gzip.open('mnist.pkl.gz', 'rb')
    train_set, valid_set, test_set = _pickle.load(f , encoding = "latin1")
    images = test_set[0]
    labels = test_set[1]
    f.close()
    return test_set

def sigmoid(x):
    b = x.max()
    y = np.exp(x - b)
    return y / (1 + y)

def softmax(x):
    y = np.exp(x)
    return y / y.sum()

def trainNeuralNetwork(firstLayer, firstBiases, lastLayer, lastBiases):
    nrIterations = 1
    while (nrIterations > 0):
        trainSet = getTrainSet()
        # Iterate trought all inputs.
        for iterator in range(50000):
            print(iterator)
            input = trainSet[0][iterator]
            target = trainSet[1][iterator]
            targetVector = np.zeros(10)
            targetVector[target] = 1

            firstOutput = np.zeros(firstLayerSize)
            secondOutput = np.zeros(lastLayerSize)
            firstError = np.zeros(firstLayerSize)
            lastError = np.zeros(lastLayerSize)

            # Feed forward.
            firstOutput = (input * firstLayer).sum(axis = 1) + firstBiases
            firstOutput = sigmoid(firstOutput)

            secondOutput = (firstOutput * lastLayer).sum(axis = 1) + lastBiases
            secondOutput = softmax(secondOutput)

            # Propagate error.
            lastError = secondOutput - targetVector
            lastError = lastError.reshape((lastLayerSize,1))
            firstError = firstOutput * (1 - firstOutput) * (lastError * lastLayer).sum(axis = 0)
            firstError = firstError.reshape((firstLayerSize,1))

            # Adjust weights and biases.
            lastLayer = lastLayer - learningRate * lastError * firstOutput
            lastBiases = lastBiases - np.reshape(learningRate * lastError, (lastLayerSize))

            firstLayer = firstLayer - learningRate * firstError * input
            firstBiases = firstBiases - np.reshape(learningRate * firstError, (firstLayerSize))            


        nrIterations -= 1
    return firstLayer, firstBiases, lastLayer, lastBiases

def testNeuralNetwork(firstLayer, firstBiases, lastLayer, lastBiases):
    testSet = getTestSet()
    goodTests = 0
    apparitionList = np.zeros(10)
    # Iterate trought all inputs.
    for iterator in range(10000):
        print(iterator)

        input = testSet[0][iterator]
        target = testSet[1][iterator]

        firstOutput = np.zeros(firstLayerSize)
        secondOutput = np.zeros(lastLayerSize)

        # Feed forward.
        firstOutput = (input * firstLayer).sum(axis = 1) + firstBiases
        firstOutput = sigmoid(firstOutput)

        secondOutput = (firstOutput * lastLayer).sum(axis = 1) + lastBiases
        secondOutput = softmax(secondOutput)

        apparitionList[secondOutput.argmax()] += 1
        if (secondOutput.argmax() == target):
            goodTests = goodTests + 1

    print(apparitionList)
    print("The result is: {}".format(goodTests/100))

def main():
    
    firstLayer = np.random.normal(0, 1 / np.sqrt(firstLayerSize), (firstLayerSize, 784))
    firstBiases = np.random.normal(0 , 1, firstLayerSize)
    lastLayer = np.random.normal(0, 1 / np.sqrt(lastLayerSize), (lastLayerSize, firstLayerSize))
    lastBiases = np.random.normal(0 , 1, lastLayerSize)

    firstLayer, firstBiases, lastLayer, lastBiases = trainNeuralNetwork(firstLayer, firstBiases, lastLayer, lastBiases)
    testNeuralNetwork(firstLayer, firstBiases, lastLayer, lastBiases)

    print("It's working!")

main()