from transformers import pipeline
from PIL import Image
import torch
import os

print("Loading Image Captioning AI...")

device = 0 if torch.cuda.is_available() else -1

captioner = pipeline(
    "image-to-text",
    model="Salesforce/blip-image-captioning-base",
    device=device
)

print("AI Model Loaded Successfully!")


def generate_caption(image_path):
    try:
        if not os.path.exists(image_path):
            print("Error: Image file not found!")
            return

        image = Image.open(image_path).convert("RGB")

        result = captioner(image, max_new_tokens=50)

        caption = result[0]["generated_text"]

        print("\nGenerated Image Caption:")
        print(caption)

    except Exception as e:
        print("Error:", e)


while True:
    print("\n===== IMAGE CAPTIONING AI =====")
    image_path = input("Enter image path (or type 'exit' to quit): ").strip()

    if image_path.lower() == "exit":
        print("Goodbye!")
        break

    generate_caption(image_path)