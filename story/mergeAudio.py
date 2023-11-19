from pydub import AudioSegment
import wave

infiles = ["audioFile1.wav","audioFile2.wav""audioFile3.wav","audioFile4.wav","audioFile5.wav","audioFile6.wav","audioFile7.wav","audioFile8.wav","audioFile9.wav","audioFile10.wav","audioFile11.wav"]
outfile = "combinedAunds.wav"

data = []
for infile in infiles:
    w = wave.open(infile, 'rb')
    data.append( [w.getparams(), w.readframes(w.getnframes())] )
    w.close()
    
output = wave.open(outfile, 'wb')
output.setparams(data[0][0])
for i in range(len(data)):
    output.writeframes(data[i][1])
output.close()
'''
audioFiles=["audioFile1.wav","audioFile2.wav""audioFile3.wav","audioFile4.wav","audioFile5.wav","audioFile6.wav","audioFile7.wav","audioFile8.wav","audioFile9.wav","audioFile10.wav","audioFile11.wav"]

def mergeAudio(audioFiles):
    combinedAudio
    for ii in range(len(audioFiles)):
        sound = AudioSegment.from_wav(f"audioFile{ii}.wav")
        combinedAudio += sound
    
    combinedAudio.export("\Users\Jilin\Desktop\BostonHacks\story\combinedAudio.wav", format="wav")
    '''