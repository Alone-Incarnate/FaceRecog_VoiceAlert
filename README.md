
# 👤 Face Recognition System with Voice Alert 🔊

Welcome to the **Face Recognition System with Voice Alert**! This application utilizes the power of facial recognition technology to identify individuals in real-time. When a recognized face is detected from a predefined list, the system provides a voice alert.

## 📸 Features

- **Real-time Face Recognition**: Detect and recognize faces using a webcam.
- **Voice Alerts**: Get audio notifications when specific individuals are detected.
- **Easy Setup**: Simply add images of individuals to the training directory.

## ⚙️ Getting Started

### Prerequisites

Before you begin, ensure you have the following libraries installed:

- `face_recognition`
- `opencv-python`
- `numpy`
- `pyttsx3`

### Installation

1. Clone the repository or download the code.
2. Install the required libraries using your preferred package manager.

### 📂 Data Preparation

- Place images of known individuals in the `train` directory. The application will use these images to learn and recognize faces.

## 🖼️ Usage

1. Run the application.
2. Allow the webcam to capture video.
3. The application will continuously recognize faces and provide voice alerts for individuals on the predefined list.

## 🤖 How It Works

- The application uses the `face_recognition` library to detect and encode faces.
- When a face is detected, it compares the encoding with known encodings to identify the individual.
- If a recognized individual is found in the specified list, a voice alert is triggered.


## 📝 Acknowledgments

- Special thanks to **face_recognition** for the powerful facial recognition capabilities.
- Thanks to **OpenCV** for providing robust image processing functionalities.
- Appreciation for **pyttsx3** for enabling voice alerts.


Happy recognizing! 🎊
