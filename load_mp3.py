from pydub import AudioSegment

def load_mp3():
  audio = AudioSegment.from_wav("sound/ocean-waves-112906.wav")
  
  # increases the volume by 10 dB
  
  audio = audio + 10
  
  audio = audio * 2
  
  audio = audio.fade_in(2000)
  
  audio.export("sound-output/ocean-waves-112906.mp3", format="mp3")
  
  audio2 = AudioSegment.from_mp3("sound-output/ocean-waves-112906.mp3")
  print("done...!")
