"""
musicinformationretrieval.com/realtime_spectrogram.py

PyAudio example: display a live spectrogram in the terminal.

For more examples using PyAudio:
    https://github.com/mwickert/scikit-dsp-comm/blob/master/sk_dsp_comm/pyaudio_helper.py
"""
import librosa
import numpy
import pyaudio
import time

CHANNELS = 1
RATE = 44100
FRAMES_PER_BUFFER = 1000
N_FFT = 4096
SCREEN_WIDTH = 178

BIN_LO = N_FFT*librosa.note_to_hz('C2')/RATE
BIN_HI = N_FFT*librosa.note_to_hz('C7')/RATE
FREQ_BINS = numpy.geomspace(BIN_LO, BIN_HI, SCREEN_WIDTH).astype('int')

p = pyaudio.PyAudio()

def generate_string_from_audio(audio_data):
    x_fft = numpy.fft.rfft(audio_data, n=N_FFT)
    X = numpy.log10(1 + 0.1*abs(x_fft))

    char_list = [' ']*SCREEN_WIDTH

    for i in range(len(FREQ_BINS)):
        b = FREQ_BINS[i]
        if X[b] > 0.3:
            char_list[i] = '*'
        elif i % 30 == 29:
            char_list[i] = '|'
    return ''.join(char_list)

def callback(in_data, frame_count, time_info, status):
    audio_data = numpy.fromstring(in_data, dtype=numpy.float32)
    print( generate_string_from_audio(audio_data) )
    return (in_data, pyaudio.paContinue)

stream = p.open(format=pyaudio.paFloat32,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                output=True,
                frames_per_buffer=FRAMES_PER_BUFFER,
                stream_callback=callback)

stream.start_stream()

while stream.is_active():
    time.sleep(0.100)

stream.stop_stream()
stream.close()

p.terminate()
