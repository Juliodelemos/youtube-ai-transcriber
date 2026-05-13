from faster_whisper import WhisperModel

model = WhisperModel(
    "small",
    device="cpu",
    compute_type="int8"
)

def transcribe(audio_file):

    segments, info = model.transcribe(
        audio_file,
        beam_size=5,
        language="pt",
        vad_filter=True
    )

    text = ""

    for segment in segments:
        text += f"[{segment.start:.2f}s -> {segment.end:.2f}s] "
        text += segment.text + "\n"

    return text