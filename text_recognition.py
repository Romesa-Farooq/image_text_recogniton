import os
import pytesseract
from PIL import Image

# Set the path to Tesseract OCR
pytesseract.pytesseract.tesseract_cmd = (
    r"C:\Program Files\Tesseract-OCR\tesseract.exe"
)
print("=" * 50)
print("        AI Text Recognition System")
print("=" * 50)

# Ask the user for the image name
image_name = input("\nEnter the image name (e.g., text.jpg): ")

# Create the complete image path
image_path = os.path.join("images", image_name)

# Check if the image exists
if not os.path.exists(image_path):
    print("\n❌ Image not found!")
    exit()

try:
    # Open the image
    img = Image.open(image_path)

    # Extract text from the image
    extracted_text = pytesseract.image_to_string(img)

    print("\n" + "=" * 50)
    print("Detected Text")
    print("=" * 50)

    # Check if any text was detected
    if extracted_text.strip():
        print(extracted_text)
    else:
        print("No text detected in the image.")

except Exception as e:
    print("\nAn error occurred:")
    print(e)