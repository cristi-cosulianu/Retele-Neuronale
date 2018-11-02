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

def activation(input): 
    if input > 0:
        input = 1
    else:
        input = 0
    return input

def targetCheck(t, digit):
    if t == digit:
        return 1
    else:
        return 0

def createAndTrainPerceptron(digit):  
    weights = np.random.uniform(0, 0.1 , 784)
    bias = 0 
    nrIterations = 3
    while (nrIterations > 0):
        trainSet = getTrainSet()
        for iterator in range(50000):
            x = trainSet[0][iterator]
            t = trainSet[1][iterator]
            z = np.dot(x, weights) + bias
            output = activation(z)
            
            error = targetCheck(t, digit) - output
            bias = bias + error * 0.1
            weights = weights + error * x * 0.1
        nrIterations -= 1
    return weights, bias

def test(listOfWeights, listOfBiases): 
    goodResults = 0
    testSet = getTestSet()
    output = np.zeros(10)
    for iterator in range(10000):
        x = testSet[0][iterator]
        t = testSet[1][iterator]
        for digit in range(10):
            output[digit] = np.dot(x, listOfWeights[digit]) + listOfBiases[digit]
        if (output.argmax() == t):
            goodResults += 1
    print(goodResults/100)


def main():
    listOfWeights = np.zeros((10,784))
    listOfBiases = np.zeros(10)

    for digit in range (10):
        listOfWeights[digit], listOfBiases[digit] = createAndTrainPerceptron(digit)
    
    test(listOfWeights, listOfBiases)

main()