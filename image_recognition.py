import numpy as np
import tensorflow as tf
from tensorflow.keras.applications.mobilenet_v2 import (
    MobileNetV2,
    preprocess_input,
    decode_predictions
)
from tensorflow.keras.preprocessing import image

print("Loading AI model...")
model = MobileNetV2(weights="imagenet")

# Ask user for image name
image_name = input("Enter image name (example: panda.jpg): ")

image_path = "images/" + image_name

try:
    # Load image
    img = image.load_img(image_path, target_size=(224, 224))

    # Convert image to array
    img_array = image.img_to_array(img)

    # Expand dimensions
    img_array = np.expand_dims(img_array, axis=0)

    # Preprocess image
    img_array = preprocess_input(img_array)

    print("\nRecognizing image...\n")

    # Predict
    predictions = model.predict(img_array)

    # Decode prediction
    result = decode_predictions(predictions, top=3)[0]

    print("Top Predictions:\n")

    for i, prediction in enumerate(result, start=1):
        name = prediction[1]
        confidence = prediction[2] * 100

        print(f"{i}. {name} ({confidence:.2f}%)")

except FileNotFoundError:
    print("\nImage not found!")