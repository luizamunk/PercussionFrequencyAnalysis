import matplotlib.pyplot as plt
import numpy as np
import scipy as scp
import wave
import sys
from scipy.io import wavfile
from scipy.fftpack import fft


# Open file
snareDrumTuned = wave.open('./Records/SnareDrum196HzMono.wav', "r")

# Extract Raw Audio from Wav File
signalSnareDrumTuned = snareDrumTuned.readframes(-1)
signalSnareDrumTuned = np.frombuffer(signalSnareDrumTuned, dtype='int16')
frequenciaAmostragem = snareDrumTuned.getframerate()
numberOfSamples = len(signalSnareDrumTuned)
print(numberOfSamples)
T = 1.0/frequenciaAmostragem

# Checking if is Mono or Stereo. Should we work with stereo?
if snareDrumTuned.getnchannels() == 2:
    print("Just Mono files!")
    sys.exit(0)

# Creating time vector to see x axis in seconds
timeSeconds = np.linspace(0, len(signalSnareDrumTuned)/frequenciaAmostragem, num=len(signalSnareDrumTuned))

plt.figure(num=1)
plt.title('Snare Drum Untuned')
plt.plot(timeSeconds,signalSnareDrumTuned)
plt.xlabel('Time (s)')
plt.ylabel('Sound Amplitude')
plt.grid(True)
plt.draw()

# Trying to plot the fft
fftVal = abs(np.fft.fft(signalSnareDrumTuned))
frequencies = np.fft.fftfreq(len(signalSnareDrumTuned), d=T)

# Arranges the frequencies in ascending order
# idx = np.argsort(freqs)

plt.figure(num=2)
plt.title('Fast Fourier Transform of Snare Drum Untuned')
plt.plot(frequencies,fftVal)
plt.grid(True)
plt.show()

