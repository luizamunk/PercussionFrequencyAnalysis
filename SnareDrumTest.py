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
from autoScaleFFTPlot import autoScaleFFTPlot
from TimeResponseAudio import TimeResponseAudio

# Create the file Graphs if it doesn't exists
if not os.path.exists('Graphs'):
    os.makedirs('Graphs')

#
# SECTION: Open each file
#
# Open file Tuned with Strainer
snareDrumTunedStrainer = wave.open('/home/luizmunk/Documents/TCC/Codes/Records/SnareDrumTunedHighAttack.wav', "r")
# Open file Tuned
snareDrumTuned = wave.open('/home/luizmunk/Documents/TCC/Codes/Records/SnareDrum196HzMono.wav', "r")
# Open file Tuned low attack
# snareDrumTuned = wave.open('/home/luizmunk/Documents/TCC/Codes/Records/SnareDrumTunedLowAtack.wav', "r")
# Open file Tuned low attack
# snareDrumTuned = wave.open('/home/luizmunk/Documents/TCC/Codes/Records/SnareDrumTunedHighAttack.wav', "r")


#
# SECTION:
#
# Extract Raw Audio from tuned snare drum
signalSnareDrumTuned = snareDrumTuned.readframes(-1)
signalSnareDrumTuned = np.frombuffer(signalSnareDrumTuned, dtype='int16')
fsTuned = snareDrumTuned.getframerate()
numberOfSamples = len(signalSnareDrumTuned)
TTuned = 1.0/fsTuned
# Extract Raw Audio tuned snare drum with strainer
signalSnareDrumTunedStrainer = snareDrumTunedStrainer.readframes(-1)
signalSnareDrumTunedStrainer = np.frombuffer(signalSnareDrumTunedStrainer, dtype='int16')
fsStrainer = snareDrumTunedStrainer.getframerate()
TStrainer = 1.0/fsStrainer
# Extract raw audio from tuned snare drum with low attack
# signalSnareDrumTunedLowAttack = snareDrumTuned.readframes(-1)
# signalSnareDrumTunedLowAttack = np.frombuffer(signalSnareDrumTunedLowAttack, dtype='int16')
# fs = snareDrumTuned.getframerate()
# numberOfSamples = len(signalSnareDrumTunedLowAttack)
# T = 1.0/fs

#
# SECTION: Check Mono File
#
# Calling function in other file to check if it's mono file
checkMonoFile(rawAudioFile=snareDrumTunedStrainer)
checkMonoFile(rawAudioFile=snareDrumTuned)

signalSnareDrumTuned, timeAxis = TimeResponseAudio(signalSnareDrumTuned, TTuned)


# Function to plot the audio signal in time 
def PlotTimeAudioSignal(audioSignal, timeAxis):
    timeResponse = plt.figure(num=1)
    plt.title('Sinal de áudio da caixa afinada')
    plt.plot(timeAxis,audioSignal)
    plt.xlabel('Tempo (s)')
    plt.ylabel('Amplitude')
    plt.grid(True)
    plt.draw()
    timeResponse.savefig("/home/luizmunk/Documents/TCC/Codes/Graphs/TimeResponseSnareTuned.pdf", bbox_inches='tight')

PlotTimeAudioSignal(audioSignal=signalSnareDrumTuned, timeAxis=timeAxis)

# Extract fast fourier transform from files
    # Just Tuned
fftAmplitudesTuned, frequenciesTuned = fftExtraction(rawAudioSignal=signalSnareDrumTuned, signalPeriod=TTuned)
    # With Strainer
fftAmplitudesTunedStrainer, frequenciesTunedStrainer = fftExtraction(rawAudioSignal=signalSnareDrumTunedStrainer, signalPeriod=TStrainer)

frequenciesTuned, fftAmplitudesTuned = autoScaleFFTPlot(fftAmplitudes=fftAmplitudesTuned, fftFrequencies=frequenciesTuned)
frequenciesTunedStrainer, fftAmplitudesTunedStrainer = autoScaleFFTPlot(fftAmplitudes=fftAmplitudesTunedStrainer, fftFrequencies=frequenciesTunedStrainer)

maskScale = (frequenciesTunedStrainer >= 0) & (frequenciesTunedStrainer <= 1000)

# Ploting fft
frequencyResponse = plt.figure(num=2)
strainer = plt.plot(frequenciesTunedStrainer[maskScale], fftAmplitudesTunedStrainer[maskScale], 'r', label='Caixa afinada com ataque forte')

tuned = plt.plot(frequenciesTuned[maskScale],fftAmplitudesTuned[maskScale], 'b--', label='Caixa afinada com ataque normal')
plt.title('Espectro de frequência da caixa',fontsize=14)
plt.xlabel('Frequência (Hz)',fontsize=14)
plt.yticks(fontsize=14) 
plt.ylabel('Amplitude',fontsize=14)
plt.xticks(fontsize=14) 
plt.grid(True)
plt.legend(loc="upper right", prop={"size":18})
plt.show()
frequencyResponse.savefig("/home/luizmunk/Documents/TCC/Codes/Graphs/FrequencyResponseSnareTunedStrainer.pdf", bbox_inches='tight')
