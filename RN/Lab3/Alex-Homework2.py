import _pickle, gzip, numpy as np
f = gzip.open('mnist.pkl.gz', 'rb')
train_set, valid_set, test_set = _pickle.load(f , encoding = "latin1")
f.close()

iterations = 10
input_layer_nodes = 784
output_layer_nodes = 10
learning_rate = 0.1
weight_matrix = np.random.uniform(0, 0.1 , (input_layer_nodes , output_layer_nodes))
bias = np.random.uniform(0 , 0.1 , (output_layer_nodes))

def predict_array(input):
    pred = np.add(np.matmul(input , weight_matrix),bias)
    for i in range(0,len(pred)):
        pred[i] = pred[i] / input_layer_nodes #Normalize data
    return pred


def predict(input):
    prediction_array = np.add(np.matmul(input , weight_matrix) , bias)
    max = -1;
    index = -1;
    for i in range(0,len(prediction_array)):
        if(prediction_array[i] > max):
            max = prediction_array[i]
            index = i
    return index

def train(input , output):
    global weight_matrix
    prediction = predict_array(input)
    vector_output = np.zeros((output_layer_nodes,))
    vector_output[output] = 1.0
    matrix_delta = []
    total_error = np.sum(np.subtract(vector_output , prediction))
    for i in range(output_layer_nodes):
        error = (vector_output[i] - prediction[i])
        bias[i] += learning_rate * error
        matrix_delta.append(np.dot(input , error * learning_rate))
    weight_matrix = np.add(weight_matrix , np.transpose(matrix_delta))
    return total_error;

def test_accuracy():
    for i in range(0,iterations):
        total_error_iteration = 0
        for j in range(0,len(train_set[0])):
            total_error_iteration += train(train_set[0][j] , train_set[1][j])
        print(total_error_iteration / len(test_set[0]) , flush = True)
    correct = 0
    for i in range(0,len(test_set[0])):
        if(predict(test_set[0][i]) == test_set[1][i]):
            correct += 1
    print("Accuracy : " + str((correct / len(test_set[0])) * 100))

test_accuracy()import _pickle, gzip, numpy as np
f = gzip.open('mnist.pkl.gz', 'rb')
train_set, valid_set, test_set = _pickle.load(f , encoding = "latin1")
f.close()

iterations = 10
input_layer_nodes = 784
output_layer_nodes = 10
learning_rate = 0.1
weight_matrix = np.random.uniform(0, 0.1 , (input_layer_nodes , output_layer_nodes))
bias = np.random.uniform(0 , 0.1 , (output_layer_nodes))

def predict_array(input):
    pred = np.add(np.matmul(input , weight_matrix),bias)
    for i in range(0,len(pred)):
        pred[i] = pred[i] / input_layer_nodes #Normalize data
    return pred


def predict(input):
    prediction_array = np.add(np.matmul(input , weight_matrix) , bias)
    max = -1;
    index = -1;
    for i in range(0,len(prediction_array)):
        if(prediction_array[i] > max):
            max = prediction_array[i]
            index = i
    return index

def train(input , output):
    global weight_matrix
    prediction = predict_array(input)
    vector_output = np.zeros((output_layer_nodes,))
    vector_output[output] = 1.0
    matrix_delta = []
    total_error = np.sum(np.subtract(vector_output , prediction))
    for i in range(output_layer_nodes):
        error = (vector_output[i] - prediction[i])
        bias[i] += learning_rate * error
        matrix_delta.append(np.dot(input , error * learning_rate))
    weight_matrix = np.add(weight_matrix , np.transpose(matrix_delta))
    return total_error

def test_accuracy():
    for i in range(0,iterations):
        total_error_iteration = 0
        for j in range(0,len(train_set[0])):
            total_error_iteration += train(train_set[0][j] , train_set[1][j])
        print(total_error_iteration / len(test_set[0]) , flush = True)
    correct = 0
    for i in range(0,len(test_set[0])):
        if(predict(test_set[0][i]) == test_set[1][i]):
            correct += 1
    print("Accuracy : " + str((correct / len(test_set[0])) * 100))

test_accuracy()