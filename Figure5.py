import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import csv 
import math

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
	Y4 = []
	Y5 = []
	Y6 = []
	Y7 = []
	Y8 = []
	Y9 = []
	Y10 = []
	Y1err = []
	Y2err = []
	Y3err = []
	Y4err = []
	Y5err = []
	Y6err = []
	Y7err = []
	Y8err = []
	Y9err = []
	Y10err = []
	
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

			if (i == j) and (Manufacturer[pos-1] == 'Mercedes Benz'): 
				mean9ScorePerYear.append(ConditionScore[pos-1])

			if (i == j) and (Manufacturer[pos-1] == 'Scania'): 
				mean10ScorePerYear.append(ConditionScore[pos-1])



		# Calculate mean score per vehicle brand per year (control for exceptions)

		mean1 = np.mean(mean1ScorePerYear)
		std1 = np.std(mean1ScorePerYear,dtype=np.float64)
		if (math.isnan(mean1)): 
			mean1 = 0
			std1 = 0
		Y1.append(mean1)
		Y1err.append(std1)

		mean2 = np.mean(mean2ScorePerYear)
		std2 = np.std(mean2ScorePerYear,dtype=np.float64)
		if (math.isnan(mean2)): 
			mean2 = 0
			std2 = 0
		Y2.append(mean2)
		Y2err.append(std1)

		mean3 = np.mean(mean3ScorePerYear)
		std3 = np.std(mean3ScorePerYear,dtype=np.float64)
		if (math.isnan(mean3)): 
			mean3 = 0
			std3 = 0
		Y3.append(mean3)
		Y3err.append(std3)

		mean4 = np.mean(mean4ScorePerYear)
		std4 = np.std(mean4ScorePerYear,dtype=np.float64)
		if (math.isnan(mean4)): 
			mean4 = 0
			std4 = 0
		Y4.append(mean4)
		Y4err.append(std4)

		mean5 = np.mean(mean5ScorePerYear)
		std5 = np.std(mean5ScorePerYear,dtype=np.float64)
		if (math.isnan(mean5)): 
			mean5 = 0
			std5 = 0
		Y5.append(mean5)
		Y5err.append(std5)

		mean6 = np.mean(mean6ScorePerYear)
		std6 = np.std(mean6ScorePerYear,dtype=np.float64)
		if (math.isnan(mean6)): 
			mean6 = 0
			std6 = 0
		Y6.append(mean6)
		Y6err.append(std6)

		mean7 = np.mean(mean7ScorePerYear)
		std7 = np.std(mean7ScorePerYear,dtype=np.float64)
		if (math.isnan(mean7)): 
			mean7 = 0
			std7 = 0
		Y7.append(mean7)
		Y7err.append(std7)

		mean8 = np.mean(mean8ScorePerYear)
		std8 = np.std(mean8ScorePerYear,dtype=np.float64)
		if (math.isnan(mean8)): 
			mean8 = 0
			std8 = 0
		Y8.append(mean8)
		Y8err.append(std8)

		mean9 = np.mean(mean9ScorePerYear)
		std9 = np.std(mean9ScorePerYear,dtype=np.float64)
		if (math.isnan(mean9)): 
			mean9 = 0
			std9 = 0
		Y9.append(mean9)
		Y9err.append(std9)

		mean10 = np.mean(mean10ScorePerYear)
		std10 = np.std(mean10ScorePerYear,dtype=np.float64)
		if (math.isnan(mean10)): 
			mean10 = 0
			std10 = 0
		Y10.append(mean10)
		Y10err.append(std10)


        #print "Mean (1) \t = %f, error = %f %%" %(mean1,std1/mean1*100)
        #print "Mean (2) \t = %f, error = %f %%" %(mean2,std2/mean2*100)
        #print "Mean (3) \t = %f, error = %f %%" %(mean3,std3/mean3*100)
        #print "Mean (4) \t = %f, error = %f %%" %(mean4,std4/mean4*100)
        #print "Mean (5) \t = %f, error = %f %%" %(mean5,std5/mean5*100)
        #print "Mean (6) \t = %f, error = %f %%" %(mean6,std6/mean6*100)
        #print "Mean (7) \t = %f, error = %f %%" %(mean7,std7/mean7*100)
        #print "Mean (8) \t = %f, error = %f %%" %(mean8,std8/mean8*100)
        #print "Mean (9) \t = %f, error = %f %%" %(mean9,std9/mean9*100)
        #print "Mean (10)\t = %f, error = %f %%" %(mean10,std10/mean10*100)

		
m1 = np.mean(Y1)
m2 = np.mean(Y2)
m3 = np.mean(Y3)
m4 = np.mean(Y4)
m5 = np.mean(Y5)
m6 = np.mean(Y6)
m7 = np.mean(Y7)
m8 = np.mean(Y8)
m9 = np.mean(Y9)
m10 = np.mean(Y10)

print "1 = %f" %m1
print "2 = %f" %m2
print "3 = %f" %m3
print "4 = %f" %m4
print "5 = %f" %m5
print "6 = %f" %m6
print "7 = %f" %m7
print "8 = %f" %m8
print "9 = %f" %m9
print "10 = %f" %m10
		
N = 12
ind = np.arange(N)  # the x locations for the groups
width = 0.08 
shift = 0.08
fig, ax = plt.subplots()

rects1 = ax.bar(ind+shift, Y1, width, color='lightgrey' )
rects2 = ax.bar(ind+width+shift, Y2, width, color='blue' )
rects3 = ax.bar(ind+2*width+shift, Y3, width, color='lightgreen' )
rects4 = ax.bar(ind+3*width+shift, Y4, width, color='red' )
rects5 = ax.bar(ind+4*width+shift, Y5, width, color='khaki' )
rects6 = ax.bar(ind+5*width+shift, Y6, width, color='purple' )
rects7 = ax.bar(ind+6*width+shift, Y7, width, color='cyan' )
rects8 = ax.bar(ind+7*width+shift, Y8, width, color='orange' )
rects9 = ax.bar(ind+8*width+shift, Y9, width, color='lemonchiffon' )
rects10 = ax.bar(ind+9*width+shift, Y10, width, color='brown', )

ax.set_xticks(ind + 0.5)
ax.set_xticklabels(('2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012'))
ax.legend((rects1[0], rects2[0], rects3[0], rects4[0], rects5[0], rects6[0], rects7[0], rects8[0], rects9[0], rects10[0]), 
('Volkswagen', 'DAF', 'Iveco', 'Renault', 'Ford', 'MAN','Fiat', 'Volvo', 'Mercedes Benz', 'Scania'), prop={'size':12}, bbox_to_anchor=(0.35, 1.1), loc=2, borderaxespad=0.)


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
