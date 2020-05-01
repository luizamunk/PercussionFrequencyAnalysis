import matplotlib.pyplot as plt
import matplotlib.axes as ax
import numpy as np
import scipy as scp
import wave
import sys
import os
from scipy.io import wavfile
from scipy.fftpack import fft

# Built methods
from checkMonoFile import checkMonoFile
from fftExtraction import fftExtraction
from TimeResponseAudio import TimeResponseAudio

#
# SECTION: Open each file
#
# Open files of Tuned snare drum
snareDrumFile = [None] * 10
for i in range(10):
    snareDrumFile[i] = wave.open('/home/luizmunk/Documents/TCC/Codes/Records/CaixaAfinadaEsteira10toques/CaixaAfinadaEsteira'+str(i)+'.wav', "r")

#
# SECTION:
#
# Extract Raw Audio from tuned snare drum
rawSnareDrum = [None] * 10
for i in range(10):
    rawSnareDrum[i] = snareDrumFile[i].readframes(-1)
    rawSnareDrum[i] = np.frombuffer(rawSnareDrum[i], dtype='int16')

#
# SECTION:
#
# Calculate the fast fourier transformer of all files
fftAmplitudes = [None] * 10
fftAmplitudes = [None] * 10
fftFrequencies = [None] * 10
audioFrequency = 44100
for i in range(10):
    fftAmplitudes[i], fftFrequencies[i] = fftExtraction(rawAudioSignal=rawSnareDrum[i], signalPeriod=1/audioFrequency)
    fftAmplitudes[i] = fftAmplitudes[i][fftFrequencies[i] >= 0]
    fftFrequencies[i] = fftFrequencies[i][fftFrequencies[i] >= 0]

maxFrequencyFromFiles = [None] * 10
maxAmplitude = [None] * 10
for i in range(10):
    # maxAmplitude[i] = np.amax(fftAmplitudes[i])
    maxFrequencyFromFiles[i] = fftFrequencies[i][fftAmplitudes[i] == np.amax(fftAmplitudes[i])]

maxAmplitudeValue = np.nanmean(maxFrequencyFromFiles)
print(maxAmplitudeValue)