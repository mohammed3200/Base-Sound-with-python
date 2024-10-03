# from plot_audio import plotAudio  # Import the plot_audio function
# from wave_example import Info_wave  # Import the Info_wave function
# from record_mic import record_mic  # Import the plot_audio function
# from load_mp3 import load_mp3  # Import the plot_audio function
from Record import RecordSound  # Import the plot_audio function

def main():
  print("loading...!")
  RecordSound()
  # Info_wave()
  # plotAudio()  # Call the plot_audio function
  # record_mic()  # Call the record_mic function
  # load_mp3()  # Call the load_mp3 function
  print("done...!")  

if __name__ == "__main__":
  main()