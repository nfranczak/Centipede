# get rid of useless imports
# os remove wav files when done
import pyaudio
import wave
import numpy
import math
from pydub import AudioSegment

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 192000
INPUT_DEVICE_INDEX = 0
RECORD_SECONDS = 5
WAVE_OUTPUT_FILENAME = "output1.wav"

def record():
    p = pyaudio.PyAudio()
    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    input_device_index= INPUT_DEVICE_INDEX,
                    frames_per_buffer=CHUNK)

    print("* recording")

    frames = []

    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)

    print("* done recording")

    stream.stop_stream()
    stream.close()
    p.terminate()

    wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()

    narr = numpy.frombuffer(data, dtype=numpy.int16)
    narr = narr.astype(numpy.int32, copy=False)
    rootMeanSquare = numpy.sqrt(numpy.mean(narr**2))
    if rootMeanSquare > 0:
        decibel = 20 * math.log10(rootMeanSquare)
    else:
        decibel = 0
    return decibel # make sure this is true

def detect_leading_silence(sound, silence_threshold=-55.0, chunk_size=1):
    '''
    sound is a pydub.AudioSegment
    silence_threshold in dB
    chunk_size in ms
    iterate over chunks until you find the first one with sound
    '''
    trim_ms = 0 # ms
    assert chunk_size > 0 # to avoid infinite loop
    while sound[trim_ms:trim_ms+chunk_size].dBFS < silence_threshold and trim_ms < len(sound):
        trim_ms += chunk_size
    return trim_ms

if __name__ == "__main__":
    decibels = record()
    sound = AudioSegment.from_file("/Users/nickfranczak/Desktop/centi/Part II/output1.wav", format="wav")
    start_trim = detect_leading_silence(sound)
    end_trim = detect_leading_silence(sound.reverse())
    duration_1 = len(sound)
    trimmed_sound = sound[start_trim:duration_1-end_trim]
    trimmed_sound.export("/Users/nickfranczak/Desktop/centi/Part II/output2.wav", format="wav")
    duration = len(AudioSegment.from_file("/Users/nickfranczak/Desktop/centi/Part II/output2.wav", format="wav"))/1000
    print('the decibels are: ' + str(decibels) + '\n' + 'duration is: ' + str(duration))
