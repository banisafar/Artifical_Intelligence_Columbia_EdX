import numpy as np
import pandas as pd
import scipy as sp
import sys
import csv

#X = np.genfromtxt(sys.argv[1], delimiter = ",")

def KMeans(data):
	#perform the algorithm with 5 clusters and 10 iterations...you may try others for testing purposes, but submit 5 and 10 respectively

    dim = data.shape[1]
    N = data.shape[0]
    print(N)

    #initialize centroids
    #centroids = np.random.rand(4,dim)  #later change this to 5
    centerslist = [[1,1], [-1, -1], [-1, 1], [1,-1]]



    for i in range(1):
        print(i)

        for j in range(N):
            print('-------------')
            print(j)
            for k in range(4):
                print(data[j, :] - centerslist[k])
                print(np.linalg.norm(data[j, :] - centerslist[k]))





        #cluster assignment


        #calculate centroid

        #filename = "centroids-" + str(i+1) + ".csv" #"i" would be each iteration
        #np.savetxt(filename, centerslist, delimiter=",")
    return data






if __name__ == '__main__':
    data = np.genfromtxt(sys.argv[1], delimiter = ",")
    KMeans(data)


    #print(x.shape)
    #np.savetxt("/Users/sahar.banisafar/Desktop/X.csv", x, delimiter=",")
