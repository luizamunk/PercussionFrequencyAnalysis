import matplotlib.pyplot as plt
import numpy as np
import scipy as scp
import wave
import sys
import os
from scipy.io import wavfile
from scipy.fftpack import fft

# Open file
snareDrumUntuned = wave.open('./Records/SnareDrumUntunedMono.wav', "r")

# Extract Raw Audio from Wav File
signalSnareDrumUntuned = snareDrumUntuned.readframes(-1)
signalSnareDrumUntuned = np.frombuffer(signalSnareDrumUntuned, dtype='int16')
frequenciaAmostragem = snareDrumUntuned.getframerate()
numberOfSamples = len(signalSnareDrumUntuned)
print(numberOfSamples)
T = 1.0/frequenciaAmostragem

# Checking if is Mono or Stereo. Should we work with stereo?
if snareDrumUntuned.getnchannels() == 2:
    print("Just Mono files!")
    sys.exit(0)

# Creating time vector to see x axis in seconds
timeSeconds = np.linspace(0, len(signalSnareDrumUntuned)/frequenciaAmostragem, num=len(signalSnareDrumUntuned))

timeResponse = plt.figure(num=1)
plt.title('Resposta temporal para a caixa desafinada')
plt.plot(timeSeconds,signalSnareDrumUntuned)
plt.xlabel('Time (s)')
plt.ylabel('Sound Amplitude')
plt.grid(True)
plt.draw()

# Create the file Graphs if it doesn't exists
if not os.path.exists('Graphs'):
    os.makedirs('Graphs')
    
timeResponse.savefig("Graphs/TimeResponseSnareUntuned.pdf", bbox_inches='tight')

# Trying to plot the fft
fftVal = abs(np.fft.fft(signalSnareDrumUntuned))/len(signalSnareDrumUntuned)
frequencies = np.fft.fftfreq(len(signalSnareDrumUntuned), d=T)

# Cutting the arrays to match only positives values
fftPositiveValues = fftVal[frequencies > 0]
frequenciesPositives = frequencies[frequencies > 0]

# Creating a mask for scale the plot
maskScale = (frequenciesPositives >= 0) & (frequenciesPositives <= 3000)

frequencyResponse = plt.figure(num=2)
plt.title('Resposta em frequência da caixa desafinada')
plt.plot(frequenciesPositives[maskScale],fftPositiveValues[maskScale])
plt.xlabel('Frequency (Hz)')
plt.ylabel('Amplitude')
plt.grid(True)
plt.show()
frequencyResponse.savefig("Graphs/FrequencyResponseSnareUntuned.pdf", bbox_inches='tight')

