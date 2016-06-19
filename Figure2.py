import numpy as np
import matplotlib 
import matplotlib.pyplot as plt
import matplotlib.lines as mlines
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
		FinancialYear.append('20'+row[1][-2:]) # Just take the last two characters
		VehicleType.append(row[2])
		Manufacturer.append(row[3])
		ConditionScore.append(row[4])

		#convert to ints 
		ConditionScore = map(int, ConditionScore)
		FinancialYear = map(int, FinancialYear) 


	#get sample size for each year 
	years = [2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012]
	Y = []

	for j in years:

		size = 0
		for i in FinancialYear: 

			if (i == j): 
				size = size + 1
				
		#print "Year %i : Sample size = %i" %(j,size)
		Y.append(size)


font = {'family' : 'normal',
        'weight' : 'bold',
        'size'   : 18}


N = 12 
ind = np.arange(N)  # the x locations for the groups
width = 0.9 
fig, ax = plt.subplots()
rects1 = ax.bar(ind, Y, width, color='lightblue')


#add some text for labels, title and axes ticks
ax.set_ylabel('Scores')
ax.set_xticks(ind + 0.5)
ax.set_xticklabels(('2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012'))

def autolabel(rects):
    # attach some text labels
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width()/2., 1.05*height,
                '%d' % int(height),
                ha='center', va='bottom')

autolabel(rects1)

matplotlib.rc('font', **font)
matplotlib.rcParams.update({'font.size': 18})
plt.xlabel("Year")
plt.ylabel("Sample Size")
plt.ylim((0,4000))
plt.show()
