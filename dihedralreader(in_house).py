import wget
from matplotlib import pyplot as plt
import csv



acclist=[]
psi_list = []
phi_list = []
with open('dihedalphatemp.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    # print(spamreader)
    for row in spamreader:
        psi_list.append(row[0])
        phi_list.append(row[1])
        # acclist.append(row[1].split(',')[0]])
# ele_load=list(set(acclist))
# print(ele_load)
max_psi = max(psi_list)
min_psi = min(psi_list)
max_phi = max(phi_list)
min_phi = min(phi_list)

print("Range of Psi:",min_psi,'-',max_psi)

print("Range of Phi:",min_phi,'-',max_phi)