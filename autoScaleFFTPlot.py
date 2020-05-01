import numpy as np

# Only the positive values of the fft
arrayLength = 22050

def autoScaleFFTPlot(fftAmplitudes, fftFrequencies):
    # Cutting the arrays to match only positives values
    fftAmplitudeValues = fftAmplitudes[fftFrequencies >= 0]
    numberOfZeros = abs(arrayLength - len(fftAmplitudeValues))

    frequenciesValues = fftFrequencies[fftFrequencies >= 0]

    return frequenciesValues, fftAmplitudeValues