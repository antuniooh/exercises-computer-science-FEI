#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Antonio Gustavo Muniz
#22.119.001 - 0

#Atividade 11


# In[1]:


from scipy import signal
import matplotlib.pyplot as plt
import numpy as np
from scipy.fftpack import fft, ifft

Fs=100
T=1/Fs
N=64
x =np.linspace(0.0,N*T,N)
signal.square

y=10*np.cos(25*2.0*np.pi*x)
yf=fft(y)
xf=np.linspace(0.0,1.0/(2.0*T),N//2)

plt.figure(1)
plt.title("Signal original")
plt.plot(x,y)
plt.axis([0,1,-1,1])
plt.show()

plt.figure(2)
plt.title("Signal FFT")
plt.plot(xf,2.0/N*np.abs(yf[0:N//2]))
plt.axis([0,50,0,1])
plt.show()


# In[2]:


from scipy import signal
import matplotlib.pyplot as plt
import numpy as np
from scipy.fftpack import fft, ifft

Fs=50
T=1/Fs
N=1024
x =np.linspace(0.0,N*T,N)
y=10 +2*np.cos(2*np.pi*2*x) + 1*np.cos(2*np.pi*30*x)
yf=fft(y)
xf=np.linspace(0.0,1.0/(2.0*T),N//2)

plt.figure(1)
plt.title("Signal original")
plt.plot(x,y)
plt.axis([0,1,0,15])
plt.show()

plt.figure(2)
plt.title("Signal FFT")
plt.plot(xf,2.0/N*np.abs(yf[0:N//2]))
plt.axis([0,50,0,1])
plt.show()


# In[6]:


from scipy.io import wavfile
from scipy import signal
import matplotlib.pyplot as plt
import numpy as np
from scipy.fftpack import fft, ifft

Fs, data=wavfile.read('musica.wav')
Fs=4096
nfft=1024

plt.figure(figsize=(7,5))
plt.specgram(data, nfft, Fs,noverlap=7*nfft//8)
plt.xlabel('tempo [s]')
plt.ylabel('frequencia [hz]')
plt.show()

plt.title("Periodograma de voz")
f, Pxx_den = signal.periodogram(data,Fs)
plt.plot(f, Pxx_den)
plt.axis([80,140,0,5000])
plt.xlabel('frequency')
plt.ylabel('power')
plt.show()


# In[ ]:




