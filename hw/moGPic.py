import scipy.io as sio
from scipy.spatial import distance
import math
import random
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import Image

img=Image.open('3096.jpg')

def moG(matContents, k, count):			 
	n=0
	D=0	
	mu=[]
	sigma=[]
	pi=[]
	dataSet=[]
	resultSet=[]
	r=[]
	mu_index=[]

	imgSet = list(img.getdata())
	n=len(imgSet)
	D=len(imgSet[0])	

	print "number of data set :" ,n	
	print "number of testing :", count
	
	for r,g,b in imgSet:
		dataSet.append(np.matrix([r,g,b]))

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
		sigma.append(100*np.identity(D))
		pi.append(1.0/k)

	for c in range(count):
			print "learning : ",c
			print "mu", mu			
			print "sigma", sigma	
			r=eStep(dataSet, mu, sigma, pi)
			mu, sigma, pi = mStep(r, dataSet)

	mu_rgb=[]
	for j in range(k):
		for R,G,B in map(tuple,mu[j].A):
			mu_rgb.append( (int(R), int(G), int(B)) )		

	for i in range(n):
		maxIndex=r[:,i].argmax()
		resultSet.append( mu_rgb[maxIndex] )

	moGImg=Image.new('RGB',img.size)
	moGImg.putdata(resultSet)
	moGImg.save('moGImg.jpg')
	moGImg.show()
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
		for i in range(N):
			nominator+=r[j][i]*dataSet[i]
		mu.append(nominator/sum(r[j]))
	
	for j in range(K):
		nominator=0
		for i in range(N):
			nominator+=r[j][i]*np.dot((dataSet[i]-mu[j]).transpose(), (dataSet[i]-mu[j]))
		sigma.append(nominator/sum(r[j]))	

	for j in range(K):
		minIndex=pi.append(sum(r[j])/N)
			
	return mu, sigma, pi

def pdf(mu, sigma, x):
	
	D=len(sigma)
	A=math.pow(2*math.pi,-0.5*D) * math.pow(np.absolute(np.linalg.det(sigma)), -0.5)
	B=math.exp( -0.5*np.dot(np.dot( x-mu, np.linalg.inv(sigma)), (x-mu).transpose() ) )
	return A*B


moG(img, 2, 3)
moG(img, 5, 3)
moG(img, 7, 3)
