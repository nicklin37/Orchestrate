import cmath
import numpy as np
 
def omega(p, q):
   return cmath.exp((2.0 * cmath.pi * 1j * q) / p)



def fft(signal):
   n = len(signal)
   if n == 1:
      return signal
   else:
      Feven = fft([signal[i] for i in xrange(0, n, 2)])
      Fodd = fft([signal[i] for i in xrange(1, n, 2)])
 
      combined = [0] * n
      for m in xrange(n/2):
         combined[m] = Feven[m] + omega(n, -m) * Fodd[m]
         combined[m + n/2] = Feven[m] - omega(n, -m) * Fodd[m]
 
      return combined


print fft([0,1,0,0])
print fft([1.0, 2.0, 1.0, -1.0, 1.5])


x = np.array([1.0, 2.0, 1.0, -1.0, 1.5])
y = fft(x)
y
