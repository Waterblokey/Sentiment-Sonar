#Trial program using whisper to convert mp4 file to text

import whisper

model = whisper.load_model("base")
result = model.transcribe("Speech-to-text/outro.mp4", language="en")
print(result["text"])

