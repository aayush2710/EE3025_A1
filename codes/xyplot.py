import numpy as np
import matplotlib.pyplot as plt
#If using termux
import subprocess
import shlex
#end if


k = 25
x=np.array([1,1,2,4,3,1])
x=np.concatenate([x,np.zeros(19)])
y = np.zeros(k)
y[0] = x[0]
y[1] = -0.5*y[0]+x[1]
for n in range(2,k-1):
	y[n] = -0.5*y[n-1]+x[n]+x[n-2]

x_axis=np.linspace(0,24,25)
plt.figure(1)
plt.stem(x_axis[:11],x[:11])
plt.title('Input')
plt.xlabel('$n$')
plt.ylabel('$x(n)$')
plt.grid()
plt.savefig("fig_x.eps")
#If using termux
#plt.savefig('../figs/x_n.eps')
#plt.savefig('../figs/x_n.pdf')
#subprocess.run(shlex.split("termux-open ../figs/x_n.pdf"))
#end if
plt.figure(2)
plt.stem(x_axis,y)
plt.title('Bounded Output')
plt.xlabel('$n$')
plt.ylabel('$y(n)$')
plt.grid()
plt.savefig("fig_y.eps")
#If using termux
#plt.savefig('../figs/y_n.pdf')
#plt.savefig('../figs/y_n.eps')
#subprocess.run(shlex.split("termux-open ../figs/y_n.pdf"))
#else
#plt.show()

d=np.array([1,0,0,0,0,0])
d=np.concatenate([d,np.zeros(19)])
h = np.zeros(k)
h[0] = d[0]
h[1] = -0.5*h[0]+d[1]
for n in range(2,k-1):
	h[n] = -0.5*h[n-1]+d[n]+d[n-2]

plt.figure(3)
plt.stem(x_axis,h)
plt.title('Impulse Response')
plt.xlabel('$n$')
plt.ylabel('$h(n)$')
plt.grid()
plt.savefig("fig_h.eps")
#If using termux
#plt.savefig('../figs/h_n.pdf')
#plt.savefig('../figs/h_n.eps')
#subprocess.run(shlex.split("termux-open ../figs/h_n.pdf"))
#else
#plt.show()