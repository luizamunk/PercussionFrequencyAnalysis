import numpy as np

# Only the positive values of the fft
arrayLength = 22050

def autoScaleFFTPlot(fftAmplitudes, fftFrequencies):
    # Cutting the arrays to match only positives values
    fftAmplitudeValues = fftAmplitudes[fftFrequencies >= 0]
    numberOfZeros = abs(arrayLength - len(fftAmplitudeValues))

    # if len(fftAmplitudeValues) < arrayLength:
    #     fftAmplitudeValues = np.append(fftAmplitudeValues,np.zeros(numberOfZeros))
    # else:
    #     fftAmplitudeValues = fftAmplitudeValues[:arrayLength]

    frequenciesValues = fftFrequencies[fftFrequencies >= 0]

    # if len(frequenciesValues) < arrayLength:
    #     frequenciesValues = np.append(frequenciesValues,np.zeros(numberOfZeros))
    # else:
    #     frequenciesValues = frequenciesValues[:arrayLength]

    # Creating a mask for scale the plot
    return frequenciesValues, fftAmplitudeValues