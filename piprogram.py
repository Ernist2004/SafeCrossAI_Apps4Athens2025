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

VIDEO_PATH = "/home/pi/wheelchair_test.mp4"  # <-- UPDATE THIS
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

    cv2.imshow("YOLO Detection (Raspberry Pi 5)", annotated)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
