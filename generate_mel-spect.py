#generating the mel-spectrogram
import librosa
import librosa.display
import matplotlib.pyplot as plt

# Function to display a mel spectrogram
def display_mel_spectrogram(mel_spec, title, save_path):
    fig, ax = plt.subplots(figsize=(10, 4))
    img = librosa.display.specshow(mel_spec, x_axis='time', y_axis='mel', ax=ax)
    ax.set(title=title)
    fig.colorbar(img, ax=ax, format="%+2.0f dB")
    plt.savefig(save_path, bbox_inches='tight', dpi=100)
    plt.close(fig)

# Visualize and save clean audio mel spectrogram
display_mel_spectrogram(clean_audio_mel[0], 'Clean Audio Mel-Spectrogram', 'clean_audio_mel.png')

# Visualize and save noise audio mel spectrogram
display_mel_spectrogram(noise_audio_mel[0], 'Noise Audio Mel-Spectrogram', 'noise_audio_mel.png')

# Visualize and save noisy audio mel spectrogram
display_mel_spectrogram(noisy_audio_mel[0], 'Noisy Audio Mel-Spectrogram', 'noisy_audio_mel.png')

#get the directory
import os
print(os.getcwd()) --> #/mnt/data0/ag918/DNS-Challenge/output_mel
 
