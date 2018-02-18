from pydub import AudioSegment
from pydub.playback import play
import librosa
import sys

BEATSPERMEASURE = 4
LENSNARE = 0.189115646259
LENKICKBIG = 0.428571428571
LENKICKHEAVY = 0.716009070295
LENHIHAT = 0.241632653061
LENCLAP = 0.241632653061

# clap, sr = librosa.load("drums/clap.wav")
# print librosa.get_duration(clap, sr)
# snare, sr = librosa.load("drums/snare.wav")
# print librosa.get_duration(snare, sr)
# kick, sr = librosa.load("drums/kick-big.wav")
# print librosa.get_duration(kick, sr)
# kick, sr = librosa.load("drums/kick-heavy.wav")
# print librosa.get_duration(kick, sr)
# hat, sr = librosa.load("drums/hihat.wav")
# print librosa.get_duration(hat, sr)

#Piano
cScale = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
yC, srC = librosa.load("piano/wav/c.wav")
#yC = librosa.effects.time_stretch(yC, librosa.get_duration(yC, srC))
yCs, srCs = librosa.load("piano/wav/cs.wav")
#yCs = librosa.effects.time_stretch(yCs, librosa.get_duration(yCs, srCs))
yD, srD = librosa.load("piano/wav/d.wav")
#yD = librosa.effects.time_stretch(yD, librosa.get_duration(yD, srD))
yDs, srDs = librosa.load("piano/wav/ds.wav")
#yDs = librosa.effects.time_stretch(yDs, librosa.get_duration(yDs, srDs))
yE, srE = librosa.load("piano/wav/e.wav")
#yE = librosa.effects.time_stretch(yE, librosa.get_duration(yE, srE))
yF, srF = librosa.load("piano/wav/f.wav")
#yF = librosa.effects.time_stretch(yF, librosa.get_duration(yF, srF))
yFs, srFs = librosa.load("piano/wav/fs.wav")
#yFs = librosa.effects.time_stretch(yFs, librosa.get_duration(yFs, srFs))
yG, srG = librosa.load("piano/wav/g.wav")
#yG = librosa.effects.time_stretch(yG, librosa.get_duration(yG, srG))
yGs, srGs = librosa.load("piano/wav/gs.wav")
#yGs = librosa.effects.time_stretch(yGs, librosa.get_duration(yGs, srGs))
yA, srA = librosa.load("piano/wav/a.wav")
#yA = librosa.effects.time_stretch(yA, librosa.get_duration(yA, srA))
yAs, srAs = librosa.load("piano/wav/as.wav")
#yAs = librosa.effects.time_stretch(yAs, librosa.get_duration(yAs, srAs))
yB, srB = librosa.load("piano/wav/b.wav")
#yB = librosa.effects.time_stretch(yB, librosa.get_duration(yB, srB))
srPiano = srC
cScaleNotesP = [yC, yCs, yD, yDs, yE, yF, yFs, yG, yGs, yA, yAs, yB, librosa.effects.pitch_shift(yC, srPiano, n_steps=12), librosa.effects.pitch_shift(yCs, srPiano, n_steps=12), librosa.effects.pitch_shift(yD, srPiano, n_steps=12), librosa.effects.pitch_shift(yDs, srPiano, n_steps=12), librosa.effects.pitch_shift(yE, srPiano, n_steps=12), librosa.effects.pitch_shift(yF, srPiano, n_steps=12), librosa.effects.pitch_shift(yFs, srPiano, n_steps=12), librosa.effects.pitch_shift(yG, srPiano, n_steps=12), librosa.effects.pitch_shift(yGs, srPiano, n_steps=12), librosa.effects.pitch_shift(yA, srPiano, n_steps=12), librosa.effects.pitch_shift(yAs, srPiano, n_steps=12), librosa.effects.pitch_shift(yB, srPiano, n_steps=12), librosa.effects.pitch_shift(yC, srPiano, n_steps=24), librosa.effects.pitch_shift(yCs, srPiano, n_steps=24)]

