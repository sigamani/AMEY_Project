import numpy as np
import matplotlib.pyplot as plt
import csv 


with open('VehicleData.csv.orig') as csvfile:

	readCSV = csv.reader(csvfile, delimiter=',') 


	VehicleID = []
	FinancialYear = []
	VehicleType = []
	Manufacturer = []
	ConditionScore = []

	for row in readCSV:

		#write rows into python lists
		VehicleID.append(row[0])
		FinancialYear.append(row[1])
		VehicleType.append(row[2])
		Manufacturer.append(row[3])
		ConditionScore.append(row[4])

		#convert to ints
		ConditionScore = map(int, ConditionScore)
		FinancialYear = map(int, FinancialYear) 


	years = [2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011]

	Y1 = []
	Y2 = []
	Y3 = []
	Y4 = []
	Y5 = []
	Y6 = []
	Y7 = []
	Y8 = []
	Y9 = []
	Y10 = []
	
	for j in years:

		pos = 0
		mean1ScorePerYear = []
		mean2ScorePerYear = []
		mean3ScorePerYear = []
		mean4ScorePerYear = []
		mean5ScorePerYear = []
		mean6ScorePerYear = []
		mean7ScorePerYear = []
		mean8ScorePerYear = []
		mean9ScorePerYear = []
		mean10ScorePerYear = []


		for i in FinancialYear: 
		
			pos = pos + 1
	
			if (i == j) and (Manufacturer[pos-1] == 'Volkswagen'): 
				mean1ScorePerYear.append(ConditionScore[pos-1])

			if (i == j) and (Manufacturer[pos-1] == 'DAF'): 
				mean2ScorePerYear.append(ConditionScore[pos-1])

			if (i == j) and (Manufacturer[pos-1] == 'Iveco'): 
				mean3ScorePerYear.append(ConditionScore[pos-1])

			if (i == j) and (Manufacturer[pos-1] == 'Renault'): 
				mean4ScorePerYear.append(ConditionScore[pos-1])

			if (i == j) and (Manufacturer[pos-1] == 'Ford'): 
				mean5ScorePerYear.append(ConditionScore[pos-1])

			if (i == j) and (Manufacturer[pos-1] == 'MAN'): 
				mean6ScorePerYear.append(ConditionScore[pos-1])

			if (i == j) and (Manufacturer[pos-1] == 'Fiat'): 
				mean7ScorePerYear.append(ConditionScore[pos-1])

			if (i == j) and (Manufacturer[pos-1] == 'Volvo'): 
				mean8ScorePerYear.append(ConditionScore[pos-1])

			#if (i == j) and (Manufacturer[pos-1] == 'Mercedes'): 
			#	mean9ScorePerYear.append(ConditionScore[pos-1])

			if (i == j) and (Manufacturer[pos-1] == 'Scania'): 
				mean10ScorePerYear.append(ConditionScore[pos-1])



		# Calculate mean score per vehicle type per year
		mean1 = reduce(lambda x, y: x + y, mean1ScorePerYear) / float(len(mean1ScorePerYear))	
		Y1.append(mean1)

		mean2 = reduce(lambda x, y: x + y, mean2ScorePerYear) / float(len(mean2ScorePerYear))	
		Y2.append(mean2)

		mean3 = reduce(lambda x, y: x + y, mean3ScorePerYear) / float(len(mean3ScorePerYear))	
		Y3.append(mean3)

		mean4 = reduce(lambda x, y: x + y, mean4ScorePerYear) / float(len(mean4ScorePerYear))	
		Y4.append(mean4)

		mean5 = reduce(lambda x, y: x + y, mean5ScorePerYear) / float(len(mean5ScorePerYear))	
		Y5.append(mean5)

		mean6 = reduce(lambda x, y: x + y, mean6ScorePerYear) / float(len(mean6ScorePerYear))	
		Y6.append(mean6)

		mean7 = reduce(lambda x, y: x + y, mean7ScorePerYear) / float(len(mean7ScorePerYear))	
		Y7.append(mean7)
	
		mean8 = reduce(lambda x, y: x + y, mean8ScorePerYear) / float(len(mean8ScorePerYear))	
		Y8.append(mean8)

		#mean9 = reduce(lambda x, y: x + y, mean9ScorePerYear) / float(len(mean9ScorePerYear))	
		#Y9.append(mean9)

		mean10 = reduce(lambda x, y: x + y, mean10ScorePerYear) / float(len(mean10ScorePerYear))	
		Y10.append(mean10)

	
#Overlay plots
plt.plot(years, Y1)
plt.plot(years, Y2)
plt.plot(years, Y3)
plt.plot(years, Y4)
plt.plot(years, Y5)
plt.plot(years, Y6)
plt.plot(years, Y7)
plt.plot(years, Y8)
#plt.plot(years, Y9)
plt.plot(years, Y10)
plt.show()
