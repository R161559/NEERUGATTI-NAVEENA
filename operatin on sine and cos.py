# a program to generate sine , cosine fuctions and to do some of the operations on them 
import numpy as np
import matplotlib.pyplot as plt
x=np.arange(0,3*np.pi,0.1)
y=np.sin(x)
plt.subplot(5,1,1)
plt.plot(x,y,'r')
plt.title('sine')
plt.xlabel('amplitude')
plt.ylabel('time')
z=np.cos(x)
plt.subplot(5,1,2)
plt.plot(x,z,'b')
plt.title('cosine')
plt.xlabel('amplitude')
plt.ylabel('time')
k=y+z
plt.subplot(5,1,3)
plt.plot(x,k,'*')
plt.title('sum of sine and cosine')
plt.xlabel('amplitude')
plt.ylabel('time')

sub=y-z
plt.subplot(5,1,4)
plt.plot(x,sub,'g')
plt.title('subtraction of sine amd cos')
plt.xlabel('amplitude')
plt.ylabel('time')

mul=y*z
plt.subplot(5,1,5)
plt.plot(x,mul,'y')
plt.title('multiplication of two signals')
plt.xlabel('amplitude')
plt.ylabel('time')
plt.show()


