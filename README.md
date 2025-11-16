# SafeCrossAI_Apps4Athens2025

🚸 **A Computer Vision Project to Help Vulnerable Pedestrians Cross Roads Safely**

SafeCrossAI is an AI-powered safety system designed to detect and assist disabled individuals and parents with young children when crossing the road. Using real-time object detection on a Raspberry Pi 5, this project aims to enhance pedestrian safety through intelligent monitoring.

---

## 🎯 Project Goals

- Detect wheelchairs, strollers, and vulnerable pedestrians near crosswalks
- Provide real-time alerts to improve road crossing safety
- Offer an affordable, edge-computing solution using Raspberry Pi hardware
- Support Athens 2025 accessibility initiatives

---

## 🛠️ Hardware Components

| Component | Specification |
|-----------|---------------|
| **Raspberry Pi 5** | 8GB RAM |
| **Camera** | Pi Night-Vision Camera (or compatible USB webcam) |
| **Power Supply** | Official Raspberry Pi 5 power adapter (5V, 5A recommended) |
| **Storage** | MicroSD card (32GB+ recommended) |

### Optional Components
- Enclosure/case for outdoor deployment
- Active cooling fan for sustained performance
- External battery pack for portable operation

---

## 📋 Software Requirements

### System Dependencies
```bash
# Update system
sudo apt update && sudo apt upgrade -y

# Install Python and pip
sudo apt install python3 python3-pip -y

# Install OpenCV dependencies
sudo apt install libopencv-dev python3-opencv -y
```

### Python Libraries
```bash
pip3 install ultralytics opencv-python
```

---

## 🚀 Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/SafeCrossAI_Apps4Athens2025.git
cd SafeCrossAI_Apps4Athens2025
```

### 2. Download YOLO Model
Place your trained YOLO model (`best.pt`) in the project directory:
```bash
mkdir -p yolo_models
# Copy your model file to yolo_models/best.pt
```

### 3. Prepare Test Video (Optional)
Place your test video in the project directory or use a live camera feed.

### 4. Run the Detection System
```bash
python3 detect.py
```

---

## 💻 Code Overview

The main detection script (`detect.py`) performs the following:

1. **Loads a custom YOLO model** trained to detect wheelchairs, strollers, and pedestrians
2. **Processes video input** from file or live camera stream
3. **Runs inference on Raspberry Pi 5 CPU** with optimized image size (480px)
4. **Displays annotated frames** with bounding boxes and class labels
5. **Exits on 'q' key press**

### Key Configuration Parameters

```python
# Model path
model_path = "/home/pi/yolo_models/best.pt"

# Confidence threshold (0-1)
CONF = 0.5

# Video source (file path or 0 for webcam)
VIDEO_PATH = "/home/pi/wheelchair_test.mp4"  # or use 0 for live camera

# Image size for inference (lower = faster, but less accurate)
model.overrides["imgsz"] = 480  # Try 320 for higher FPS
```

---

## 🔧 Performance Optimization Tips

### For Better Speed
- Reduce `imgsz` to 320 or 416
- Lower `CONF` threshold if you're getting too many false positives
- Use a lighter YOLO model (YOLOv8n instead of YOLOv8s/m/l)

### For Better Accuracy
- Increase `imgsz` to 640 (default)
- Use a larger YOLO model variant
- Adjust `CONF` threshold based on your use case

### Raspberry Pi 5 Specific
- Enable active cooling to prevent thermal throttling
- Overclock CPU (with adequate cooling)
- Use 64-bit Raspberry Pi OS for better performance

---

## 📊 Expected Performance

| Configuration | FPS (Approx.) | Accuracy |
|---------------|---------------|----------|
| imgsz=320, YOLOv8n | 8-12 FPS | Good |
| imgsz=480, YOLOv8n | 5-8 FPS | Better |
| imgsz=640, YOLOv8s | 2-4 FPS | Best |

*Performance varies based on model complexity and scene complexity*

---

## 📸 Using Live Camera

To use a live camera instead of a video file:

```python
# Replace VIDEO_PATH with camera index
VIDEO_PATH = 0  # For default USB camera
# or
VIDEO_PATH = "libcamera"  # For Pi Camera Module
```

For Pi Camera Module, you may need:
```bash
sudo apt install python3-picamera2
```

---

## 🤝 Contributing

Contributions are welcome! Please feel free to submit pull requests or open issues for:
- Model improvements
- Performance optimizations
- Additional safety features
- Documentation enhancements

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- Built for **Apps4Athens 2025** initiative
- Powered by **Ultralytics YOLOv8**
- Optimized for **Raspberry Pi 5**

---

## 📞 Contact

For questions or collaboration opportunities, please open an issue or reach out through GitHub.

**Together, we can make Athens roads safer for everyone! 🚸**
