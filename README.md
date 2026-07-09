# 🖼️ AI Image & Text Recognition System

## 📌 Overview

The **AI Image & Text Recognition System** is a Python-based application developed as part of the **DecodeLabs Artificial Intelligence Internship – Project 4**.

This project demonstrates two important Artificial Intelligence applications:

* **Image Recognition** using TensorFlow's pre-trained **MobileNetV2** model.
* **Text Recognition (OCR)** using **Tesseract OCR** and **PyTesseract**.

The application allows users to identify objects in images and extract text from images through a simple command-line interface.

---

## 🚀 Features

### 🖼️ Image Recognition

* Recognizes objects in images using a pre-trained deep learning model.
* Displays the **Top 3 predictions** with confidence scores.
* Uses **MobileNetV2** trained on the ImageNet dataset.

### 📝 Text Recognition (OCR)

* Extracts text from image files.
* Supports JPG, JPEG, and PNG image formats.
* Uses **Tesseract OCR** for accurate text extraction.

---

## 🛠️ Technologies Used

* Python 3.12
* TensorFlow
* MobileNetV2
* NumPy
* Pillow (PIL)
* PyTesseract
* Tesseract OCR

---

## 📂 Project Structure

```text
AI-Project-4/
│
├── image_recognition.py
├── text_recognition.py
├── images/
│   ├── panda.jpg
│   ├── sunflower.jpg
│   ├── text.png
│   └── text2.jpg
├── screenshots/
│   ├── image_output.png
│   └── text_output.png
├── requirements.txt
├── README.md
└── .gitignore
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/Romesa-Farooq/image-text-recognition.git
```

### 2. Open the project folder

```bash
cd image-text-recognition
```

### 3. Create a virtual environment

```bash
python -m venv .venv
```

### 4. Activate the virtual environment

**Windows**

```bash
.venv\Scripts\activate
```

### 5. Install the required libraries

```bash
pip install -r requirements.txt
```

### 6. Install Tesseract OCR

Download and install **Tesseract OCR**.

After installation, update the path inside `text_recognition.py` if necessary.

Example:

```python
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
```

---

# ▶️ Running the Project

## Image Recognition

Run:

```bash
python image_recognition.py
```

Example:

```text
Loading AI Model...

Enter image name:
panda.jpg

Recognizing image...

Top Predictions

1. giant_panda (99.82%)
2. lesser_panda (0.12%)
3. llama (0.03%)
```

---

## Text Recognition

Run:

```bash
python text_recognition.py
```

Example:

```text
Enter image name:
text.png

Detected Text

Hello DecodeLabs
Artificial Intelligence Internship
```

## 📖 Learning Outcomes

Through this project, I learned:

* How pre-trained deep learning models perform image recognition.
* Image preprocessing using TensorFlow.
* Optical Character Recognition (OCR) using Tesseract.
* Working with image files using Pillow.
* Building AI applications in Python.
* Handling user input and file operations.

---

## 🎯 Future Improvements

* Develop a graphical user interface (GUI).
* Support webcam-based image recognition.
* Detect multiple objects in a single image.
* Improve OCR accuracy through image preprocessing.
* Enable batch processing of multiple images.

---

## 👩‍💻 Author

**Romesa Farooq**

BS Software Engineering Student

Artificial Intelligence & Flutter Enthusiast

GitHub: https://github.com/Romesa-Farooq

---

## 📄 License

This project was developed for educational purposes as part of the **DecodeLabs Artificial Intelligence Internship Program**.
