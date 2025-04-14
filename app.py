from fastapi import FastAPI, File, UploadFile
from PIL import Image
import io
from model_utils import generate_caption

app = FastAPI()

@app.post("/generate_caption/")
async def caption(file: UploadFile = File(...)):
    image = Image.open(io.BytesIO(await file.read())).convert("RGB")
    caption = generate_caption(image)
    return {"caption": caption}
