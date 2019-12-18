#implementing the special functions
import numpy as np
import matplotlib.pyplot as plt
a=np.arange(1,4*np.pi,0.1)
x=np.exp(a)
plt.subplot(3,1,1) 
plt.plot(a,x,'*')
plt.xlabel('time')
plt.ylabel('amplitude')
plt.title('exponential function')
y=np.log(a)
plt.subplot(3,1,2)
plt.plot(a,y,'r')
plt.xlabel('time')
plt.ylabel('amplitude')
plt.title('logarithemic function')
z=np.tan(a)
plt.subplot(3,1,3)
plt.plot(a,z,'y')
plt.title('tan functio')
plt.xlabel('time')
plt.ylabel('amplitude')
plt.show()

