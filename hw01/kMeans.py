import scipy.io as sio
from scipy.spatial import distance
import math
import random
import Image

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
			print "mu", mu
			for x in dataSet:
				for i in range(k):
					distanceSet[i] = distance.euclidean(x,mu[i])
#				print "distance Set : ",distanceSet, "min : ",min(distanceSet), "index: ",distanceSet.index(min(distanceSet))
				resultSet[c][ distanceSet.index(min(distanceSet)) ].append( x )
			
			for i in range(k):
#				print "cluster ", i
				print "number of data in cluster i ",i, ": ", len(resultSet[c][i])
				print resultSet[c][i]
		
			for i in range(k):
				
#				print "number of resultSet of cluster i ",i, ": ", len(resultSet[c][i])
				try:
					sigmaOfX=0
					sigmaOfY=0
					for x,y in resultSet[c][i]:
						sigmaOfX+=x
						sigmaOfY+=y
					mu[i]=( sigmaOfX/len(resultSet[c][i]) , sigmaOfY/len(resultSet[c][i]))	
				except:
					print "zero term"

k_mean(matContents,2,2)
