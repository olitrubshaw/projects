import numpy as np
import scipy.spatial.distance as distance_metrics
import pandas as pd
from sklearn.datasets import load_digits
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
#part a

#feature vectors functions
def get_manhattan(v1, v2):
    return distance_metrics.cityblock(v1, v2)

def get_euclidean(v1, v2):
    return distance_metrics.euclidean(v1, v2)

def get_minowski(v1, v2, p):
    return distance_metrics.minkowski(v1, v2, p)

#define vector coordinates
v1 = np.array([2, 4])
v2 = np.array([1, 2])
v3 = np.array([5, 4])

print("distance from v1 and v2: ")
print("Manhattan: ", get_manhattan(v1, v2))
print("Euclidean: ", get_euclidean(v1, v2))
print("Minowski: ", get_minowski(v1, v2, 3))

print("distance from v1 and v3: ")
print("Manhattan: ", get_manhattan(v1, v3))
print("Euclidean: ", get_euclidean(v1, v3))
print("Minowski: ", get_minowski(v1, v3, 3))

print("distance from v2 and v3: ")
print("Manhattan: ", get_manhattan(v2, v3))
print("Euclidean: ", get_euclidean(v2, v3))
print("Minowski: ", get_minowski(v2, v3, 3))

vA = np.array([0, 0, 0])
vB = np.array([255, 255, 255])

print("distance from vA and vB: ")
print("Manhattan: ", get_manhattan(vA, vB))
print("Euclidean: ", get_euclidean(vA, vB))
print("Minowski: ", get_minowski(vA, vB, 3))

#part b
#reads data from csv file
data = pd.read_csv("knn-2d-toy-dataset.csv", header=None)
data = data.to_numpy()

#split data into features and labels
x_train = data[:, 1:3].astype(float)
y_train = data[:, 3]

query = np.array([6.0, 2.0])

#function to find nearest neighbor
def find_nearest(query, x_train, y_train, distance_func):
    distances = []
    for i in range(len(x_train)):
        d = distance_func(x_train[i], query)
        distances.append(d)

    nearest_index = np.argmin(distances)

    print("nearest instance: ", int(data[nearest_index, 0]))
    print("shortest distance: ", distances[nearest_index])
    print("predicted insect type: ", y_train[nearest_index])

print("Manhattan: ")
find_nearest(query, x_train, y_train, get_manhattan)

print("Euclidean: ")
find_nearest(query, x_train, y_train, get_euclidean)

#part c
#handwritten digits dataset
dataset = load_digits()
X = dataset.data
Y = dataset.target
print("Feature data shape: ", X.shape)
print("Class labels shape: ", Y.shape)

#train KNN classifier
knn = KNeighborsClassifier(n_neighbors=1, metric="euclidean")
knn.fit(X, Y)
y_predict = knn.predict(X)
accuracy = accuracy_score(Y, y_predict)
print("accuracy: ", accuracy)
print("accuracy percent: ", accuracy * 100, "%")

#test loop
k_values = [3, 11, 100]
metrics = ["euclidean", "manhattan", "minkowski"]
results = []
for k in k_values:
    for metric in metrics:
        knn = KNeighborsClassifier(n_neighbors = k, metric = metric)
        knn.fit(X, Y)
        y_predict = knn.predict(X)
        accuracy = accuracy_score(Y, y_predict)
        results.append((k, metric, accuracy))
        print("k: ", k, " metric: ", metric, " accuracy: ", accuracy)

#find the best configuration
best_config = max(results, key = lambda result: result[2])
print("Best configuration: k = ", best_config[0])
print("Best configuration: metric = ", best_config[1])
print("Best configuration: accuracy = ", best_config[2], 4)
