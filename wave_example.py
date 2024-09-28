# Audio file formats
# -------------------
# .mp3
# .wav
# .ogg
# .flac
# .aac
# .m4a

# importing os module 
import os 
import wave

# Audio signal parameters
# -------------------
# - number of channels
# - sample width in bytes
# - frame rate (frames per second)
# - framerate/sample-rate: 44,100 Hz
# - number of frames
# - values of a frame
def Info_wave():
  obj = wave.open("sound/ocean-waves-112906.wav","rb")
  
  print("Number of channels",obj.getnchannels())
  print("sample width ", obj.getsampwidth())
  print("frame rate ", obj.getframerate())
  print("number of frames ", obj.getnframes())
  print("parameters ", obj.getparams())
  
  t_audio = obj.getnframes() / obj.getframerate()
  
  print("Time of audio ", t_audio)
  
  frames = obj.readframes(-1)
  print(type(frames),type(frames[0]))
  print(len(frames))
  obj.close()
  
  
  # Create the folder in the current directory
  os.makedirs("sound-output", exist_ok=True)
  
  obj_new = wave.open("sound-output/ocean-waves-112906_new.wav","wb")
  
  obj_new.setnchannels(1)
  obj_new.setsampwidth(2)
  obj_new.setframerate(44100.0)
  
  obj_new.writeframes(frames)
  
  obj_new.close()