import scipy.io as sio
from scipy.spatial import distance
import math
import random
import Image

img = Image.open('108005.jpg')

def k_mean(matContents, k, count, beta):			 
	n=0	
	mu=[]
	dataSet=[]
	resultSet=[]
	r=[]
	dataSet=list(img.getdata())
	n=len(dataSet)	
	
	print "number of data set :" ,n	
	print "number of testing :", count

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
			r=calculatingR(dataSet, k, mu, beta)
			mu=calculatingMu(dataSet, k, mu, r)

def calculatingR(dataSet, k, mu, beta):
	r=[]
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

def calculatingMu(dataSet, k, mu, r):
	for i in range(k):
		sigmaRX=[]
		sigmaR=0
		indexOfX=0
		mr=0
		mg=0
		mb=0
		for x in dataSet:
			for r,g,b in x:
				mr+=r*r[i][indexOfX]
				mg+=g*r[i][indexOfX]
				mb+=b*r[i][indexOfX]
				indexOfX=+1
		sigmaR=sum(r[i])
		mu[i]= [mr/sigmaR, mg/sigmaR, mb/sigmaR]
	return mu

k_mean(img, 2, 1, 0.0005)
