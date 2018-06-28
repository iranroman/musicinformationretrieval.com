"""
PyAudio Example: Make a wire between input and output (i.e., record a
few samples and play them back immediately).

This is the callback (non-blocking) version.
"""
import numpy
import pyaudio
import time

WIDTH = 2
CHANNELS = 1
RATE = 44100

p = pyaudio.PyAudio()

def g(z):
    if z:
        return '*'
    else:
        return ' '

def callback(in_data, frame_count, time_info, status):
    audio_data = numpy.fromstring(in_data, dtype=numpy.float32)
    X = numpy.log(abs(numpy.fft.fft(audio_data)))
    print( ''.join(g(z > 1.5) for z in X[:140]) )
    return (in_data, pyaudio.paContinue)

stream = p.open(format=pyaudio.paFloat32,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                output=True,
                stream_callback=callback)

stream.start_stream()

while stream.is_active():
    time.sleep(0.2)

stream.stop_stream()
stream.close()

p.terminate()
