"""
musicinformationretrieval.com/realtime_spectrogram.py

PyAudio example: display a live log-spectrogram in the terminal.

For more examples using PyAudio:
    https://github.com/mwickert/scikit-dsp-comm/blob/master/sk_dsp_comm/pyaudio_helper.py
"""
import librosa
import numpy
import pyaudio
import time

# Define global variables.
CHANNELS = 1
RATE = 44100
FRAMES_PER_BUFFER = 1000
N_FFT = 4096
SCREEN_WIDTH = 178
ENERGY_THRESHOLD = 0.4

# Choose the frequency range of your log-spectrogram.
F_LO = librosa.note_to_hz('C2')
F_HI = librosa.note_to_hz('C9')
M = librosa.filters.mel(RATE, N_FFT, SCREEN_WIDTH, fmin=F_LO, fmax=F_HI)

p = pyaudio.PyAudio()

def generate_string_from_audio(audio_data):
    """
    This function takes one audio buffer as a numpy array and returns a
    string to be printed to the terminal.
    """
    # Compute real FFT.
    x_fft = numpy.fft.rfft(audio_data, n=N_FFT)

    # Compute mel spectrum.
    melspectrum = M.dot(abs(x_fft))

    # Initialize output characters to display.
    char_list = [' ']*SCREEN_WIDTH

    for i in range(SCREEN_WIDTH):

        # If there is energy in this frequency bin, display an asterisk.
        if melspectrum[i] > ENERGY_THRESHOLD:
            char_list[i] = '*'

        # Draw frequency axis guidelines.
        elif i % 30 == 29:
            char_list[i] = '|'

    # Return string.
    return ''.join(char_list)

def callback(in_data, frame_count, time_info, status):
    audio_data = numpy.fromstring(in_data, dtype=numpy.float32)
    print( generate_string_from_audio(audio_data) )
    return (in_data, pyaudio.paContinue)

stream = p.open(format=pyaudio.paFloat32,
                channels=CHANNELS,
                rate=RATE,
                input=True,   # Do record input.
                output=False, # Do not play back output.
                frames_per_buffer=FRAMES_PER_BUFFER,
                stream_callback=callback)

stream.start_stream()

while stream.is_active():
    time.sleep(0.100)

stream.stop_stream()
stream.close()

p.terminate()