#Bass
yC, srC = librosa.load("Octaver/Octaver-c1.wav")
yDs, srDs = librosa.load("Octaver/Octaver-d#1.wav")
yFs, srFs = librosa.load("Octaver/Octaver-f#1.wav")
yA, srA = librosa.load("Octaver/Octaver-a1.wav")
yC2, srC = librosa.load("Octaver/Octaver-c2.wav")
yDs2, srDs = librosa.load("Octaver/Octaver-d#2.wav")
yFs2, srFs = librosa.load("Octaver/Octaver-f#2.wav")
yA2, srA = librosa.load("Octaver/Octaver-a2.wav")
yC3, srC = librosa.load("Octaver/Octaver-c3.wav")
yDs3, srDs = librosa.load("Octaver/Octaver-d#3.wav")
yFs3, srFs = librosa.load("Octaver/Octaver-f#3.wav")
yA3, srA = librosa.load("Octaver/Octaver-a3.wav")
srBass = srC
cScaleNotesB = [yC, librosa.effects.pitch_shift(yC, srBass, n_steps=1), librosa.effects.pitch_shift(yC, srBass, n_steps=2), yDs, librosa.effects.pitch_shift(yDs, srBass, n_steps=1), librosa.effects.pitch_shift(yDs, srBass, n_steps=2), yFs, librosa.effects.pitch_shift(yFs, srBass, n_steps=1), librosa.effects.pitch_shift(yFs, srBass, n_steps=2), yA, librosa.effects.pitch_shift(yA, srBass, n_steps=1), librosa.effects.pitch_shift(yA, srBass, n_steps=2), yC2, librosa.effects.pitch_shift(yC2, srBass, n_steps=1), librosa.effects.pitch_shift(yC2, srBass, n_steps=2), yDs2, librosa.effects.pitch_shift(yDs2, srBass, n_steps=1), librosa.effects.pitch_shift(yDs2, srBass, n_steps=2), yFs2, librosa.effects.pitch_shift(yFs2, srBass, n_steps=1), librosa.effects.pitch_shift(yFs2, srBass, n_steps=2), yA2, librosa.effects.pitch_shift(yA2, srBass, n_steps=1), librosa.effects.pitch_shift(yA2, srBass, n_steps=2), yC3, librosa.effects.pitch_shift(yC3, srBass, n_steps=1), librosa.effects.pitch_shift(yC3, srBass, n_steps=2), yDs3, librosa.effects.pitch_shift(yDs3, srBass, n_steps=1), librosa.effects.pitch_shift(yDs3, srBass, n_steps=2), yFs3, librosa.effects.pitch_shift(yFs3, srBass, n_steps=1), librosa.effects.pitch_shift(yFs3, srBass, n_steps=2), yA3, librosa.effects.pitch_shift(yA3, srBass, n_steps=1), librosa.effects.pitch_shift(yA3, srBass, n_steps=2)]

#COMMENTS on stuff that confuse me
#spb means how long before every beat

#Drums
#each x is 1/16th of a measure
#hat    |xxxx|xxxx|xxxx|xxxx|
#snare  |xxxx|xxxx|xxxx|xxxx|
#kick   |xxxx|xxxx|xxxx|xxxx|

