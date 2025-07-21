from fastapi import FastAPI, File, UploadFile
import whisper
import io

# Load the Whisper model
model = whisper.load_model("base")

app = FastAPI()

@app.post("/transcribe/")
async def transcribe_audio(file: UploadFile = File(...)):
    audio_data = await file.read()
    audio_file = io.BytesIO(audio_data)
    result = model.transcribe(audio_file)
    return {"text": result["text"]}
