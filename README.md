# 🎙️ VocalEmote

> Detect emotions in real-time from your speech using NLP and deep learning.

VocalEmote is a Python project that captures audio from your microphone, transcribes it into text using Google's Speech Recognition API, and then analyzes the emotion behind your spoken words using a fine-tuned transformer model from Hugging Face.

---

## 1️⃣ Overview

This project combines **speech recognition** with **natural language emotion detection** to provide a simple interface for understanding how emotions are conveyed through speech.

---

## 2️⃣ Features

- 🎤 **Real-Time Speech Input**: Captures your voice from the microphone.
- 🗣️ **Speech-to-Text**: Converts spoken words to text using Google Speech Recognition.
- 🧠 **Emotion Detection**: Uses a pre-trained transformer model (`j-hartmann/emotion-english-distilroberta-base`) to classify emotions like *joy, sadness, anger, fear, surprise,* and more.
- 🖥️ **Terminal Output**: Displays both transcribed text and detected emotion clearly in the terminal.

---

## 3️⃣ Tech Stack

- **Python 3.7+**
- **[SpeechRecognition](https://pypi.org/project/SpeechRecognition/)** – to process and recognize voice input.
- **[Transformers (Hugging Face)](https://huggingface.co/transformers/)** – for running the emotion detection model.
- **[PyTorch](https://pytorch.org/)** – backend engine for transformer inference.
- **Pretrained Model** – `j-hartmann/emotion-english-distilroberta-base`

---

## 4️⃣ Setup & Installation

### 🔧 Clone the Repository

```bash
git clone https://github.com/yourusername/vocalemote.git
cd vocalemote
```

### Create and Activate a Virtual Environment (Recommended)
```Windows
python -m venv venv
venv\Scripts\activate

```

### Install Dependencies
```
pip install -r requirements.txt
```
---

## 5️⃣ Usage
Run the app:
```
python app.py
```
---

## 📌 Notes
Internet connection is required for both speech-to-text and transformer model inference.

Use a good quality microphone for better accuracy.

---

## 🙋‍♀️ Acknowledgements
Hugging Face Transformers

Google Speech Recognition API

---

## Ouput

