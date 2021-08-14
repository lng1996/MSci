from __future__ import print_function
import pylab
import numpy as np
import mdtraj as md
import matplotlib.pyplot as plt

trajectory = md.load('s1x1whole.xtc', top = 's1x1i.pdb')
sasa = md.shrake_rupley(trajectory)

trajectory2 = md.load('s1x2whole.xtc', top = 's1x2i.pdb')
sasa2 = md.shrake_rupley(trajectory2)

trajectory3 = md.load('s1x3whole.xtc', top = 's1x3i.pdb')
sasa3 = md.shrake_rupley(trajectory3)


print(trajectory)
print('sasa data shape', sasa.shape)
#init_sasa = sasa[0]
total_sasa = sasa.sum(axis=1)/78.382614
print(total_sasa)
plt.plot(trajectory.time, total_sasa)

print(trajectory2)
print('sasa data shape', sasa2.shape)
#init_sasa = sasa[0]
total_sasa2 = sasa2.sum(axis=1)/78.382614
print(total_sasa)
plt.plot(trajectory2.time, total_sasa2)

print(trajectory3)
print('sasa data shape', sasa3.shape)
#init_sasa = sasa[0]
total_sasa3 = sasa3.sum(axis=1)/78.382614
print(total_sasa)
plt.plot(trajectory3.time, total_sasa3)



plt.title("S1X1 Dimer")
plt.xlabel('Time [ps]', size=16)
plt.ylabel('Total SASA', size=16)
# plt.legend([line1, line2, line3], ['S1X1', 'S1X2', 'S1X3'])
plt.grid(color='purple', linestyle='--', linewidth=1)
plt.show()





def autocorr(x):
    "Compute an autocorrelation with numpy"
    x = x - np.mean(x)
    result = np.correlate(x, x, mode='full')
    result = result[int(result.size/2):]
    return result / result[0]

plt.semilogx(trajectory.time, autocorr(total_sasa))
plt.semilogx(trajectory2.time, autocorr(total_sasa2))
plt.semilogx(trajectory3.time, autocorr(total_sasa3))
plt.title("S1X(1-3) Dimers")
plt.xlabel('Time [ps]', size=16)
plt.ylabel('SASA autocorrelation', size=16)
# plt.legend([line0, line1, line2], ['S1X1', 'S1X2', 'S1X3'])
plt.grid(color='purple', linestyle='--', linewidth=1)
plt.show()