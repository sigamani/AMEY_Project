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
	

	for j in years:

		pos = 0
		mean1ScorePerYear = []
		mean2ScorePerYear = []
		mean3ScorePerYear = []


		for i in FinancialYear: 
		
			pos = pos + 1
	
			if (i == j) and (VehicleType[pos-1] == 'Heavy Goods Vehicle'): 
				mean1ScorePerYear.append(ConditionScore[pos-1])

			if (i == j) and (VehicleType[pos-1] == 'Light Goods Vehicle'): 
				mean2ScorePerYear.append(ConditionScore[pos-1])

			if (i == j) and (VehicleType[pos-1] == 'Personnel Vehicle'): 
				mean3ScorePerYear.append(ConditionScore[pos-1])


		# Calculate mean score per vehicle type per year
		mean1 = reduce(lambda x, y: x + y, mean1ScorePerYear) / float(len(mean1ScorePerYear))	
		Y1.append(mean1)

		mean2 = reduce(lambda x, y: x + y, mean2ScorePerYear) / float(len(mean2ScorePerYear))	
		Y2.append(mean2)

		mean3 = reduce(lambda x, y: x + y, mean3ScorePerYear) / float(len(mean3ScorePerYear))	
		Y3.append(mean3)
	
	
#yerr = 0.1 + 0.2*np.sqrt(Y3)
#xerr = 0.1 + yerr

#Overlay plots
plt.plot(years, Y1)
plt.plot(years, Y2)
plt.plot(years, Y3)
#plt.errorbar(years, Y3, xerr=0.2, yerr=0.4)
plt.plot(years, Y1, '-r', label='Heavy Goods Vehicle', linewidth=2.0)
plt.plot(years, Y2, '-g', label='Light Goods Vehicle', linewidth=2.0)
plt.plot(years, Y3, '-b', label='Personnel Vehicle', linewidth=2.0)
plt.legend(loc='upper right')
plt.ylim((0,100))
plt.xlabel("Time (year)")
plt.ylabel("Mean Conditional Score")
leg = plt.legend()
leg.get_frame().set_linewidth(0.0)
plt.show()
