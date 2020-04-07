import sys

def checkMonoFile(rawAudioFile):
    if rawAudioFile.getnchannels() == 2:
        print("Just Mono files!")
        sys.exit(0)