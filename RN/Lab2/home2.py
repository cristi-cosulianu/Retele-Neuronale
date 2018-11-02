import cPickle, gzip, numpy as np

def getTrainSet():
    f = gzip.open('mnist.pkl.gz', 'rb')
    train_set, valid_set, test_set = cPickle.load(f)
    f.close()
    images = train_set[0]
    labels = train_set[1]
    return images, labels

def getTestSet():
    f = gzip.open('mnist.pkl.gz', 'rb')
    train_set, valid_set, test_set = cPickle.load(f)
    images = test_set[0]
    labels = test_set[1]
    f.close()
    return test_set

def activation(input): 
    for i in range(len(input)):
        if input[i] > 0:
            input[i] = 1
        else:
            input[i] = 0
    return input

def targetCheck(t, digit):
    if t == digit:
        return 1
    else:
        return 0

def train(listOfPerceptrons, listOfBiases):   
    nrIterations = 1
    while (nrIterations > 0):
        trainSet = getTrainSet()
        for iterator in range(50000):
            z = np.dot(trainSet[0][iterator], listOfPerceptrons) + listOfBiases
            output = activation(z)
            
            # adjust weights
            for i in range(10):
                error = targetCheck(trainSet[1][iterator], i) - output[i]
                print (error)
                print(np.shape(listOfPerceptrons[i]))
                listOfBiases[i] = listOfBiases[i] + error * 0.1
                # incearca cu operatii de numpy
                # 
                listOfPerceptrons[i] = listOfPerceptrons[i] + error * trainSet[0][iterator] * 0.1
        nrIterations -= 1

def test(listOfPerceptrons, listOfBiases): 
    goodResults = 0
    testSet = getTestSet()
    for iterator in range(10000):
        output = np.dot(testSet[0][iterator], listOfPerceptrons) + listOfBiases
        if (output.argmax() == testSet[1][iterator]):
            goodResults += 1
    print(goodResults)


def main():
    listOfPerceptrons = np.zeros((784,10))
    listOfBiases = np.zeros(10)
    train(listOfPerceptrons, listOfBiases)
    test(listOfPerceptrons, listOfBiases)

main()