#standard break beat?
# |x x |x x |xxx |x x |
# |    |x   |    |x   |
# |x   |    |  x |    |
def makeStandardBreaks(bpm):
	spb = 60.0 / bpm
	measure = 4.0 * spb
	timeBeat = ((measure / 16.0) * 1000)
	canvas = AudioSegment.silent(measure * 1000 * 2)
	oneBeat = AudioSegment.silent(spb * 1000)
	snare = AudioSegment.from_file("drums/snare.wav")
	kickBig = AudioSegment.from_file("drums/kick-big.wav")
	kickHeavy = AudioSegment.from_file("drums/kick-heavy.wav")
	hihat = AudioSegment.from_file("drums/hihat.wav")
	hihat = hihat
	hatBeat1 = hihat + AudioSegment.silent(2 * timeBeat - (LENHIHAT * 1000)) + hihat + AudioSegment.silent(2 * timeBeat - (LENHIHAT * 1000)) + hihat + AudioSegment.silent(2 * timeBeat - (LENHIHAT * 1000)) + hihat + AudioSegment.silent(2 * timeBeat - (LENHIHAT * 1000)) + hihat + AudioSegment.silent(2 * timeBeat - (LENHIHAT * 1000)) + hihat + AudioSegment.silent(2 *timeBeat - (LENHIHAT * 1000)) + hihat + AudioSegment.silent(2 * timeBeat - (LENHIHAT * 1000)) + hihat + AudioSegment.silent(2 * timeBeat - (LENHIHAT * 1000)) + hihat + AudioSegment.silent(2 * timeBeat - (LENHIHAT * 1000))
	hatBeat2 = hihat + AudioSegment.silent(2 * timeBeat - (LENHIHAT * 1000)) + hihat + AudioSegment.silent(2 * timeBeat - (LENHIHAT * 1000)) + hihat + AudioSegment.silent(2 * timeBeat - (LENHIHAT * 1000)) + hihat + AudioSegment.silent(timeBeat - (LENHIHAT * 1000)) + hihat + AudioSegment.silent(timeBeat - (LENHIHAT * 1000)) + hihat + AudioSegment.silent(2 *timeBeat - (LENHIHAT * 1000)) + hihat + AudioSegment.silent(4 * timeBeat - (LENHIHAT * 1000)) + hihat
	snareKickBeat1 = kickBig + AudioSegment.silent(4 * timeBeat - (LENKICKBIG * 1000)) + snare + AudioSegment.silent(6 * timeBeat - (LENSNARE * 1000)) + kickHeavy + AudioSegment.silent(2 * timeBeat - (LENKICKHEAVY * 1000)) + snare
	oneMeasure = canvas.overlay(hatBeat1).overlay(hatBeat2, position = measure * 1000).overlay(snareKickBeat1).overlay(snareKickBeat1, position = measure * 1000)
	twoMeasures = oneMeasure + oneMeasure
	twoMeasures.export("drumsStandardBreaks.wav", format = "wav")

# 2 and 4 beat
# | x x| x x|
# |xxxx|xxxx|
# |x x |x x |
def make2and4Beat(bpm):
	spb = 60.0 / bpm
	measure = 4.0 * spb
	timeBeat = (measure / 4) * 1000
	canvas = AudioSegment.silent(measure * 1000)
	oneBeat = AudioSegment.silent(spb * 1000)
	snare = AudioSegment.from_file("drums/snare.wav")
	kick = AudioSegment.from_file("drums/kick-big.wav")
	hihat = AudioSegment.from_file("drums/hihat.wav")
	hihat = hihat + 5
	snareBeat = snare + AudioSegment.silent(timeBeat - (LENSNARE * 1000)) + snare + AudioSegment.silent(timeBeat - (LENSNARE * 1000)) + snare + AudioSegment.silent(timeBeat - (LENSNARE * 1000)) + snare
	kickHihatBeat = kick + AudioSegment.silent(timeBeat - (LENKICKBIG * 1000)) + hihat + AudioSegment.silent(timeBeat - (LENHIHAT * 1000)) + kick + AudioSegment.silent(timeBeat - (LENKICKBIG * 1000)) + hihat
	oneMeasure = canvas.overlay(snareBeat).overlay(kickHihatBeat)
	twoMeasures = oneMeasure + oneMeasure
	twoMeasures.export("drums24.wav", format="wav")


