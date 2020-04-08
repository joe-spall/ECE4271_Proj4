import librosa
import IPython.display as ipd

audio_path = '5E63D3FF.WAV'
x , sr = librosa.load(audio_path,sr=48000)
print(type(x), type(sr))
ipd.Audio(audio_path)