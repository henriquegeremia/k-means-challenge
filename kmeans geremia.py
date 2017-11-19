import pandas as pd

file_path = 'height weight.csv'
csv_file = pd.read_csv(file_path, header=None)
csv_file.head()

# testing

df = csv_file
k = 2

n_of_registers, n_of_features = df.shape

# it creates a vector for each register
points = []
for i in n_of_registers:
    df.iloc
    points = points.append()

start_centroids(k, points)
