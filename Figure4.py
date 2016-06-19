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
	Y1 = []
	Y2 = []
	Y3 = []
	Y1err = []
	Y2err = []
	Y3err = []

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
		mean1 = np.mean(mean1ScorePerYear)
		std1 = np.std(mean1ScorePerYear,dtype=np.float64)
		Y1.append(mean1)
		Y1err.append(std1)

		mean2 = np.mean(mean2ScorePerYear)
		std2 = np.std(mean2ScorePerYear,dtype=np.float64)
		Y2.append(mean2)
		Y2err.append(std2)

		mean3 = np.mean(mean3ScorePerYear)
		std3 = np.std(mean3ScorePerYear,dtype=np.float64)
		Y3.append(mean3)
		Y3err.append(std3)

		#print "Mean (Heavy) \t = %f, error = %f %%" %(mean1,std1/mean1*100)
		#print "Mean (Light) \t = %f, error = %f %%" %(mean2,std2/mean2*100)
		#print "Mean (Personnel) \t = %f, error = %f %%" %(mean3,std3/mean3*100)

N = 12
ind = np.arange(N)  # the x locations for the groups
width = 0.25
fig, ax = plt.subplots()
rects1 = ax.bar(ind+0.15, Y1, width, color='orange', yerr=Y1err, ecolor='black')
rects2 = ax.bar(ind+width+0.15, Y2, width, color='darkolivegreen', yerr=Y2err, ecolor='black')
rects3 = ax.bar(ind+width+0.4, Y3, width, color='cyan', yerr=Y3err, ecolor='black')

ax.set_xticks(ind + 0.5)
ax.set_xticklabels(('2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012'))
ax.legend((rects1[0], rects2[0], rects3[0]), ('Heavy Goods Vehicle', 'Light Goods Vehicle', 'Personnel Vehicle'),bbox_to_anchor=(0.35, 1.1), loc=2, borderaxespad=0.)

#Plot gridlines
ax = plt.gca()
ax.yaxis.grid(True)

#set fonts
font = {'family' : 'normal',
        'weight' : 'bold',
        'size'   : 18}
matplotlib.rc('font', **font)
matplotlib.rcParams.update({'font.size': 18})
	
plt.ylim((0,100))
plt.xlabel("Year")
plt.ylabel("Mean Conditional Score")
plt.show()
