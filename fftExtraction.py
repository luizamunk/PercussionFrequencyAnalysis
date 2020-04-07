import numpy as np
import math
numberOfSamples = 44100

def mag2db(mag):
    return np.array(map(lambda x : 20*math.log10(x),mag))


def fftExtraction(rawAudioSignal, signalPeriod):
    numberOfZeros = abs(numberOfSamples - len(rawAudioSignal))

    # Normalizing audioyo size
    if len(rawAudioSignal) < numberOfSamples:
        rawAudioSignal = np.append(rawAudioSignal,np.zeros(numberOfZeros))
    else:
        rawAudioSignal = rawAudioSignal[:numberOfSamples]
        
    fftAmplitudes = abs(np.fft.fft(rawAudioSignal))
    frequencies = np.fft.fftfreq(len(rawAudioSignal), d=signalPeriod)

    # Normalize amplitudes
    maxValue = np.amax(fftAmplitudes)
    fftAmplitudes = fftAmplitudes/maxValue



    return fftAmplitudes, frequencies