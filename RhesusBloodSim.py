#rhesus population calculator
import random
from random import choice
#import numpy as np

#randnums= np.random.randint(0,2,10)
#print(randnums)
nextgenalleles = []
thisgenalleles = []
storecountdeadkids = []
print("This program will simulate the propagation of Rhesus negative alleles through a population\n")
#print("")
def startchoices():
	startprevalence = int(input("What percentage of the population Rhesus positive do you want to start with.\n>>>"))
	startpopulationsize = int(input("How many couples are in your starting population?"))
	generationtime = int(input("How many generations do you want to simulate? To run until elimination, leave field blank\n>>>"))
	averagefamilysize = int(input("What is the average family size? family sizes will be randomly generated with a gaussian distribution\n>>>"))
	runsim(startprevalence,startpopulationsize,generationtime,averagefamilysize)	

def conception(averagefamilysize,child,father,mother,generationtime,storecountdeadkids):
	familydistribution = random.gauss(averagefamilysize, averagefamilysize/4)
	print(familydistribution, "average family size")
	familydistribution = round(familydistribution)
	print (familydistribution, "rounded family size")
	for y in range (0, familydistribution):
		zygosity = random.randint(0,1)
		if  zygosity == 1:
			child.allele1 = father.allele1
		else:
			child.allele1 = father.allele2
		zygosity = random.randint(0,1)
		if zygosity == 1:
			child.allele2 = mother.allele1
		else:
			child.allele2 = mother.allele2
		child.phenotype = (child.allele1, child.allele2) 
		print(child.phenotype,("this is the child phenotype for the child number" +str(y+1)))
# now work out how to count the loss of children
		#if mother.phenotype ==(0,0) and child.phenotype !=(0,0):
				#mother.sensitised =+ 1  ### come back to this later- -- - - - - - '
				#print(mother.sensitised)
		if mother.phenotype == (0,0) and child.phenotype !=(0,0)  and y>0: #mother.sensitised >0: 
			storecountdeadkids.append(1)
			print("the child died")
		else:
			nextgenalleles.append(child.phenotype)
			#nextgenallele2.append(child.allele2)
	print("this be the list", nextgenalleles)
	print("No of homozygous negatives",nextgenalleles.count((0 , 0)))
	print("No of heterozygous positives", (nextgenalleles.count((1 , 0))))
	print("No of other heterozygous positives",nextgenalleles.count((0 , 1)))
	print("No of homozygous positives",nextgenalleles.count((1 , 1)))
	#print(sum(nextgenallele1+ nextgenallele2, "this is the total")) # marked for deletion			
	storecountpositivehetero =+ nextgenalleles.count((1 , 0)) + nextgenalleles.count((0 , 1))
	storecountnegativehomo=+ nextgenalleles.count((0 , 0))
	storecountpositivehomo =+ nextgenalleles.count((1 , 1))
	print("total homo negatives ", storecountnegativehomo)
	print("total hetero positives", storecountpositivehetero)
	print("total homo positives", storecountpositivehomo)
	print("the number of dead kids",sum(storecountdeadkids))
	if thisgenalleles == []:
		generations(generationtime,thisgenalleles,nextgenalleles,father,mother,averagefamilysize,child,storecountdeadkids)
	else:
		print("go to next gen")

