import matplotlib.pyplot as plt
import matplotlib.axes as ax
import numpy as np
import scipy as scp
import wave
import sys
import os
from scipy.io import wavfile
from scipy.fftpack import fft

# Create the file Graphs if it doesn't exists
if not os.path.exists('Graphs'):
    os.makedirs('Graphs')

# Open file
snareDrumTuned = wave.open('/home/luizmunk/Documents/TCC/Codes/Records/SnareDrumTunedLowAtack.wav', "r")

# Extract Raw Audio from Wav File
signalSnareDrumTuned = snareDrumTuned.readframes(-1)
signalSnareDrumTuned = np.frombuffer(signalSnareDrumTuned, dtype='int16')
fs = snareDrumTuned.getframerate()
numberOfSamples = len(signalSnareDrumTuned)
T = 1.0/fs

# Checking if is Mono or Stereo. Should we work with stereo?
if snareDrumTuned.getnchannels() == 2:
    print("Just Mono files!")
    sys.exit(0)

# Creating time vector to see x axis in seconds
timeSeconds = np.linspace(0, len(signalSnareDrumTuned)/fs, num=len(signalSnareDrumTuned))

timeResponse = plt.figure(num=1)
plt.title('Resposta temporal da caixa afinada com ataque fraco')
plt.plot(timeSeconds,signalSnareDrumTuned)
plt.xlabel('Time (s)')
plt.ylabel('Sound Amplitude')
plt.grid(True)
plt.draw()
timeResponse.savefig("/home/luizmunk/Documents/TCC/Codes/Graphs/TimeResponseSnareTunedLowAttack.pdf", bbox_inches='tight')


# Trying to plot the fft
fftVal = abs(np.fft.fft(signalSnareDrumTuned))
frequencies = np.fft.fftfreq(len(signalSnareDrumTuned), d=T)

# Cutting the arrays to match only positives values
fftPositiveValues = fftVal[frequencies > 0]
frequenciesPositives = frequencies[frequencies > 0]

# Creating a mask for scale the plot
maskScale = (frequenciesPositives >= 0) & (frequenciesPositives <= 3000)

# Ploting fft
frequencyResponse = plt.figure(num=2)
plt.plot(frequenciesPositives[maskScale],fftPositiveValues[maskScale])
plt.title('Resposta em frequência da caixa afinada com ataque fraco')
plt.xlabel('Frequência (Hz)')
plt.ylabel('Amplitude')
plt.grid(True)
plt.show()
frequencyResponse.savefig("/home/luizmunk/Documents/TCC/Codes/Graphs/FrequencyResponseSnareTunedLowAttack.pdf", bbox_inches='tight')

