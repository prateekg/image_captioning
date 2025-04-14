import onnxruntime as ort
from transformers import ViTImageProcessor, AutoTokenizer
from PIL import Image
import torch

# Load tokenizer and processor
processor = ViTImageProcessor.from_pretrained("nlpconnect/vit-gpt2-image-captioning")
tokenizer = AutoTokenizer.from_pretrained("nlpconnect/vit-gpt2-image-captioning")

# Load ONNX session
session = ort.InferenceSession("image_captioning_vit_encoder.onnx")

def preprocess(image: Image.Image):
    inputs = processor(images=image, return_tensors="pt")
    return inputs.pixel_values

def generate_caption(image: Image.Image):
    pixel_values = preprocess(image).numpy()
    
    # Run inference
    outputs = session.run(None, {"pixel_values": pixel_values})
    
    # Postprocess
    generated_ids = torch.tensor(outputs[0])
    caption = tokenizer.decode(generated_ids[0], skip_special_tokens=True)
    return caption
