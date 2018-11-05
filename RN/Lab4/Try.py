import _pickle, gzip, numpy as np
learningRate = 0.7
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

def trainNeuralNetwork():

    firstLayer = np.random.normal(0, 1 / np.sqrt(firstLayerSize), (firstLayerSize, 784))
    lastLayer = np.random.normal(0, 1 / np.sqrt(lastLayerSize), (lastLayerSize, firstLayerSize))
    firstBiases = np.random.normal(0 , 0.1, firstLayerSize)
    lastBiases = np.random.normal(0 , 0.1, lastLayerSize)

    nrIterations = 1
    while (nrIterations > 0):
        trainSet = getTrainSet()
        # Iterate trought all inputs.
        for iterator in range(len(trainSet[0])):
            print(iterator)
            input = trainSet[0][iterator]
            target = trainSet[1][iterator]
            targetVector = np.zeros(10)
            targetVector[target] = 1

            # Feed forward.
            firstOutput = sigmoid(np.dot(firstLayer, input) + firstBiases)
            lastOutput = softmax(np.dot(lastLayer, firstOutput) + lastBiases)

            # Calculate error for last layer.
            lastError = lastOutput - targetVector
            lastError = np.reshape(lastError, (lastLayerSize, 1))
 
            
            # Calculate first layer error.
            firstError = firstOutput * (1 - firstOutput) * (lastLayer * lastError).sum(axis = 0)
            firstError = np.reshape(firstError, (firstLayerSize, 1))

            # Adjust weights.
            lastLayer = lastLayer - learningRate * lastError * firstOutput
            firstLayer = firstLayer - learningRate * firstError * input

            # Adjust biases.
            firstBiases = firstBiases - firstError.flatten() * learningRate
            lastBiases = lastBiases - lastError.flatten() * learningRate

        nrIterations -= 1
    return firstLayer, firstBiases, lastLayer, lastBiases

def testNeuralNetwork(firstLayer, firstBiases, lastLayer, lastBiases):
    testSet = getTestSet()
    goodTests = 0
    apparitionList = np.array([0,0,0,0,0,0,0,0,0,0])
    # Iterate trought all inputs.
    for iterator in range(len(testSet[0])):
        print(iterator)

        input = testSet[0][iterator]
        target = testSet[1][iterator]

        # Feed forward.
        firstOutput = sigmoid(np.dot(firstLayer, input) + firstBiases)
        lastOutput = softmax(np.dot(lastLayer, firstOutput) + lastBiases)

        apparitionList[lastOutput.argmax()] += 1
        if (lastOutput.argmax() == target):
            goodTests = goodTests + 1

    print(apparitionList)
    print("The result is: {}".format(goodTests/100))

def main():
    
    firstLayer, firstBiases, lastLayer, lastBiases = trainNeuralNetwork()
    testNeuralNetwork(firstLayer, firstBiases, lastLayer, lastBiases)

main()