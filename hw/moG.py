import scipy.io as sio
from scipy.spatial import distance
import math
import random
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab

matContents=sio.loadmat('data3.mat')

def moG(matContents, k, count):			 
	n=0	
	mu=[]
	sigma=[]
	pi=[]
	dataSet=[]
	resultSet=[]
	r=[]
	mu_index=[]
	n=len(matContents['x'])*len(matContents['x'][0])
	D=2

	print "number of data set :" ,n	
	print "number of testing :", count
	for a,b in zip(matContents['x'], matContents['y']):
		for c,d in zip(a,b):
			dataSet.append(np.matrix([c,d]))

	for i in range(k):
		mu_index.append(0)

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
		sigma.append(np.identity(D))
		pi.append(1.0/k)
	for c in range(count):
			print "learning : ",c
			print "mu", mu			
			print "sigma", sigma	
			r=eStep(dataSet, mu, sigma, pi)
			mu, sigma, pi = mStep(r, dataSet)
"""
	for i in range(k):
		x,y= np.random.multivariate_normal(mu[i], sigma[i], 50).T
		plt.plot(x,y)
		plt.show()	
"""
def eStep(dataSet, mu, sigma, pi):

	k=len(mu)
	N=len(dataSet)
	r=np.empty([k,N])
	print "mu: ", mu		 	
	nominator=0
	denominator=0


	for j in range(k):
		index=0
		for i in range(len(dataSet)):
			nominator=pdf(mu[j],sigma[j],dataSet[index])*pi[j]
			denominator=0
			for q in range(k):
				denominator+=pdf(mu[q],sigma[q],dataSet[index]) * pi[q]		 
			r[j][i]=nominator/denominator
			index+=1
#	print "R"
#	print r
	return r

def mStep(r, dataSet):

	mu = []
	sigma = []
	pi=[]

	K = len(r[:,0])
	N = len(dataSet)

	for j in range(K):
		nominator=0
		for i in range(len(dataSet)):
			nominator+=r[j][i]*dataSet[i]
		mu.append(nominator/sum(r[j]))
	
	for j in range(K):
		nominator=0
		for i in range(len(dataSet)):
			nominator+=r[j][i]*np.dot((dataSet[i]-mu[j]).transpose(), (dataSet[i]-mu[j]))
		sigma.append(nominator/sum(r[j]))	

	for j in range(K):
		pi.append(sum(r[j])/len(dataSet))
	return mu, sigma, pi

def pdf(mu, sigma, x):
	k=len(sigma)
	A=math.pow(2*math.pi,-0.5*k) * math.pow(np.absolute(np.linalg.det(sigma)), -0.5)
	B=math.exp( -0.5*np.dot(np.dot( x-mu, np.linalg.inv(sigma)), (x-mu).transpose() ) )
	return A*B


moG(matContents, 2, 5)
