#Jeffrey Zhu
#Hack on the Hill IV
#Reading Wav Files

#from __future__ import print_function
import wave, struct
import numpy, numpy.fft as fft
import array
import librosa

# filename = librosa.util.example_audio_file()

# y, sr = librosa.load(filename)

# tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr)

# print('Estimated tempo: {:.2f} beats per minute'.format(tempo))

# beat_times = librosa.frames_to_time(beat_frames, sr=sr)

# print('Saving output to beat_times.csv')
# librosa.output.times_csv('beat_times.csv', beat_times)


waveFile = wave.open('c.wav', 'r')

length = waveFile.getnframes()

waveInfo = []
waveMag = []

for i in range(0,length)[::30]:
    waveData = waveFile.readframes(1)
    data = struct.unpack('<i', waveData)
    #print int(data[0])
    if(int(data[0]) > 0):
    	#print int(data[0])
    	waveInfo.append(int(data[0]))

print waveInfo[0]
print librosa.fft_frequencies(waveInfo[5])
print librosa.hz_to_note(waveInfo[0])

#print librosa.hz_to_note(librosa.fft_frequencies(waveInfo[0]))

#for i in range(0, len(waveInfo)):
#	waveMag.append(librosa.fft_frequencies(waveInfo[i]))
#	print librosa.fft_frequencies(waveInfo[i])

#if(int(data[0]) > 0):
#   	print librosa.hz_to_note(int(data[0]))
