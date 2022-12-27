import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def main():
    path = 'gumtree_vector.csv' # Path to the csv file
    # analyze the vectors within the csv file
    # each line is a vector

    # read the csv file
    df = pd.read_csv(path, sep='delimiter', header=None, engine='python')

    # collect lengths of each vector
    lengths = []
    # for each line in the csv file
    for i in range(len(df)):
        # each line is vector of the form [x1, y1, x2, y2, ...]
        vector = df.iloc[i]
        # convert the vector to a numpy array
        vector = np.array(vector[0].split(','))
        # add the length to the list
        lengths.append(len(vector))

    # find the max, min, avg, median, std of length of vectors and print them
    print(f"analysis on gumtree_vector.csv")
    print('max: ', max(lengths))
    print('min: ', min(lengths))
    print('avg: ', np.mean(lengths))
    print('median: ', np.median(lengths))
    print('std: ', np.std(lengths))

    # find index of max length vector
    max_index = lengths.index(max(lengths))
    print(f"max length vector index: {max_index}")

    # plot the lengths
    # max size of the vector is 1000000
    plt.plot(lengths)
    plt.xlabel('vector index')
    plt.ylabel('vector length')
    plt.title('vector length analysis')
    plt.show()



    
if __name__ == '__main__':
    main()