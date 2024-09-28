import pyaudio
import wave

FRAMS_PER_BUFFER = 3200
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100

def record_mic():
  p = pyaudio.PyAudio()

  stream = p.open(format=FORMAT,
                  channels=CHANNELS,
                  rate=RATE,
                  input=True,
                  frames_per_buffer=FRAMS_PER_BUFFER)


  print("Start recoding")

  frames = []
  seconds = 5

  for i in range(0, int(RATE / FRAMS_PER_BUFFER * seconds)):
    data = stream.read(FRAMS_PER_BUFFER)
    frames.append(data)

  stream.stop_stream()
  stream.close()
  p.terminate()

  obj = wave.open("sound/ocean-waves-112906.wav", "wb")
  obj.setnchannels(CHANNELS)
  obj.setsampwidth(p.get_sample_size(FORMAT))
  obj.setframerate(RATE)
  obj.writeframes(b''.join(frames))
  obj.close()