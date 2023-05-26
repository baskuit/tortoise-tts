 
import os
from pydub import AudioSegment

def convert_mp3_to_wav(mp3_file, wav_file, bitrate='192k'):
    # Load the MP3 file
    audio = AudioSegment.from_mp3(mp3_file)

    # Set the desired bitrate
    # audio = audio.set_frame_rate(44100).set_channels(2).set_bitrate(bitrate)

    # Export the audio to WAV format
    audio.export(wav_file, format='wav', bitrate=22050)

# Get the current directory
cur_dir = os.getcwd()

# Process each MP3 file in the current directory
for file_name in os.listdir(cur_dir):
    if file_name.endswith('.mp3'):
        mp3_file = os.path.join(cur_dir, file_name)
        wav_file = os.path.splitext(mp3_file)[0] + '.wav'
        convert_mp3_to_wav(mp3_file, wav_file)
        print(f"Converted {mp3_file} to {wav_file}")
