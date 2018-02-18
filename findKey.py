from collections import Counter
import librosa


filename = "Sorrywav.wav"

y, sr = librosa.load(filename)

tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr)

beat = ('{:.2f}'.format(tempo))

notes = []

file = open("writeto.txt", "r")

for line in file:
	line = line.strip()
	notes.append(line[:-1])


mCounter = Counter(notes)
finalkey = max(mCounter, key=mCounter.get)
distinct = set(notes)

CM = ["A", "B", "C", "D", "E", "F", "G"]

GM = ["A", "B", "C", "D", "E", "F#", "G"]

DM = ["A", "B", "C#", "D", "E", "F#", "G"]

AM = ["A", "B", "C#", "D", "E", "F#", "G#"]

EM = ["A", "B", "C#", "D#", "E", "F#", "G#"]

BM = ["A#", "B", "C#", "D#", "E", "F#", "G#"]

FSharp = ["A#", "B", "C#", "D#", "E#", "F#", "G#"]

CSharp = ["A#", "B#", "C#", "D#", "E#", "F#", "G#"]

FM = ["A#", "B", "C", "D", "E", "F", "G"]

BFlat = ["A#", "B", "C", "D#", "E", "F", "G"]

EFlat = ["A#", "B", "C", "D#", "E", "F", "G#"]

AFlat = ["A#", "B", "C#", "D#", "E", "F", "G#"]

print (finalkey + ' ' + beat)
#f = open("final.txt", "w")

#f.write(beat + '\n' + finalkey)

#f.close()
# keys = [CM, GM, DM, AM, EM, BM, FSharp, CSharp, FM, BFlat, EFlat, AFlat]
# counter = [0] * 12

# for note in distinct:
# 	for key in keys:
# 		if note in key:
# 			counter[keys.index(key)] += 1

# zipped = sorted(zip(counter, keys), reverse=True)
# print zipped


file.close()
