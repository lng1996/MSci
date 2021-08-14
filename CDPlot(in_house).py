import matplotlib.pyplot as plt
import csv
import numpy as np

x = []
y1 = []
y2 = []
y3 = []
y4 = []
y5 = []
y6 = []
y7 = []
y8 = []

# z=[]
# f=[]

# with open('m1.csv','r') as csvfile:
#     plots = csv.reader(csvfile, delimiter=',')
#     for column in plots:
#         z.append(float(column[0]))
#         f.append(float(column[1]))


with open('ch1.csv','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for column in plots:
        x.append(float(column[0]))
        y1.append(float(column[1]))
        y2.append(float(column[2]))
        y3.append(float(column[3]))
        y4.append(float(column[4]))
        y5.append(float(column[5]))
        y6.append(float(column[6]))
        y7.append(float(column[7]))
        y8.append(float(column[8]))


plt.rcParams['axes.facecolor'] = 'white'
plt.rcParams['axes.edgecolor'] = 'white'
plt.rcParams['axes.grid'] = True
plt.rcParams['grid.alpha'] = 1
plt.rcParams['grid.color'] = "#cccccc"

STD = [20,30,40,50,60,70,80]
STI = [np.mean(y8),np.mean(y7),np.mean(y6),np.mean(y5),np.mean(y2),np.mean(y3),np.mean(y4)]

# plt.plot(x,y1, label='(20℃)')
# plt.plot(80,np.mean(y4),'bo', label='80°C')
# plt.plot(70,np.mean(y3),'bo', label='70°C')
# plt.plot(60,np.mean(y2),'bo',label='60°C')
# plt.plot(50,np.mean(y5),'bo',label='50°C')
# plt.plot(40,np.mean(y6),'bo',label='40°')
# plt.plot(30,np.mean(y7),'bo',label='30°C')
# plt.plot(20,np.mean(y8),'bo',label='20°C')
# plt.plot(z,f, label='Initial Value (20°C)')
plt.plot(STD,STI, label = 'Average Absorption Values')

leg = plt.legend()

leg_lines = leg.get_lines()
leg_texts = leg.get_texts()
# bulk-set the properties of all lines and texts
plt.setp(leg_lines, linewidth=0.5)

ax = plt.gca()

plt.xlabel('Temperature (°C)')
plt.ylabel('Molar Ellipticity (deg×cm2/dmol)')
plt.title('αβ-2 Peptide (100μM solution with PB) Melt Spectral Curve')
plt.legend()
plt.show()