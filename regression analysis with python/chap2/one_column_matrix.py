import numpy as np

#creating a vector
vector = np.array([1,2,3,4,5])

#creating a matrix 1x5
row_vector = vector.reshape((5,1))

#creating a matrix 5x1
column_vector = vector.reshape((1,5))

#the matrix
single_feature_matrix = vector.reshape((1,5))

print(vector)
print(row_vector)
print(column_vector)
print(single_feature_matrix)
