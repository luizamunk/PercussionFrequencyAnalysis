import numpy as np
numberOfSamples = 44100

def TimeResponseAudio(rawAudioSignal, signalPeriod):
    timeSeconds = np.linspace(0, numberOfSamples/(1/signalPeriod), num=numberOfSamples)
    numberOfZeros = abs(numberOfSamples - len(rawAudioSignal))

    # Normalizing audio size
    if len(rawAudioSignal) < numberOfSamples:
        rawAudioSignal = np.append(rawAudioSignal,np.zeros(numberOfZeros))
    else:
        rawAudioSignal = rawAudioSignal[:numberOfSamples]


    return rawAudioSignal, timeSeconds