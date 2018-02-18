#Jeffrey Zhu
#Hack on the Hill IV
#Reading Wav Files

#from __future__ import print_function
from __future__ import print_function
import wave, struct
import numpy, numpy.fft as fft
import array
import librosa


filename = "Sorrywav.wav"

y, sr = librosa.load(filename)

tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr)

final = ('{:.2f}'.format(tempo))

#print('Estimated tempo: {:.2f} beats per minute'.format(tempo))

# beat_times = librosa.frames_to_time(beat_frames, sr=sr)

# print('Saving output to beat_times.csv')
# librosa.output.times_csv('beat_times.csv', beat_times)

# frequencies = []

# notes = []

# finalNotes = []

# frequencies = (librosa.fft_frequencies(sr))

# for i in range(0, len(frequencies)):
# 	if(frequencies[i] != 0):
# 		notes.append(librosa.hz_to_note(frequencies[i]))


# #for i in range(0, len(frequencies)):
# #	print(notes[i])

# for j in range(0, len(notes)):
# 	skip = 0
# 	for l in range(0, len(finalNotes)):
# 		if(notes[j] == finalNotes[l]):
# 			skip = 1
# 			break
# 	string = notes[j]
# 	counter = 0
# 	if (skip == 0):
# 		for i in range(0, len(notes)):
# 			if (notes[i] == string):
# 				counter += 1
# 			if (counter >= 10):
# 				finalNotes.append(notes[i])
# 				break
			

# for i in range(0, len(finalNotes)):
# 	print(finalNotes[i])


#waveFile = wave.open('c.wav', 'r')

#length = waveFile.getnframes()

# waveInfo = []
# waveMag = []

# for i in range(0,length)[::50]:
#     waveData = waveFile.readframes(1)
#     data = struct.unpack('<i', waveData)
#     #print int(data[0])
#     if(int(data[0]) > 0):
#     	#print int(data[0])
#     	waveInfo.append(int(data[0]))

# print waveInfo[0]
# print librosa.hz_to_note(waveInfo)

#print librosa.hz_to_note(librosa.fft_frequencies(waveInfo[0]))

#for i in range(0, len(waveInfo)):
#	waveMag.append(librosa.fft_frequencies(waveInfo[i]))
#	print librosa.fft_frequencies(waveInfo[i])

#if(int(data[0]) > 0):
#   	print librosa.hz_to_note(int(data[0]))
