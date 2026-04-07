import os
import uuid
import shutil
import subprocess
from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from ultralytics import YOLO

UPLOAD_DIR = "/tmp/uploads"
RESULTS_DIR = "/tmp/results"

os.makedirs(UPLOAD_DIR, exist_ok=True)
os.makedirs(RESULTS_DIR, exist_ok=True)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

model = YOLO("yolov8n.pt")

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/upload")
async def upload_video(file: UploadFile = File(...)):
    video_id = str(uuid.uuid4())
    input_path = f"{UPLOAD_DIR}/{video_id}.mp4"
    
    with open(input_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    output_path = f"{RESULTS_DIR}/{video_id}_output.mp4"

    process_video(input_path, output_path)

    return {
        "video_id": video_id,
        "output": output_path
    }

def process_video(input_path, output_path):
    results = model(input_path)

    # Just copy video for now (replace with real clipping later)
    shutil.copy(input_path, output_path)
