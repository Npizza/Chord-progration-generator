from pydub import AudioSegment

class TimeSig:
	def __init__(self,U,D):
		self.u = U
		self.d = D

class Settings:
	def __init__(self,trackname,bpm,trackbars,U,D):
		#import the name of the start track
		self.trackname = trackname
		#import the wav file
		self.track = AudioSegment.from_wav(trackname)
		#set the bpm
		self.bpm = bpm
		#set the total bars
		self.totaltrackbars = trackbars
		#set the time signature
		self.timesig = TimeSig(U,D)
		#calculate the T parametre
		self.t = 60*4/self.bpm
		#calculate the duration of one bar
		self.bar_duration = self.timesig.u * self.t/self.timesig.d

	def print_bpm(self):
		print('Bpm = ',self.bpm)
	def print_trackname(self):
		print('The track name is ',self.trackname )
	def print_totalbartrack(self):
		print('The track beats are',self.track_beats)
	def print_timesig(self):
		print('Time signature ',self.timesig.u,'/',self.timesig.d)
	def print_barduration(self):
		print('Bar duration ', self.bar_duration)


class Chord:
	def __init__(self,note,classification,chord):
		self.note = note
		self.cl = classification
		self.chord = chord
		self.filename = self.note +self.cl + '.wav'
	def print_characteristic(self):
		print('Chord:',self.note,self.cl)


#start the main


track = Settings('startTrack.wav',60,5,4,4)
print(track.track.duration_seconds)

notelist=['C','C#','D','D#','E','F','F#','G','G#','A','A#','B']
classchord = ['major']
chordlist = []

#duration of a bar in milli second

bar_duration_in_millisec = track.bar_duration * 1000
print('bar_duration_in_millisec', bar_duration_in_millisec)
rest_track_duration = track.track.duration_seconds * 1000
chord_track = track.track
for cl in classchord:
	for note in notelist:
		print(note,cl)
		#create the chord
		#cut the chord from the wwhole track
		#rest_mili = 
		rest_track_duration = rest_track_duration - bar_duration_in_millisec
		print('rest_track_duration = ',rest_track_duration)
		chord_clip = chord_track[:bar_duration_in_millisec]
		chord_track = chord_track[-rest_track_duration:]
		#create the chord class
		chord = Chord(note,cl,chord_clip)
		#push the chord to the list
		chordlist.append(chord)


for chord in chordlist:
	print(chord.note,chord.cl,chord.filename)
	#extract the chord
	chord.chord.export(chord.filename, format="wav")




track.print_bpm()
track.print_timesig()
track.print_trackname()
track.print_barduration()











# Am7 = AudioSegment.from_wav("Am7.wav")
# Dm7 = AudioSegment.from_wav("Dm7.wav")
# combined = Am7 + Dm7

# repeated = combined * 3
# file_handle = repeated.export("/home/pizza/Desktop/music_gen/output.wav", format="wav")
