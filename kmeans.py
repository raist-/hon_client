import numpy
import random

class kmeans(object):

    def __init__(self, data, num_clusters):
        self.__data = data
        self.__num_records = data.shape[0]
        self.__num_dimensions = data.shape[1]
        self.__num_clusters = num_clusters
        self.__centroids = numpy.zeros(shape = (self.__num_clusters, self.__num_dimensions))
        self.__cluster_matrix = numpy.zeros(shape = (self.__num_records, 2))
        self.__cluster_matrix[:,0] = self.__cluster_matrix[:,0] + 1000000


    def initCentroids(self):
        for centroid_index in xrange(self.__num_clusters):
            random_data_index = random.randint(0, self.__num_records - 1)
            print random_data_index
            print centroid_index
            numpy.copyto(self.__centroids[centroid_index], self.__data[random_data_index])

    def updateClusters(self):

        #calculate the sum of squares where arr2 is the matrix of sample points and arr is the current cluster vector.
        for centroid_index in xrange(self.__num_clusters):
            possible_cluster_updates = numpy.zeros(shape = self.__cluster_matrix.shape)
            possible_cluster_updates[:,1] = centroid_index
            possible_cluster_updates[:,0] = numpy.sum((self.__data - self.__centroids[centroid_index])**2, axis=1)
                        
            numpy.copyto(self.__cluster_matrix, possible_cluster_updates, where = numpy.repeat(possible_cluster_updates[:,0] < self.__cluster_matrix[:,0], 2).reshape(self.__cluster_matrix.shape))
            print possible_cluster_updates
            print self.__cluster_matrix
    #def clusterData(self):