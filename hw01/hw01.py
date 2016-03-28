import scipy.io as sio
from scipy.spatial import distance
import math
import random

matContents=sio.loadmat('data0.mat')

def k_mean(matContents, k, count):			 
	n=0	
	mu=[]
	dataSet=[]
	resultSet=[]
	n=len(matContents['x'])*len(matContents['x'][0])
	
	print "number of data set :" ,n	
	print "number of testing :", count
	for a,b in zip(matContents['x'], matContents['y']):
		for c,d in zip(a,b):
			dataSet.append((c,d))

	mu_index=[]
	distanceSet=[]
	for x in range(k):
		mu_index.append(0)
		distanceSet.append(0)
	
	for c in range(count):
		resultSet.append([])	
		for i in range(k):
			resultSet[c].append([])
		
	print "resultSet : "
	print resultSet	

	for i in range(k):
		overlap=True
		while(overlap):
			mu_index[i]=random.randrange(1,10000)%n
			for j in range(i):
				if(mu_index[j] == mu_index[i]):
					overlap=True
					break;
				overlap=False
			if(i==0):
				overlap=False

	for i in range(k):
		mu.append(dataSet[mu_index[i]])


	for c in range(count):
			print "learning : ",c
			for x in dataSet:
				for i in range(k):
					distanceSet[i] = distance.euclidean(x,mu[i])
				resultSet[c][ distanceSet.index(min(distanceSet)) ].append( (x, mu[distanceSet.index(min(distanceSet))]) )
			print "mu" ,mu			
			print "cluster 0"
			print resultSet[c][0]
			print "cluster 1"
			print resultSet[c][1]
			print "cluster 0 + cluster 1 : ",len(resultSet[c][0])+len(resultSet[c][1])
			for i in range(k):
				sumX=0
				sumY=0
	#			print "resultSet[c][i][0]"
	#			print resultSet[c][i][0]
				for x,y in resultSet[c][i][0]:
					sumX+=x
					sumY+=y
				mu[i]=( sumX/len(resultSet[c][i]) , sumY/len(resultSet[c][i]) )
k_mean(matContents,2,6)
