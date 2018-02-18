#Jeffrey Zhu
#Hack on the Hill IV
#Reading Wav Files

import wave, struct
import numpy, numpy.fft as fft
import array
import librosa
import pyaudio

waveFile = wave.open('c.wav', 'r',format=pyaudio.paInt16,
                                channels=1,
                                rate=FSAMP,
                                input=True,
                                frames_per_buffer=FRAME_SIZE)

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

# Shift the buffer down and new data in
buf[:-FRAME_SIZE] = buf[FRAME_SIZE:]
buf[-FRAME_SIZE:] = np.fromstring(waveFile.read(FRAME_SIZE), np.int16)

# Run the FFT on the windowed buffer
fft = np.fft.rfft(buf * window)

# Get frequency of maximum response in range
freq = (np.abs(fft[imin:imax]).argmax() + imin) * FREQ_STEP

# Get note number and nearest note
n = freq_to_number(freq)
n0 = int(round(n))

# Console output once we have a full buffer
num_frames += 1

if num_frames >= FRAMES_PER_FFT:
    if ('{:7.2f}' > 300):
        file.write('{:>3s} {:+.2f}'.format(
            freq, note_name(n0), n-n0)
    #waveInfo.append(int(data[0])
#for i in range(0,len(waveInfo)):
#	print (fft.fft2(waveInfo[i]))
	#waveMag.append(fft.fft2(waveInfo[i]))
#print fft.fft2(waveInfo)
#print waveMag[0]
