import Bio.PDB
from matplotlib import pyplot as plt
import math
from Bio.PDB import MMCIFParser
from Bio.PDB.Polypeptide import PPBuilder
from os import PathLike, walk
from pandas import DataFrame
import matplotlib
import numpy as np

def findseq(file_name):
    #location gives the location of the motif in the cif file
    location = []
    structure = Bio.PDB.MMCIFParser().get_structure(file_name.split('.')[0], file_name)

    ppb=PPBuilder()
    for pp in ppb.build_peptides(structure):
        # print(pp.get_sequence())
        #This gives the index of the 4-residue long beta sequence.
        # print(pp.get_sequence().find('RRWT'))
        location.append(pp.get_sequence().find('RRWT'))
    # print(location)
    return location

filenames = next(walk('.'), (None, None, []))[2] 
dih_list = []
for file in filenames:
    # print(file[-4:-0])
    if file[-4:-1] == '.ci':
        # print(file)
        findices = findseq(file)
        count = 0
        for model in Bio.PDB.MMCIFParser().get_structure(file.split('.')[0], file):
            for chain in model:
                try:
                    if findices[count] != -1:
                        poly = Bio.PDB.Polypeptide.Polypeptide(chain)
                        # print("Model %s Chain %s" % (str(model.id), str(chain.id)))
                        getstruc = poly.get_phi_psi_list()
                        dih_list.extend(getstruc[findices[count]:findices[count]+3])
                    count += 1
                except: 
                    break
print(len(dih_list))
delind = []
for i in range(len(dih_list)):
    if dih_list[i][0] == None or dih_list[i][1] == None:
        delind.append(i)
for j in delind: 
    del dih_list[j]

Phi = []
Psi = []
for i in range(len(dih_list)):
    try:
        Phi.append(math.degrees(dih_list[i][0]))
        Psi.append(math.degrees(dih_list[i][1]))
    except:
        print(dih_list[i])
        break
print(Phi, Psi)

nb = 75

plt.hist2d(Phi, Psi, bins=nb, cmap='inferno')

cb = plt.colorbar()
cb.set_label('Number of Tuples')


plt.title('Heatmap of "RRWT" Motif Dihedrals')
plt.xlabel('Phi')
plt.ylabel('Psi')


plt.show()

