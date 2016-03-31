import scipy.io as sio
from scipy.spatial import distance
import math
import random
import numpy
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab

matContents=sio.loadmat('data0.mat')

def moG(matContents, k, count, beta):			 
	n=0	
	mu=[]
	sig=[]
	dataSet=[]
	resultSet=[]
	r=[]
	n=len(matContents['x'])*len(matContents['x'][0])
	
	print "number of data set :" ,n	
	print "number of testing :", count
	for a,b in zip(matContents['x'], matContents['y']):
		for c,d in zip(a,b):
			dataSet.append([c,d])

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
			r=eStep(dataSet, k, mu, beta)
			mu=mStep(dataSet, k, mu, r)
	#		print "test : ", r[0][10]+r[1][10]

def eStep(dataSet, k, mu, beta):
	r=numpy.zeros(shape=(k,len(dataSet)))
	term=[]
	for i in range(k):
		r.append([])
		term.append([])

	for i in range(k):
		for x in dataSet:
			term[i].append( math.exp(-beta* math.pow(distance.euclidean(x,mu[i]),2)) )
	for i in range(k):
		for x in range(len(dataSet)):
			sigma=0
			for j in range(k):
				sigma+=term[j][x]	
			r[i].append( term[i][x]/sigma )
	print "R"
	print r
	return r

def mStep(dataSet, k, mu, r):
	for i in range(k):
		sigmaRX=[]
		sigmaR=0
		indexOfX=0
		for x in dataSet:
			sigmaRX.append([r[i][indexOfX]*s for s in x])
#			print "Rx: ", sigmaRx
			indexOfX+=1
		mx=0
		my=0
		sigmaR=sum(r[i])
		for x,y in sigmaRX:
			mx+=x
			my+=y			
		mu[i]= [mx/sigmaR, my/sigmaR]
				
	return mu

moG(matContents, 2, 4, 0.5)
