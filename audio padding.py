import os
import wave
import contextlib
from pydub import AudioSegment

clean_base_dir = "/mnt/data0/ts468/data/DNS-Challenge/datasets_fullband/clean_fullband/datasets_fullband/clean_fullband/italian_speech/M-AILABS_Speech_Dataset/it_IT_128hrs_16k/mix"

max_duration = 0

# Function to recursively find the maximum duration of audio files in a directory
def find_max_duration(directory):
    global max_duration
    for subdir, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".wav"):
                file_path = os.path.join(subdir, file)
                with contextlib.closing(wave.open(file_path,'r')) as f:
                    frames = f.getnframes()
                    rate = f.getframerate()
                    duration = frames / float(rate)
                    if duration > max_duration:
                        max_duration = duration

# Find maximum duration of clean audio
find_max_duration(clean_base_dir)
print(f"Maximum duration of clean audio files: {max_duration:.2f} seconds")

# Set target duration to 19 seconds
target_duration = 19
target_duration_ms = int(target_duration * 1000)  # Convert to milliseconds for pydub

# Function to pad audio to target length
def pad_audio(audio_path, target_length_ms):
    sound = AudioSegment.from_file(audio_path, format="wav")
    if len(sound) < target_length_ms:
        silence = AudioSegment.silent(duration=target_length_ms - len(sound))
        padded_sound = sound + silence
        return padded_sound
    else:
        return sound[:target_length_ms]

# Function to process all WAV files in a directory
def process_directory(input_dir, output_dir):
    for subdir, _, files in os.walk(input_dir):
        for file in files:
            if file.endswith(".wav"):
                input_path = os.path.join(subdir, file)
                
                # Create the same subdirectory structure in the output directory
                relative_path = os.path.relpath(subdir, input_dir)
                output_subdir = os.path.join(output_dir, relative_path)
                os.makedirs(output_subdir, exist_ok=True)
                
                output_path = os.path.join(output_subdir, file)
                
                # Pad the audio and export
                padded_audio = pad_audio(input_path, target_duration_ms)
                padded_audio.export(output_path, format="wav")
                print(f"Processed: {input_path} -> {output_path}")

# Set up output directory
output_base_dir = "clean_padd_audio.wav"  # Replace with your desired output path
os.makedirs(output_base_dir, exist_ok=True)

# Process and pad all clean audio files
process_directory(clean_base_dir, output_base_dir)
print("All files have been processed and padded to 19 seconds.")
