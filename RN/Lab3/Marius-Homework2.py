import pickle,gzip
import numpy as np

def test(w,b,test_set):
    success=0
    failure=0
    x=np.array(test_set[0])
    t=np.array(test_set[1])
    chance=np.zeros(10)
    for i in range(len(x)):
        for j in range(10):
            z=x[i]*w[j]+b[j]
            chance[j]=z.mean()
        print(np.argmax(chance),t[i])
        if np.argmax(chance)==t[i]:
            success+=1
        else:
            failure+=1
    print("Success:")
    print(success)
    print("Failure:")
    print(failure)


def perceptron(train_set,digit):
    x = np.array(train_set[0])
    t = np.array(train_set[1])
    w = np.zeros(784) #np.random.rand(784) - 0.5
    w.reshape((28,28))
    b = 0
    m = 0.1
    nrIterations = 1
    while (nrIterations>0):
        for i in range(len(x)):
            print(i)
            z = x[i] * w + b
            o=activation(z)
            target=1 if t[i]==digit else -1
            w=w+(target-o)*x[i]*m
            b=b+(target-o)*m
        nrIterations-=1
    return w,b


def activation(input):
    return input.mean()
    # result=np.abs(input)
    # result+=1
    # result=np.divide(input,result)
    # return result,result.sum()

f=gzip.open("mnist.pkl.gz","rb")
train_set, valid_set, test_set = pickle.load(f,encoding="latin1")
#train_set[0]-50000 elemente (vectori de numere intre 0 si 1
#train_set[0][0]-784 elemente (numere intre 0 si 1)
#train_set[1]-50000 elemente (cifre de la 0 la 9)
f.close()
w=np.zeros((10,784))
b=np.zeros(10)
for i in range(10):
    w[i],b[i]=perceptron(train_set,i)
print(b)
test(w,b,test_set)