# this makes like | 1 4 | 5 |
def makeBasic145(key, bpm):
	#Piano
	spb = 60.0 / bpm
	measure = BEATSPERMEASURE * spb
	scaleIndex = cScale.index(key)
	tempNote = cScaleNotesP[scaleIndex]
	note1_1 = librosa.effects.time_stretch(tempNote, (librosa.get_duration(tempNote, srPiano) / measure) * 2.0)
	tempNote = cScaleNotesP[scaleIndex + 4]
	note1_2 = librosa.effects.time_stretch(tempNote, (librosa.get_duration(tempNote, srPiano) / measure) * 2.0)
	tempNote = cScaleNotesP[scaleIndex + 7]
	note1_3 = librosa.effects.time_stretch(tempNote, (librosa.get_duration(tempNote, srPiano) / measure) * 2.0)
	librosa.output.write_wav("noteP1_1.wav", note1_1, srPiano)
	librosa.output.write_wav("noteP1_2.wav", note1_2, srPiano)
	librosa.output.write_wav("noteP1_3.wav", note1_3, srPiano)
	audioSegment1_1 = AudioSegment.from_file("noteP1_1.wav")
	audioSegment1_2 = AudioSegment.from_file("noteP1_2.wav")
	audioSegment1_3 = AudioSegment.from_file("noteP1_3.wav")
	audioSegment1 = audioSegment1_1.overlay(audioSegment1_2).overlay(audioSegment1_3)

	tempNote = cScaleNotesP[scaleIndex + 5]
	note4_1 = librosa.effects.time_stretch(tempNote, (librosa.get_duration(tempNote, srPiano) / measure) * 2.0)
	tempNote = cScaleNotesP[scaleIndex + 9]
	note4_2 = librosa.effects.time_stretch(tempNote, (librosa.get_duration(tempNote, srPiano) / measure) * 2.0)
	tempNote = cScaleNotesP[scaleIndex + 12]
	note4_3 = librosa.effects.time_stretch(tempNote, (librosa.get_duration(tempNote, srPiano) / measure) * 2.0)
	librosa.output.write_wav("noteP4_1.wav", note4_1, srPiano)
	librosa.output.write_wav("noteP4_2.wav", note4_2, srPiano)
	librosa.output.write_wav("noteP4_3.wav", note4_3, srPiano)
	audioSegment4_1 = AudioSegment.from_file("noteP4_1.wav")
	audioSegment4_2 = AudioSegment.from_file("noteP4_2.wav")
	audioSegment4_3 = AudioSegment.from_file("noteP4_3.wav")
	audioSegment4 = audioSegment4_1.overlay(audioSegment4_2).overlay(audioSegment4_3)

	tempNote = cScaleNotesP[scaleIndex + 7]
	note5_1 = librosa.effects.time_stretch(tempNote, (librosa.get_duration(tempNote, srPiano) / measure))
	tempNote = cScaleNotesP[scaleIndex + 11]
	note5_2 = librosa.effects.time_stretch(tempNote, (librosa.get_duration(tempNote, srPiano) / measure))
	tempNote = cScaleNotesP[scaleIndex + 14]
	note5_3 = librosa.effects.time_stretch(tempNote, (librosa.get_duration(tempNote, srPiano) / measure))
	librosa.output.write_wav("noteP5_1.wav", note5_1, srPiano)
	librosa.output.write_wav("noteP5_2.wav", note5_2, srPiano)
	librosa.output.write_wav("noteP5_3.wav", note5_3, srPiano)
	audioSegment5_1 = AudioSegment.from_file("noteP5_1.wav")
	audioSegment5_2 = AudioSegment.from_file("noteP5_2.wav")
	audioSegment5_3 = AudioSegment.from_file("noteP5_3.wav")
	audioSegment5 = audioSegment5_1.overlay(audioSegment5_2).overlay(audioSegment5_3)

	audio145 = audioSegment1 + audioSegment4 + audioSegment5
	audio145.export("piano145.wav", format="wav")

	#Bass
	tempNote = cScaleNotesB[scaleIndex]
	note1_1 = librosa.effects.time_stretch(tempNote, (librosa.get_duration(tempNote, srBass) / measure) * 2.0)
	tempNote = cScaleNotesB[scaleIndex + 5]
	note4_1 = librosa.effects.time_stretch(tempNote, (librosa.get_duration(tempNote, srBass) / measure) * 2.0)
	tempNote = cScaleNotesB[scaleIndex + 7]
	note5_1 = librosa.effects.time_stretch(tempNote, (librosa.get_duration(tempNote, srBass) / measure))
	librosa.output.write_wav("noteB1_1.wav", note1_1, srBass)
	librosa.output.write_wav("noteB4_1.wav", note4_1, srBass)
	librosa.output.write_wav("noteB5_1.wav", note5_1, srBass)

	audioSegment1_1 = AudioSegment.from_file("noteB1_1.wav")
	audioSegment4_1 = AudioSegment.from_file("noteB4_1.wav")
	audioSegment5_1 = AudioSegment.from_file("noteB5_1.wav")

	audio145 = (audioSegment1_1 + 10) + (audioSegment4_1 + 10) + (audioSegment5_1 + 10)
	audio145.export("bass145.wav", format="wav")

