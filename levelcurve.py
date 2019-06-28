import matplotlib.pyplot as plt
import numpy as np

def LevelCurve(f,k=0,numk=3,ss=1,plotx=0,ploty=0,plotz=0,graphsize=10):
   for k in [x * ss for x in range(0, numk+2)]:
      graph(f,plotx,ploty,k,graphsize/2)
   plt.legend()
   plt.ylim(-graphsize,graphsize)
   plt.xlim(-graphsize,graphsize)
   plt.show()
   return

def graph(f,px,py,k,size):
   x=np.linspace(px-size,px+size,10000)
   plt.plot(x,f(x,k),label='k='+str(k))
