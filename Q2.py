import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import csv


with open('VehicleData.csv') as csvfile:

	readCSV = csv.reader(csvfile, delimiter=',') 

	VehicleID = []
	FinancialYear = []
	VehicleType = []
	Manufacturer = []
	ConditionScore = []

	for row in readCSV:

		#write rows into python lists
		VehicleID.append(row[0])
		FinancialYear.append('20'+row[1][-2:]) # Just take the last characters
		VehicleType.append(row[2])
		Manufacturer.append(row[3])
		ConditionScore.append(row[4])

		#convert to ints
		ConditionScore = map(int, ConditionScore)
		FinancialYear = map(int, FinancialYear) 



	years = [2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012]
	Y = []
	Yerr = []

	for j in years:

		pos = 0
		meanScorePerYear = []
		for i in FinancialYear: 
		
			pos = pos + 1
		
			if (i == j): 
				meanScorePerYear.append(ConditionScore[pos-1])

		mean = np.mean(meanScorePerYear)
		std = np.std(meanScorePerYear,dtype=np.float64)

		#write mean and standard dev into arrays to plot
		Y.append(mean)
		Yerr.append(std)
	
N = 12
ind = np.arange(N)  # the x locations for the groups
width = 0.9
fig, ax = plt.subplots()
rects1 = ax.bar(ind, Y, width, color='lightblue', yerr=Yerr, ecolor='black')

ax.set_xticks(ind + 0.5)
ax.set_xticklabels(('2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012'))


#Plot gridlines
ax = plt.gca()
ax.yaxis.grid(True)

#set fonts
font = {'family' : 'normal',
        'weight' : 'bold',
        'size'   : 18}
matplotlib.rc('font', **font)
matplotlib.rcParams.update({'font.size': 18})
plt.xlabel("Year")
plt.ylabel("Mean Conditional Score")
plt.ylim((0,100))
plt.show()
