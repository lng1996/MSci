# Code source: Patrick Kunzmann
# License: BSD 3 clause

import biotite
import biotite.structure as struc
import biotite.structure.io as strucio
import biotite.structure.io.xtc as xtc
import numpy as np
import matplotlib.pyplot as plt

# Put here the path of the downloaded files
templ_file_path = "s1x1i.pdb"
traj_file_path  = "s1x1whole.xtc"

templ_file_path2 = "s1x2i.pdb"
traj_file_path2  = "s1x2whole.xtc"

templ_file_path3 = "s1x3i.pdb"
traj_file_path3  = "s1x3whole.xtc"

# Gromacs does not set the element symbol in its PDB files,
# but Biotite guesses the element names from the atom names,
# emitting a warning
template = strucio.load_structure(templ_file_path)
template2 = strucio.load_structure(templ_file_path2)
template3 = strucio.load_structure(templ_file_path3)
# The structure still has water and ions, that are not needed for our
# calculations, we are only interested in the protein itself
# These are removed for the sake of computational speed using a boolean
# mask
# protein_mask = struc.filter_amino_acids(template)
# template = template[protein_mask]
# We could have loaded the trajectory also with
# 'strucio.load_structure()', but in this case we only want to load
# those coordinates that belong to the already selected atoms of the
# template structure.
# Hence, we use the 'XTCFile' class directly to load the trajectory
# This gives us the additional option that allows us to select the
# coordinates belonging to the amino acids.
xtc_file = xtc.XTCFile.read(traj_file_path, atom_i=np.where(template)[0])
trajectory = xtc_file.get_structure(template)

xtc_file2 = xtc.XTCFile.read(traj_file_path2, atom_i=np.where(template2)[0])
trajectory2 = xtc_file2.get_structure(template2)

xtc_file3 = xtc.XTCFile.read(traj_file_path3, atom_i=np.where(template3)[0])
trajectory3 = xtc_file3.get_structure(template3)
# Get simulation time for plotting purposes
time = xtc_file.get_time()

# trajectory, transform = struc.superimpose(trajectory[0], trajectory)
# rmsd = struc.rmsd(trajectory[0], trajectory)

# trajectory2, transform = struc.superimpose(trajectory2[0], trajectory2)
# rmsd2 = struc.rmsd(trajectory2[0], trajectory2)

# trajectory3, transform = struc.superimpose(trajectory3[0], trajectory3)
# rmsd3 = struc.rmsd(trajectory3[0], trajectory3)

# figure = plt.figure(figsize=(6,3))
# ax = figure.add_subplot(111)
# ax.plot(time, rmsd, color=biotite.colors["dimorange"])
# ax.plot(time, rmsd2, color=biotite.colors["brightorange"])
# ax.plot(time, rmsd3, color=biotite.colors["lightgreen"])
# ax.set_xlim(time[100], time[-1])
# ax.set_ylim(10, 24)
# ax.set_title("S1X1 Dimer")
# ax.set_xlabel("Time (ps)")
# ax.set_ylabel("RMSD (Å)")
# figure.tight_layout()
# plt.grid(color='purple', linestyle='--', linewidth=1)
# plt.show()


# radius = struc.gyration_radius(trajectory)
# radius2 = struc.gyration_radius(trajectory2)
# radius3 = struc.gyration_radius(trajectory3)


# figure = plt.figure(figsize=(6,3))
# ax = figure.add_subplot(111)
# ax.plot(time, radius, color=biotite.colors["dimorange"])
# ax.plot(time, radius2, color=biotite.colors["brightorange"])
# ax.plot(time, radius3, color=biotite.colors["lightgreen"])
# ax.set_xlim(time[0], time[-1])
# # ax.set_ylim(14.0, 14.5)
# ax.set_title("S1X1 Dimer")
# ax.set_xlabel("Time (ps)")
# ax.set_ylabel("Radius of gyration (Å)")
# figure.tight_layout()
# plt.grid(color='purple', linestyle='--', linewidth=1)
# plt.show()


ca_trajectory = trajectory[:, trajectory.atom_name == "CA"]
rmsf = struc.rmsf(struc.average(ca_trajectory), ca_trajectory)

ca_trajectory = trajectory2[:, trajectory2.atom_name == "CA"]
rmsf2 = struc.rmsf(struc.average(ca_trajectory), ca_trajectory)

ca_trajectory = trajectory3[:, trajectory3.atom_name == "CA"]
rmsf3 = struc.rmsf(struc.average(ca_trajectory), ca_trajectory)

figure = plt.figure(figsize=(6,3))
ax = figure.add_subplot(111)
res_count = struc.get_residue_count(trajectory)
# ax.plot(np.arange(1, res_count+1), rmsf, color=biotite.colors["dimorange"])
ax.plot(range(1, 38), rmsf[39:76], color=biotite.colors["dimorange"])
ax.plot(range(1, 36), rmsf2[37:72], color=biotite.colors["dimorange"])
ax.plot(range(1, 38), rmsf3[37:76], color=biotite.colors["dimorange"])
ax.set_xlim(1, 38)
# ax.set_ylim(0, 1.5)
ax.set_title("S1X(1-3) Dimers (Chains B)")
ax.set_xlabel("Residue")
ax.set_ylabel("RMSF (Å)")
figure.tight_layout()

plt.grid(color='green', linestyle='--', linewidth=0.5)
plt.show()