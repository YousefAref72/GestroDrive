# Gesture-Controlled and Voice-Controlled Smart Car 🚗💡

## Project Overview
This project introduces an innovative solution for hands-free vehicle navigation using voice and hand gesture controls. The car is designed to navigate through complex environments, avoiding obstacles while responding to real-time voice commands and hand gestures. By leveraging advanced machine learning and computer vision techniques, the system provides a seamless and intuitive user experience. 🤖

## Features
- **Voice-Controlled Navigation** 🎙️: Navigate the car effortlessly using spoken commands.
- **Gesture-Controlled Navigation** ✋: Use hand gestures to guide the car with precision.
- **Obstacle Avoidance** 🚧: Real-time detection and avoidance of obstacles ensure smooth movement.
- **Real-Time Response** ⚡: Instant processing of voice and gesture inputs for seamless control.
- **Advanced Computer Vision** 👀: Utilizes **MediaPipe Hands** for high-fidelity hand tracking.

## MediaPipe Hands Integration

### Hand and Finger Tracking
The core of our gesture control system is powered by **MediaPipe Hands**, an advanced hand and finger tracking solution that employs machine learning to infer 21 3D hand landmarks from a single frame. This enables robust and real-time gesture recognition even on mobile devices.

#### Key Benefits:
- **High-Precision Tracking** ✅: Detects hand landmarks with 95.7% accuracy.
- **Multi-Hand Support** ✌️: Recognizes gestures from multiple hands simultaneously.
- **Optimized for Mobile** 📱: Delivers real-time performance on mobile and embedded systems.

### Palm Detection Model
The palm detection model plays a critical role in accurately locating hand positions within an image. Unlike traditional hand detection methods, this model is optimized for real-time applications and can effectively handle occlusions.

- **Single-Shot Detector** 🔍: Designed for fast and efficient palm detection.
- **Context-Aware** 🧠: Uses additional contextual features (arm, body) for improved accuracy.
- **Non-Maximum Suppression** 🚀: Effectively handles multiple hand occlusions.

### Hand Landmark Model
After detecting the palm, the hand landmark model predicts precise 3D key points for hand gestures. This allows the system to interpret complex gestures with minimal latency.

- **21 Key-Point Detection** 🎯: Accurately tracks hand-knuckle coordinates.
- **Robust to Occlusions** 🛡️: Performs well even when parts of the hand are obscured.
- **Extensive Training Data** 📊: Trained on a dataset of ~30,000 annotated real-world images.

## How It Works
1. **User Input** 🎙️: The system receives a voice command or detects a hand gesture.
2. **Palm Detection** ✋: Identifies the location of the user's hand using the palm detection model.
3. **Gesture Recognition** 🤖: The hand landmark model processes hand movements and converts them into commands.
4. **Navigation and Control** 🚗: The car moves according to the recognized voice or gesture command, avoiding obstacles as needed.

## Demo Video 🎥
[Click here to watch the demo](video/demo.mp4)


## Setup & Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/your-repository/gesture-controlled-car.git
   ```

2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Install MediaPipe**
   ```bash
   pip install mediapipe
   ```

4. **Run the Application**
   ```bash
   python app.py
   ```

## Contributing
We welcome contributions to enhance the system. If you’d like to contribute, please fork the repository, create a branch, and submit a pull request. 🤝

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact
For inquiries or collaboration, reach out at:
**Email:** yousefmostafa222004@gmail.com 📧

