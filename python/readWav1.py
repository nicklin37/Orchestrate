#Jeffrey Zhu
#Hack on the Hill IV
#Reading Wav Files

import wave, struct
import numpy, numpy.fft as fft
import array
import librosa

waveFile = wave.open('c.wav', 'r')

length = waveFile.getnframes()

waveInfo = []
waveMag = []

data = struct.unpack('h', '\xfd\xfe')
print data[0]

for i in range(0,length):
    waveData = waveFile.readframes(1)
    data = struct.unpack('<i', waveData)
    #print data
    #int test = data
    if(data[0] != 0):
    	print librosa.hz_to_note(int(data[0])
    #waveInfo.append(int(data[0])
#for i in range(0,len(waveInfo)):
#	print (fft.fft2(waveInfo[i]))
	#waveMag.append(fft.fft2(waveInfo[i]))
#print fft.fft2(waveInfo)
#print waveMag[0]