def make1456(key, bpm):
	#Piano
	spb = 60.0 / bpm
	measure = BEATSPERMEASURE * spb
	scaleIndex = cScale.index(key)
	tempNote = cScaleNotesP[scaleIndex + 7]
	note1_1 = librosa.effects.time_stretch(tempNote, (librosa.get_duration(tempNote, srPiano) / measure) * 2.0)
	tempNote = cScaleNotesP[scaleIndex + 12]
	note1_2 = librosa.effects.time_stretch(tempNote, (librosa.get_duration(tempNote, srPiano) / measure) * 2.0)
	tempNote = cScaleNotesP[scaleIndex + 16]
	note1_3 = librosa.effects.time_stretch(tempNote, (librosa.get_duration(tempNote, srPiano) / measure) * 2.0)
	librosa.output.write_wav("2noteP1_1.wav", note1_1, srPiano)
	librosa.output.write_wav("2noteP1_2.wav", note1_2, srPiano)
	librosa.output.write_wav("2noteP1_3.wav", note1_3, srPiano)
	audioSegment1_1 = AudioSegment.from_file("2noteP1_1.wav")
	audioSegment1_2 = AudioSegment.from_file("2noteP1_2.wav")
	audioSegment1_3 = AudioSegment.from_file("2noteP1_3.wav")
	audioSegment1 = audioSegment1_1.overlay(audioSegment1_2).overlay(audioSegment1_3)

	tempNote = cScaleNotesP[scaleIndex + 7]
	note4_1 = librosa.effects.time_stretch(tempNote, (librosa.get_duration(tempNote, srPiano) / measure) * 2.0)
	tempNote = cScaleNotesP[scaleIndex + 11]
	note4_2 = librosa.effects.time_stretch(tempNote, (librosa.get_duration(tempNote, srPiano) / measure) * 2.0)
	tempNote = cScaleNotesP[scaleIndex + 14]
	note4_3 = librosa.effects.time_stretch(tempNote, (librosa.get_duration(tempNote, srPiano) / measure) * 2.0)
	librosa.output.write_wav("2noteP4_1.wav", note4_1, srPiano)
	librosa.output.write_wav("2noteP4_2.wav", note4_2, srPiano)
	librosa.output.write_wav("2noteP4_3.wav", note4_3, srPiano)
	audioSegment4_1 = AudioSegment.from_file("2noteP4_1.wav")
	audioSegment4_2 = AudioSegment.from_file("2noteP4_2.wav")
	audioSegment4_3 = AudioSegment.from_file("2noteP4_3.wav")
	audioSegment4 = audioSegment4_1.overlay(audioSegment4_2).overlay(audioSegment4_3)

	tempNote = cScaleNotesP[scaleIndex + 9]
	note5_1 = librosa.effects.time_stretch(tempNote, (librosa.get_duration(tempNote, srPiano) / measure) * 2.0)
	tempNote = cScaleNotesP[scaleIndex + 12]
	note5_2 = librosa.effects.time_stretch(tempNote, (librosa.get_duration(tempNote, srPiano) / measure) * 2.0)
	tempNote = cScaleNotesP[scaleIndex + 16]
	note5_3 = librosa.effects.time_stretch(tempNote, (librosa.get_duration(tempNote, srPiano) / measure) * 2.0)
	librosa.output.write_wav("2noteP5_1.wav", note5_1, srPiano)
	librosa.output.write_wav("2noteP5_2.wav", note5_2, srPiano)
	librosa.output.write_wav("2noteP5_3.wav", note5_3, srPiano)
	audioSegment5_1 = AudioSegment.from_file("2noteP5_1.wav")
	audioSegment5_2 = AudioSegment.from_file("2noteP5_2.wav")
	audioSegment5_3 = AudioSegment.from_file("2noteP5_3.wav")
	audioSegment5 = audioSegment5_1.overlay(audioSegment5_2).overlay(audioSegment5_3)

	tempNote = cScaleNotesP[scaleIndex + 9]
	note6_1 = librosa.effects.time_stretch(tempNote, (librosa.get_duration(tempNote, srPiano) / measure) * 2.0)
	tempNote = cScaleNotesP[scaleIndex + 12]
	note6_2 = librosa.effects.time_stretch(tempNote, (librosa.get_duration(tempNote, srPiano) / measure) * 2.0)
	tempNote = cScaleNotesP[scaleIndex + 17]
	note6_3 = librosa.effects.time_stretch(tempNote, (librosa.get_duration(tempNote, srPiano) / measure) * 2.0)
	librosa.output.write_wav("2noteP6_1.wav", note6_1, srPiano)
	librosa.output.write_wav("2noteP6_2.wav", note6_2, srPiano)
	librosa.output.write_wav("2noteP6_3.wav", note6_3, srPiano)
	audioSegment6_1 = AudioSegment.from_file("2noteP6_1.wav")
	audioSegment6_2 = AudioSegment.from_file("2noteP6_2.wav")
	audioSegment6_3 = AudioSegment.from_file("2noteP6_3.wav")
	audioSegment6 = audioSegment6_1.overlay(audioSegment6_2).overlay(audioSegment6_3)

	audio145 = audioSegment1 + audioSegment4 + audioSegment5 + audioSegment6
	audio145.export("piano1456.wav", format="wav")

	#Bass
	tempNote = cScaleNotesB[scaleIndex + 12]
	note1_1 = librosa.effects.time_stretch(tempNote, (librosa.get_duration(tempNote, srBass) / measure) * 2.0)
	tempNote = cScaleNotesB[scaleIndex + 11]
	note4_1 = librosa.effects.time_stretch(tempNote, (librosa.get_duration(tempNote, srBass) / measure) * 2.0)
	tempNote = cScaleNotesB[scaleIndex + 9]
	note5_1 = librosa.effects.time_stretch(tempNote, (librosa.get_duration(tempNote, srBass) / measure) * 2.0)
	tempNote = cScaleNotesB[scaleIndex + 5]
	note6_1 = librosa.effects.time_stretch(tempNote, (librosa.get_duration(tempNote, srBass) / measure) * 2.0)
	librosa.output.write_wav("2noteB1_1.wav", note1_1, srBass)
	librosa.output.write_wav("2noteB4_1.wav", note4_1, srBass)
	librosa.output.write_wav("2noteB5_1.wav", note5_1, srBass)
	librosa.output.write_wav("2noteB6_1.wav", note5_1, srBass)

	audioSegment1_1 = AudioSegment.from_file("2noteB1_1.wav")
	audioSegment4_1 = AudioSegment.from_file("2noteB4_1.wav")
	audioSegment5_1 = AudioSegment.from_file("2noteB5_1.wav")
	audioSegment6_1 = AudioSegment.from_file("2noteB6_1.wav")

	audio145 = (audioSegment1_1 + 10) + (audioSegment4_1 + 10) + (audioSegment5_1 + 10) + (audioSegment6_1 + 10)
	audio145.export("bass1456.wav", format="wav")


#puts together drums, piano (all two measures)
def putTogether():
	drumsT = AudioSegment.from_file("drums24.wav")
	pianoT = AudioSegment.from_file("piano145.wav")
	piano2T = AudioSegment.from_file("piano1456.wav")
	bassT = AudioSegment.from_file("bass145.wav")
	bass2T = AudioSegment.from_file("bass1456.wav")
	drums = drumsT + drumsT
	piano = pianoT + piano2T
	bass = bassT + bass2T
	together = drums.overlay(piano).overlay(bass)
	#play(together)
	together1 = together + together + together + together
	together1.export("instrumental.wav", format="wav")
	asdf = AudioSegment.from_file("instrumental.wav") 
	voice = AudioSegment.from_file("test.wav")
	together2 = asdf.overlay(voice)
	together2.export("voice.wav", format="wav")

for line in sys.stdin:
	mLine = line
makeBasic145(mLine.split()[0], float(float(mLine.split()[1])/4.0))
make1456(mLine.split()[0], float(float(mLine.split()[1])/4.0))
#makeStandardBreaks(argv[2])
make2and4Beat(float(mLine.split()[1]))
putTogether()
