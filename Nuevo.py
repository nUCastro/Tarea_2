import sys
from math import *
import scipy.special as sp

import numpy as np
print 'Tiempo promedio en compilacion= 12s.'

#Se aplica [-1,1] debido a que la funcion erf se define como la integral entre 0 y oo.
#Para crear una normal(0,1) debemos tomar la otra parte, o sea, los numeros negativos.
a=np.random.uniform(-1,1,size=1000000)
c=[]


for i in range(len(a)):
	c.append(sp.erfinv(a[i])*sqrt(2))
import matplotlib.pyplot as plt
#Aqui hare la distribucion normal para comparar los datos anteriores.
b=np.linspace(int(min(c))-1,int(max(c))+1,100)

d=[]
for i in b:
	d.append((1.0/sqrt(2*pi))*exp(-(i**2)/2))
	
plt.plot(b,d,'-r',label="Distribucion normal")	
plt.hist(c,bins=100,normed=True,label="Datos provenientes de la uniforme")
plt.ylim((0,0.5))
plt.legend()
plt.show()
