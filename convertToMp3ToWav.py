from pydub import AudioSegment

mp3_filename = 'input/mp3/city-of-stars.mp3'
wav_filename = 'input/wav/city-of-stars.wav'

AudioSegment.from_file(mp3_filename).export(wav_filename, format='wav')