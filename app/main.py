from downloader import download_audio
from transcriber import transcribe
import os

url = input("Cole a URL do YouTube: ")

audio_file = download_audio(url)

print("\nTranscrevendo...\n")

text = transcribe(audio_file)

filename = os.path.basename(audio_file)
output_file = f"transcripts/{filename}.txt"

with open(output_file, "w", encoding="utf-8") as f:
    f.write(text)

print("\nConcluído!")
print(f"Arquivo salvo em: {output_file}")