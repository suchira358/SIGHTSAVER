import torch
from PIL import Image
from transformers import CLIPProcessor, CLIPModel

model = CLIPModel.from_pretrained("openai/clip-vit-base-patch32")
processor = CLIPProcessor.from_pretrained("openai/clip-vit-base-patch32")

labels = [
    "shoes",
    "t shirt",
    "dress",
    "laptop",
    "phone",
    "cosmetics",
    "bag"
]

def detect_product(image_path):

    image = Image.open(image_path)

    inputs = processor(text=labels, images=image, return_tensors="pt", padding=True)

    outputs = model(**inputs)

    probs = outputs.logits_per_image.softmax(dim=1)

    idx = probs.argmax()

    return labels[idx]
