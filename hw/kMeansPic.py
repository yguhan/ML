import scipy.io as sio
from scipy.spatial import distance
import math
import random
import Image


img=Image.open("3096.jpg")

def k_mean(matContents, k, count):			 
	n=0	
	mu=[]
	imgSet=[]
	dataSet=[]
	resultSet=[]
	#n=len(matContents['x'])*len(matContents['x'][0])
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
		imgSet.append([])
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
			resultSet[c][ distanceSet.index(min(distanceSet)) ].append( x )				
			imgSet[c].append(mu[ distanceSet.index(min(distanceSet)) ])			
		
		for i in range(k):
				
			try:
				sigmaOfR=0
				sigmaOfG=0
				sigmaOfB=0
					
				for r,g,b in resultSet[c][i]:
					sigmaOfR+=r
					sigmaOfG+=g
					sigmaOfB+=b
				mu[i]=( sigmaOfR/len(resultSet[c][i]), sigmaOfG/len(resultSet[c][i]), sigmaOfB/len(resultSet[c][i]) )
					
			except:
				print "zero term"
		
	kImg=Image.new('RGB', img.size)
	kImg.putdata(imgSet[c-1])
	kImg.save('kImg.jpg')
	kImg.show()
k_mean(img, 2, 3)		
k_mean(img, 4, 3)			
k_mean(img, 6, 3)			 
