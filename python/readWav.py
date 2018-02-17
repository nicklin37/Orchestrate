#Jeffrey Zhu
#Hack on the Hill IV
#Reading Wav Files

import wave, struct

waveFile = wave.open('eqt-major-sc.wav', 'r')

length = waveFile.getnframes()
for i in range(0,length):
    waveData = waveFile.readframes(1)
    data = struct.unpack("<i", waveData)
    print(int(data[0]))
