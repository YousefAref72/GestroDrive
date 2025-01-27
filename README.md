# Smart Medicine Delivery Car - README

## Project Overview
This project introduces an innovative solution for hospital medicine delivery using a smart, voice- and gesture-controlled car. Designed to navigate busy hospital corridors, this system can deliver medicine efficiently, saving valuable time, money, and lives. With seamless obstacle avoidance and real-time response, our smart car is revolutionizing hospital logistics.

## Features
- **Voice-Controlled Navigation:** Simply speak commands to direct the smart car to its destination.
- **Gesture-Controlled Navigation:** Use hand gestures to guide the car through the hospital.
- **Obstacle Avoidance:** The system detects and avoids obstacles, ensuring safe and smooth navigation.
- **Real-Time Response:** Thanks to MediaPipe Hands integration, the car can respond instantly to voice or hand gesture inputs.
- **Efficient Medicine Delivery:** Ensures quick, safe transport of medicine to hospital rooms, improving patient care and hospital efficiency.

## MediaPipe Hands Integration

### Hand and Finger Tracking
The core of our gesture-controlled navigation system is powered by **MediaPipe Hands**, a high-fidelity hand and finger tracking solution. MediaPipe Hands leverages machine learning (ML) to infer 21 3D hand landmarks from just a single frame, achieving real-time performance even on mobile devices.

Key benefits of integrating MediaPipe Hands into the system:
- **Real-time Hand Tracking:** The system detects and tracks hand gestures in real-time, enabling precise control of the smart car.
- **Multiple Hand Support:** MediaPipe can detect and track multiple hands, allowing flexibility in gesture control.
- **Mobile-Friendly:** The system is optimized for performance on mobile devices, ensuring portability and ease of use.

### Palm Detection Model
The palm detection model plays a crucial role in identifying hand locations in the environment. It is designed to work effectively across varying hand sizes and even in self-occluded scenarios (e.g., handshakes).

- **Single-Shot Detector:** Optimized for mobile, real-time use.
- **Effective Self-Occlusion Handling:** The model uses non-maximum suppression to handle multiple hand occlusions, ensuring accurate palm detection.
- **Context-Aware:** Incorporates additional context, like arm or body features, to improve hand localization accuracy.
- **High Precision:** Achieves an average precision of 95.7% in palm detection.

### Hand Landmark Model
After detecting the palm, the hand landmark model identifies and localizes 21 key 3D hand coordinates within the detected region. This model is robust to partial visibility and self-occlusions, ensuring accurate gesture interpretation.

- **Precise Keypoint Localization:** The model locates 21 hand-knuckle coordinates with high accuracy.
- **Training Data:** The model was trained using approximately 30,000 real-world images with manually annotated 3D coordinates.
- **Synthetic Data:** To improve robustness, synthetic hand models were also used during training for various hand poses.

## How It Works

1. **Voice Command or Gesture Input:** The user issues a voice command or uses a hand gesture to instruct the car.
2. **Palm Detection:** The system detects the palm using the MediaPipe Hands palm detection model.
3. **Gesture Tracking:** The hand landmark model tracks the 21 key points of the hand and interprets the gesture to control the car's movement.
4. **Navigation and Obstacle Avoidance:** The car navigates the hospital corridors, avoiding obstacles in real-time.
5. **Medicine Delivery:** The car delivers medicine to the designated room with precision and speed.

## Setup & Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/your-repository/smart-medicine-delivery-car.git
   ```

2. **Install Dependencies**
   Install the necessary dependencies by running:
   ```bash
   pip install -r requirements.txt
   ```

3. **MediaPipe Installation**
   To use the MediaPipe Hands functionality, ensure you have installed MediaPipe:
   ```bash
   pip install mediapipe
   ```

4. **Run the Application**
   Start the car navigation system by running:
   ```bash
   python app.py
   ```

## Contributing
We welcome contributions to enhance the functionality of the smart medicine delivery car. If you'd like to contribute, please fork the repository, create a branch, and submit a pull request.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments
- **MediaPipe Hands:** For providing the cutting-edge hand and gesture tracking technology.
- **TensorFlow:** For enabling real-time machine learning inference.
- **The Open Source Community:** For their continuous contributions to machine learning and computer vision.
