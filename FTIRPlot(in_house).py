import matplotlib.pyplot as plt
import csv

x = []
y1 = []



with open('A-b-2.csv','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for column in plots:
        x.append(float(column[0]))
        y1.append(float(column[1]))

# plt.plot(x,y1, label='(20℃)')
plt.rcParams['axes.facecolor'] = 'white'
plt.rcParams['axes.edgecolor'] = 'white'
plt.rcParams['axes.grid'] = True
plt.rcParams['grid.alpha'] = 1
plt.rcParams['grid.color'] = "#cccccc"
plt.plot(x,y1)


ax = plt.gca()

plt.xlabel('Wavenumber (cm^-1)')
plt.ylabel('Absorption Units')
plt.title('FTIR (100uM Alpha-Beta Peptide 2)')
plt.legend()
plt.show()