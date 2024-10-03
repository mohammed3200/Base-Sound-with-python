import pyaudio
import wave
import keyboard
import time
import os 


def RecordSound():

  FORMAT = pyaudio.paInt16
  CHANNLS = 1
  RATE = 44100
  CHUNK = 1024

  # Create the folder in the current directory
  os.makedirs("Records", exist_ok=True)

  # Record the sound
  OUTPUT_FILENAME = "Records/recordedFile.wav"

  audio = pyaudio.PyAudio()
  stream = audio.open(format=FORMAT,
                      channels=CHANNLS,
                      rate=RATE,
                      input=True,
                      frames_per_buffer=CHUNK)

  frames = []
  print("Press SPACE to start recording")
  keyboard.wait('space')
  print("Recording... Press SPACE to stop.")
  time.sleep(0.2)


  while True:
    try:
      data = stream.read(CHUNK)
      frames.append(data)
    except KeyboardInterrupt:
      break
    if keyboard.is_pressed('space'):
      print("Stopping recording after a brief delay...")
      time.sleep(0.2)
      break

  stream.stop_stream()
  stream.close()
  audio.terminate()

  waveFile = wave.open(OUTPUT_FILENAME, 'wb')
  waveFile.setnchannels(CHANNLS)
  waveFile.setsampwidth(audio.get_sample_size(FORMAT))
  waveFile.setframerate(RATE)
  waveFile.writeframes(b''.join(frames))
  waveFile.close()
  print("Finished recording. Saved to", OUTPUT_FILENAME)