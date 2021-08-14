from Bio.PDB.MMCIFParser import MMCIFParser
from Bio.PDB.MMCIF2Dict import MMCIF2Dict

path = 'C:/Users/Leo/Desktop/Disser/Computational/Jupyter/cif'
file_path = f'{path}/1vjt.cif'
parser = MMCIFParser()

structure = parser.get_structure('1vjt', file_path)

mmcif_dict = MMCIF2Dict(file_path)
full_id = residue.get_full_id()

print(full_id)