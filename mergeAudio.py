import pydub
from pydub import AudioSegment

def mergeAudio(audioFiles):
    dialogue = AudioSegment.from_file("audioFile0.wav")
    combinedDialogue = dialogue
    for ii in range(1,len(audioFiles)):
        dialogue = AudioSegment.from_file(f"audioFile{ii}.wav")
        combinedDialogue += dialogue
