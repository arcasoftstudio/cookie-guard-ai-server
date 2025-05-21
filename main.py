from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from detector import detect_button
from PIL import Image
import io

app = FastAPI()

# CORS per estensione browser
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/detect")
async def detect(file: UploadFile = File(...)):
    image_data = await file.read()
    image = Image.open(io.BytesIO(image_data)).convert("RGB")
    result = detect_button(image)
    return result
