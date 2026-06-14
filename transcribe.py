import whisper
import json

print("Cargando modelo Whisper...")

model = whisper.load_model("medium")

print("Analizando Nothing Else Matters...")

result = model.transcribe(
    "song.mp3",
    word_timestamps=True
)

lyrics = []

for segment in result["segments"]:
    lyrics.append({
        "text": segment["text"].strip(),
        "start": segment["start"],
        "end": segment["end"]
    })


with open("lyrics.json", "w", encoding="utf-8") as file:
    json.dump(
        lyrics,
        file,
        indent=4,
        ensure_ascii=False
    )

print("")
print("============================")
print("lyrics.json creado correctamente")
print("============================")