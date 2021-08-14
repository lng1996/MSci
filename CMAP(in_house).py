import Bio.PDB
import numpy
import pylab
import matplotlib.pyplot as plt
import matplotlib

def calc_residue_dist(residue_one, residue_two):
    """Returns the C-alpha distance between two residues"""
    diff_vector  = residue_one["CA"].coord - residue_two["CA"].coord
    return numpy.sqrt(numpy.sum(diff_vector * diff_vector))

def calc_dist_matrix(chain_one, chain_two):
    """Returns a matrix of C-alpha distances between two chains"""
    answer = numpy.zeros((len(chain_one), len(chain_two)), numpy.float)
    for row, residue_one in enumerate(chain_one) :
        for col, residue_two in enumerate(chain_two) :
            answer[row, col] = calc_residue_dist(residue_one, residue_two)
    return answer

structure = Bio.PDB.PDBParser().get_structure('now', 's1x1f.pdb')
#print(structure.header)
model = structure[0]
#print(model.get_chains())
dist_matrix = calc_dist_matrix(model["A"], model["B"])

dist_matrix = list(dist_matrix)

for i in range(len(dist_matrix)):
    dist_matrix[i] = list(dist_matrix[i])
# for i in range(len(dist_matrix)):
#     for j in range(len(dist_matrix[i])):
#         print(dist_matrix[i][j])
#         if dist_matrix[i][j] < 10.0 and dist_matrix[i][j] > 0.0:
#             dist_matrix[i][j] = False
#         else:
#             dist_matrix[i][j] = True

print(dist_matrix)
contact_map = dist_matrix

print(type(contact_map))
print("Minimum distance", numpy.min(dist_matrix))
print("Maximum distance", numpy.max(dist_matrix))
plt.title("S1X1 Dimer (A,B)")
plt.imshow(numpy.transpose(dist_matrix),cmap='Greys')
plt.colorbar().set_label('Interaction Distance')
plt.show()

# plt.colorbar().set_label('Interaction Distance')
# pylab.hsv()
# pylab.show()
# plt.imshow(dist_matrix)
# plt.show()
# """ pylab.matshow(numpy.transpose(contact_map))
# pylab.colorbar()
# pylab.show( """