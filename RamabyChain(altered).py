import Bio.PDB
from Bio.PDB.Structure import Structure
from matplotlib import pyplot as plt
from sklearn.cluster import OPTICS, cluster_optics_dbscan
import numpy as np
import math
import os
from matplotlib.pyplot import Axes as ax

downloads_path = 'C:/Users/Leo/Desktop/S1UM/CL'
filename_list = os.listdir(downloads_path)
# psi_phi_list = []

font = {'family': 'serif',
        'color':  'black',
        'weight': 'heavy',
        'size': 16,
        }
for filename in filename_list:
    for model in Bio.PDB.PDBParser().get_structure("",f"{downloads_path}/{filename}") :
        for chain in model :
            poly = Bio.PDB.Polypeptide.Polypeptide(chain)
            print("Model %s Chain %s" % (str(model.id), str(chain.id)))
            # print(poly.get_phi_psi_list())
            psi_phi_list = poly.get_phi_psi_list()

            point_psi=[]
            point_phi=[]
            for point in psi_phi_list:
                if point[0] != None and point[1] != None:
                    point_psi.append(point[0]*180/math.pi)
                    point_phi.append(point[1]*180/math.pi)
            #print(len(point_phi))
      
            plt.ylabel("Psi", fontdict=font)
            plt.xlabel("Phi", fontdict=font)
            plt.title('S1 Monomer (0 [ns])', fontdict=font, loc='center', pad=None)
            plt.plot(point_psi,point_phi,'.')
    
    plt.grid(color='purple', linestyle='--', linewidth=1)
    plt.show()