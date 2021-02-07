import matplotlib.pyplot as plt
from matplotlib.markers import MarkerStyle
from matplotlib import patches

# from http://gregsurges.com/post/90076189091/python-zplane

z = np.array([])
p = np.array([0,-1/2])
fig = plt.figure(figsize=(6, 6))
ax = plt.subplot(1,1,1)
ax.set_facecolor("#529dcd")
unit_circle = patches.Circle((0,0), radius=1, fill=False, gid = "$|z| = 1$",
                                 lw = 1.5,color='black', ls='dotted', alpha=0.9)
ax.add_patch(unit_circle)

unit_circle = patches.Circle((0,0), radius=np.max(np.abs(p)), fill=True,
                                ec = 'black', color='white', ls='solid', alpha=1)
ax.add_patch(unit_circle)
# plt.axvline(0, color='0.7')
# plt.axhline(0, color='0.7')
plt.xlim((-2, 2))
plt.ylim((-2, 2))


plt.plot(z.real, z.imag, 'ko', fillstyle='none', ms = 10)
plt.plot(p.real, p.imag, 'kx', fillstyle='none', ms = 10)
plt.show()
#If using termux
#plt.savefig('../figs/zplot.pdf')
#plt.savefig('../figs/zplot.eps')
#subprocess.run(shlex.split("termux-open ../figs/zplot.pdf"))
#else
#plt.show()