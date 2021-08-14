import RamachanDraw

def DrawRam(pdb_file):
	# RamachanDraw.plot(pdb_file, cmap='viridis', alpha=0.75, dpi=100, save=True, show=False, out='C:/Users/lgorn/Desktop/Disser/Plots/'+str(pdb_file)+'.png')
	RamachanDraw.plot(pdb_file, cmap='viridis', alpha=0.75, dpi=1000, save=True, show=False, out=str(pdb_file)+'.png')
