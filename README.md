SafeCrossAI_Apps4Athens2025

A project designed to help disabled individuals and parents with young children cross the road safely by leveraging artificial intelligence (AI) for real-time object detection. This project uses a Raspberry Pi and a camera to monitor crosswalks and detect objects, providing feedback to help people safely cross roads.

Hardware Components

Raspberry Pi 5 (8GB RAM): The core processing unit for running the AI model and managing the video feed.

Pi Night-Vision Camera or any webcam: Used for capturing real-time video of the surroundings to detect pedestrians, vehicles, and other relevant objects.

Software Components

Python 3.x: Programming language used for developing the AI model and handling video streams.

OpenCV: Used for video capture, processing, and visual output.

YOLO (You Only Look Once): A state-of-the-art, real-time object detection model. YOLO is used to identify people, vehicles, and other objects in the camera feed.

Ultralytics YOLO: A Python package that simplifies the use of YOLO for object detection tasks.

Project Overview

This system uses the YOLOv5 object detection model to analyze video frames in real time. The detection model is capable of identifying and locating pedestrians, vehicles, and other relevant objects in the video feed. By integrating a camera with the Raspberry Pi, the system can provide a live stream that identifies hazards and obstacles for pedestrians, including people with disabilities or those with young children.

Key Features:

Real-time object detection for improved pedestrian safety.

Optimized for use with a Raspberry Pi 5.

Provides visual feedback using a webcam or Pi camera.

Supports low-power CPU mode (ideal for Raspberry Pi environments).

Code Overview
Requirements

Install Python dependencies:

pip install opencv-python ultralytics


Download YOLO Model:

You will need a pre-trained YOLO model to use with this project. For this, download the YOLOv5 model from the official Ultralytics repository
 or use your own custom-trained model. Make sure to update the model_path to the location of your model file.

Set up the video source:

You can either use a webcam or a pre-recorded video file for testing. The following code works with both video files and webcams (just update VIDEO_PATH).

Example Code
import cv2
from ultralytics import YOLO

# ---------------------------
# Load YOLO Model
# ---------------------------
model_path = "/home/pi/yolo_models/best.pt"   # <-- UPDATE THIS
model = YOLO(model_path)

# ---------------------------
# Confidence threshold
# ---------------------------
CONF = 0.5   # 0–1

# ---------------------------
# Open video file or camera
# ---------------------------

VIDEO_PATH = "/home/pi/wheelchair_test.mp4"  # <-- UPDATE THIS for video files
cap = cv2.VideoCapture(VIDEO_PATH)

if not cap.isOpened():
    print("Error: Could not open video source.")
    exit()

# Reduce input size for faster CPU inference
model.overrides["imgsz"] = 480  # You can test 320 for more speed

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # YOLO inference
    results = model.predict(
        frame,
        conf=CONF,
        verbose=False,
        device="cpu",   # ensure CPU mode
        half=False      # FP16 not supported on CPU
    )

    annotated = results[0].plot()

    # Display the frame with detection annotations
    cv2.imshow("YOLO Detection (Raspberry Pi 5)", annotated)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()

Code Explanation:

Loading the YOLO Model: The YOLO() function loads the pre-trained model. You must provide the path to your model (best.pt in this example).

Video Capture: This is set to either capture a live webcam feed or play a pre-recorded video (change VIDEO_PATH).

Real-time Object Detection: Each frame from the video feed is passed through the YOLO model to detect objects. Detected objects are annotated on the frame.

Display: The annotated video is shown in a window using cv2.imshow().

Model Training

To train your own custom YOLO model, follow the instructions in the Ultralytics YOLO documentation
 on how to collect data, label it, and fine-tune the model.

Setting Up the System

Install Raspberry Pi OS: Ensure your Raspberry Pi 5 is running the latest Raspberry Pi OS.

Connect the Camera: Connect your Pi camera or external webcam.

Install Dependencies: Follow the installation steps to install OpenCV and YOLO dependencies.

Run the Script: Run the Python script to start real-time object detection.

Conclusion

The SafeCrossAI_Apps4Athens2025 project is designed to provide a cost-effective and scalable way to enhance road safety for people with disabilities and parents with young children. By leveraging AI for real-time object detection and integrating it into a Raspberry Pi-based system, this solution can significantly improve pedestrian safety in urban environments.
