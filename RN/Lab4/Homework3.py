import _pickle, gzip, numpy as np

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

def sigmoidActivation(z):
    return 1 / (1 + np.exp(-z))

def softMaxActivation(zList):
    #expList = np.array(list(map(lambda z : np.exp(z), zList)))
    #expList = np.array([lambda z : np.exp(z) for z in zList])
    expList = np.zeros(len(zList))
    for index in range(len(zList)):
        expList[index] = np.exp(zList[index])
    sumExpList = expList.sum()
    return np.array(list(map(lambda expZ : expZ / sumExpList, expList)))

def trainNeuralNetwork(firstLayer, firstBiases, lastLayer, lastBiases):
    nrIterations = 1
    while (nrIterations > 0):
        trainSet = getTrainSet()
        # Iterate trought all inputs.
        for iterator in range(50000):
            input = trainSet[0][iterator]
            target = trainSet[1][iterator]
            firstOutput = np.zeros(100)
            secondOutput = np.zeros(10)

            # Compute output for all neurons from FIRST layer.
            for index in range(100):
                z = np.dot(input, firstLayer[index]) + firstBiases[index]
                firstOutput[index] = sigmoidActivation(z)

            # Compute partial output for all neurons from LAST layer.
            secondPartialOutput = np.zeros(10)
            for index in range(10):
                secondPartialOutput[index] = np.dot(firstOutput, lastLayer[index] + lastBiases[index])
            
            # Activate partial output from LAST layer.
            secondOutput = softMaxActivation(secondPartialOutput)

            # Calculate error for all neurons form LAST layer.
            lastError =  np.array(list(map(lambda z : z - target, secondOutput)))

            # Propagate the error to FIRST layer.
            firstError = np.zeros(100)
            for index in range(100):
                # Multiply errors from LAST layer with weigts for this neuron.
                errorWeightsList = lastError * firstLayer[:,[index]]
                # Calculate error for this neuron.
                firstError[index] = firstOutput[index] * (1 - firstOutput[index]) * errorWeightsList.sum()

            # Calculate cost function for every weight and adjust every weight between FIRST and LAST layer.
            # Calculate cost function for every weight and adjust every weight between INPUT and FIRST layer.

        nrIterations -= 1

def main():
    firstLayer = np.random.uniform(0, 0.1, (100, 784))
    firstBiases = np.random.uniform(0, 1, 100)
    lastLayer = np.random.uniform(0, 0.1, (10, 100))
    lastBiases = np.random.uniform(0, 1, 10)

    trainNeuralNetwork(firstLayer, firstBiases, lastLayer, lastBiases)

    print("It's working!")

main()