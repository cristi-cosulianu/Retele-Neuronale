import _pickle, gzip, numpy as np
learningRate = 0.3

firstLayerSize = 30
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

def targetCheck(t, digit):
    if t == digit:
        return 1
    else:
        return 0

def sigmoidActivation(zList):
    normalizer = zList.max()
    normalizedList = np.array(zList - normalizer)
    return 1 / (1 + np.exp(normalizedList))

def softMaxActivation(zList):
    normalizer = zList.max()
    expList = np.exp(zList - normalizer)
    sumExpList = expList.sum()
    return expList / sumExpList

def trainNeuralNetwork(firstLayer, firstBiases, lastLayer, lastBiases):
    firstLayer[0] = np.zeros(784)
    nrIterations = 1
    while (nrIterations > 0):
        trainSet = getTrainSet()
        # Iterate trought all inputs.
        for iterator in range(50000):
            print(iterator)
            input = trainSet[0][iterator]
            target = trainSet[1][iterator]
            firstOutput = np.zeros(firstLayerSize)
            secondOutput = np.zeros(lastLayerSize)

            # Compute output for all neurons from FIRST layer.
            for index in range(firstLayerSize):
                z = np.dot(input, firstLayer[index]) + firstBiases[index]
                firstOutput[index] = z
            firstOutput = sigmoidActivation(firstOutput)



            # Compute output for all neurons from LAST layer.
            secondOutput = np.zeros(lastLayerSize)
            for index in range(lastLayerSize):
                secondOutput[index] = softMaxActivation(np.dot(firstOutput, lastLayer[index]) + lastBiases[index])
            

            # Calculate error for all neurons form LAST layer.
            lastError = np.zeros(lastLayerSize)
            for index in range(lastLayerSize):
                #lastError[index] = secondOutput[index] * (1 - secondOutput[index]) * (secondOutput[index] - targetCheck(target, index))
                lastError[index] = secondOutput[index] - targetCheck(target, index)

            # Propagate the error to FIRST layer.
            firstError = np.zeros(firstLayerSize)
            for index in range(firstLayerSize):
                # Multiply errors from LAST layer with weigts for this neuron.
                errorWeightsList = lastError * firstLayer[:,[index]]
                # Calculate error for this neuron.
                firstError[index] = firstOutput[index] * (1 - firstOutput[index]) * errorWeightsList.sum()

            # Calculate cost function for every weight between FIRST and LAST layer.
            for index in range(lastLayerSize):
                biasCostFunction = lastError[index] * learningRate
                # Adjust every biases between FIRST and LAST layer.
                lastBiases[index] = lastBiases[index] - biasCostFunction

                weightsCostFunction = firstOutput * biasCostFunction
                # Adjust every weight between FIRST and LAST layer.
                lastLayer[index] = lastLayer[index] - weightsCostFunction
            
            # Calculate cost function for every weight between INPUT and FIRST layer.
            for index in range(firstLayerSize):
                biasCostFunction = firstError[index] * learningRate
                # Adjust every biases between INPUT and FIRST layer.
                firstBiases[index] = firstBiases[index] - biasCostFunction

                weightsCostFunction = input * biasCostFunction 
                # Adjust every weight between INPUT and FIRST layer.
                firstLayer[index] = firstLayer[index] - weightsCostFunction

        nrIterations -= 1
    return firstLayer, firstBiases, lastLayer, lastBiases

def testNeuralNetwork(firstLayer, firstBiases, lastLayer, lastBiases):
    testSet = getTestSet()
    goodTests = 0
    apparitionList = np.zeros(10)
    # Iterate trought all inputs.
    for iterator in range(10000):
        input = testSet[0][iterator]
        target = testSet[1][iterator]
        firstOutput = np.zeros(firstLayerSize)
        secondOutput = np.zeros(lastLayerSize)

        # Compute output for all neurons from FIRST layer.
        for index in range(firstLayerSize):
            firstOutput[index] = np.dot(input, firstLayer[index]) + firstBiases[index]

        # Compute output for all neurons from LAST layer.
        secondOutput = np.zeros(lastLayerSize)
        for index in range(lastLayerSize):
            secondOutput[index] = np.dot(firstOutput, lastLayer[index]) + lastBiases[index]

        apparitionList[secondOutput.argmax()] += 1
        if (secondOutput.argmax() == target):
            goodTests = goodTests + 1

    print(apparitionList)
    print("The result is: {}".format(goodTests / 100))

def main():
    firstLayer = np.random.uniform(0, 0.1, (firstLayerSize, 784))
    firstBiases = np.random.uniform(0, 1, firstLayerSize)
    lastLayer = np.random.uniform(0, 0.1, (lastLayerSize, firstLayerSize))
    lastBiases = np.random.uniform(0, 1, lastLayerSize)

    firstLayer, firstBiases, lastLayer, lastBiases = trainNeuralNetwork(firstLayer, firstBiases, lastLayer, lastBiases)
    testNeuralNetwork(firstLayer, firstBiases, lastLayer, lastBiases)

    print("It's working!")

main()