def runsim(startprevalence,startpopulationsize,generationtime,averagefamilysize):
	#global nextgenallele1 # to be deleted 
	#global nextgenallele2 #to be deleted
	#global storecountdeadkids
	class father: #sets the attributes of the father
		allele1 = 0
		allele2 = 0
		phenotype = (allele1, allele2)
	class mother:#sets mother attributes
		allele1 = 0
		allele2 = 0
		phenotype = (allele1, allele2)
		sensitised = 0
	class child: #sets child attributes, which will be inherited randomly from father and mother
		allele1 = 0
		allele2 = 0
		phenotype = (allele1, allele2)
	#class storecount
	d = {0: 'rh', 1: 'Rh'}
	positivechance = random.randint(1,100)
	#if negativechance < startprevalence: # if below this number, 
		#print("this works" + str(negativechance))
	for x in range (0, startpopulationsize):
		positivechance = random.randint(0,100)
		if positivechance <= startprevalence:
				father.allele1 = 1
		else:
				father.allele1 = 0
		print(positivechance, ("this is the positive chance in for dads first allele in  family" +str(x+1)))# for testing purposes you can comment these out later for clean results
		positivechance = random.randint(0,100)
		if positivechance <= startprevalence:
				#print(positivechance)
				father.allele2 = 1
		else:
				father.allele2 = 0
		print(positivechance, ("this is the positive chance in for dads second allele in  family" +str(x+1)))# for testing purposes you can comment these out later for clean results
		father.phenotype = (father.allele1, father.allele2)
		print(father.phenotype, ("this is father phenotype"))# for testing purposes you can comment these out later for clean results
		positivechance = random.randint(0,100)
		if positivechance <= startprevalence:
				#print(positivechance)
				mother.allele1 = 1
		else:
				mother.allele1 = 0
		print(positivechance, ("this is the positive chance in for mums first allele in  family" +str(x+1)))# for testing purposes you can comment these out later for clean results
		positivechance = random.randint(0,100)
		if positivechance <= startprevalence:
				#print(positivechance)
				mother.allele2 =1
		else:
				mother.allele2 = 0		
		print(positivechance, ("this is the positive chance in for mums second allele in  family" +str(x+1)))# for testing purposes you can comment these out later for clean results
		mother.phenotype = (mother.allele1, mother.allele2)
		print(mother.phenotype, ("this is mother phenotype")) # for testing purposes you can comment these out later for clean results
		conception(averagefamilysize,child,father,mother,generationtime,storecountdeadkids)
	
def endresults(generationtime,nextgenalleles,storecountdeadkids):
	print("total generations:", generationtime)
	hozp =nextgenalleles.count((1, 1))
	hetz1 = nextgenalleles.count((1, 0))
	hetz2 = nextgenalleles.count((0, 1))
	hozn =nextgenalleles.count((0, 0))
	totalpos = ((hozp+0.5*hetz1+ 0.5*hetz2)/len(nextgenalleles))
	print("the end proportion of positive alleles is", totalpos)
	exit()
	

def generations(generationtime,thisgenalleles,nextgenalleles,father,mother,averagefamilysize,child,storecountdeadkids):
	for x in range(0, generationtime):
		print("this is generation number", 0-generationtime)
		print(nextgenalleles)
		if nextgenalleles and all(elem == (1, 1) for elem in nextgenalleles):
			endresults(generationtime,nextgenalleles,storecountdeadkids)
		elif nextgenalleles and all(elem ==(0,0) for elem in nextgenalleles):
			endresults(generationtime,nextgenalleles,storecountdeadkids)
		"""positives = [(1, 1), (1, 0), (0, 1)] #-stuck on this =++===-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
		negatives = [(0, 0), (0, 1), (1, 0)]
		if any(positives) in nextgenalleles:
			print("keep going")	
		elif any(negatives) in nextgenalleles:
			print("keep going")
		else:
			endresults()"""
		print("working check alleles from last gen before clear",thisgenalleles) # working check can be deleleted later
		print("working check alleles from list next gen",nextgenalleles) # working check can be deleted later
		thisgenalleles.clear()
		thisgenalleles.extend(nextgenalleles)
		nextgenalleles.clear()
		print("working check alleles from last gen",thisgenalleles)# working check can be deleted later
		for x in range(0, len(thisgenalleles)):
			while len(thisgenalleles)-1 >2:	
				matchmaker = random.randint(0 , len(thisgenalleles) -1)
				print(matchmaker)
				father.phenotype = thisgenalleles[matchmaker]
				father.allele1 = father.phenotype[0]
				father.allele2 = father.phenotype[1]
				print(thisgenalleles[matchmaker], "this is the matchmaker working")
				print("this is this is thisgenallelesmatchmaker",thisgenalleles[matchmaker])
				print("this is father phenotype", father.phenotype)
				thisgenalleles.pop(matchmaker)
				matchmaker = random.randint(0 , len(thisgenalleles) -1)
				mother.phenotype = thisgenalleles[matchmaker]
				mother.allele1 = mother.phenotype[0]
				mother.allele2 = mother.phenotype[1]
				print(thisgenalleles[matchmaker], "this is the matchmaker working")
				thisgenalleles.pop(matchmaker)
				print("this is workings", generationtime) # working check can be deleted later
				conception(averagefamilysize,child,father,mother,generationtime,storecountdeadkids)
	endresults(generationtime,nextgenalleles,storecountdeadkids)
startchoices()


"""you will need a for loop for each child, nested in a for loop for population size, then you need to figure out how to incorporate the new data into the next generation."""
