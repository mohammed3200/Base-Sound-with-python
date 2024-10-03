import wave
import matplotlib.pyplot as plt
import numpy as np

obj = wave.open("sound/ocean-waves-112906.wav", "rb")

sample_freq = obj.getframerate()
n_samples = obj.getnframes()
signal_wave = obj.readframes(-1)

obj.close()

t_audio = n_samples / sample_freq

signal_array = np.frombuffer(signal_wave, dtype=np.int32)

times = np.linspace(0, t_audio, num=n_samples)


def plotAudio():
  plt.figure(figsize=(15, 5))
  plt.plot(times, signal_array)
  plt.title("Audio Signal")
  plt.ylabel("Signal wave")
  plt.xlabel("Time (s)")
  plt.xlim(0, t_audio)
  plt.show()