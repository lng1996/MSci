import MDAnalysis as mda
from MDAnalysis.analysis import dihedrals
from MDAnalysis.core import groups
import matplotlib.pyplot as plt
import numpy as np
#%matplotlib inline

dir_str = "C:/Users/Leo/Desktop/"
gro = f'{dir_str}/step4.1_equilibration.gro'
xtc = f'{dir_str}/step5_production.xtc'

u = mda.Universe(gro, xtc)
protein = u.select_atoms('protein')
print('There are {} residues in the protein'.format(len(protein.residues)))
print(protein.residues)
for res in protein.residues[1:36]:
    phi = res.phi_selection()
    if phi is None:
        print('R'+res)
        names = None
    else:
        names = phi.names
    print('{}: {} '.format(res.resname, names))
for res in protein.residues[1:36]: 
    
    omegas = res.omega_selection() 
    if omegas is None: 
        names = None 
        print('Big Oof')
    else: 
        names = omegas.names 
    print('{}: {} '.format(res.resname, names))

    omegas = [res.omega_selection() for res in protein.residues[1:36]]
for i in range(36):
    if omegas[i] is None:
        print('Big Oof')
    else:
        print(omegas[i].dihedral.value(),i)

dihs = dihedrals.Dihedral(omegas).run()
print(dihs.angles.shape)

labels = ['Res {}'.format(n) for n in np.arange(1, 33)]
for ang, label in zip(dihs.angles.T, labels):
    plt.plot(ang, label=label)
plt.xlabel('Frame')
plt.ylabel('Angle (degrees)')
plt.legend()