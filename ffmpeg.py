"""
This script converts all wav files in a directory to mp3.

sox drum_samples_in/train/kick_01.wav -r 22050 --norm -b 16 -e signed-integer drum_samples_out/train/kick_01.wav remix -
sox in.wav --norm out.wav
sox in.wav out.wav remix -
sox in.wav -b 16 -e signed-integer out.wav

ffmpeg -i drum_samples_in/train/kick_01.wav drum_samples_out/train/kick_01.mp3 
"""
from pathlib import Path
import os

for p in Path().glob('drum_samples_in/test/*.wav'):
    input_wav = p.resolve()
    output_stem = input_wav.stem
    command = "ffmpeg -i {} drum_samples_out/test/{}.mp3".format(input_wav, output_stem)
    print(command)
    os.system(command)
