from pydub import AudioSegment
from pydub.playback import play
import librosa

audioc = AudioSegment.from_file("piano/wav/c1.wav")
audiod = AudioSegment.from_file("piano/wav/d1.wav")
audioe = AudioSegment.from_file("piano/wav/e1.wav")
audiof = AudioSegment.from_file("piano/wav/f1.wav")
audiog = AudioSegment.from_file("piano/wav/g1.wav")
audioa = AudioSegment.from_file("piano/wav/a1.wav")
audiob = AudioSegment.from_file("piano/wav/b1.wav")

y, sr = librosa.load("piano/wav/c1.wav")
y_stretch = librosa.effects.time_stretch(y, 0.5)
y_pitch = librosa.effects.pitch_shift(y_stretch, sr, n_steps = 12)
librosa.output.write_wav("test.wav", y_stretch, sr)
librosa.output.write_wav("test2.wav", y_pitch, sr)

test = AudioSegment.from_file("test.wav")
test2 = AudioSegment.from_file("test2.wav")
mixed = audioc.overlay(audioe).overlay(audiog)
mixed2 = audiof.overlay(audioa).overlay(audioc)
mixed3 = audiog.overlay(audiob).overlay(audiod)
repeatedc = audioc[175:180] * 100
repeatedd = audiod[150:155] * 100
repeatede = audioe[150:155] * 100
repeatedf = audiof[150:155] * 100
repeatedg = audiog[150:155] * 100
repeateda = audioa[150:155] * 100
repeatedb = audiob[150:155] * 100
sample = mixed + mixed2 + mixed3
#sample = repeatedc + repeatedd + repeatede + repeatedf + repeatedg + repeateda + repeatedb
#sample = repeatedc + audioc
#sample = test + test2
play(sample)
