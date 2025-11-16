import cv2
from ultralytics import YOLO

# ---------------------------
# Load YOLO Model
# ---------------------------
model_path = "best_yolo_model.pt"
model = YOLO(model_path)

# ---------------------------
# Settings
# ---------------------------
CONF = 0.3          # confidence threshold
FRAME_SKIP = 0      # Process 1 frame, skip next 2  (change this number)

VIDEO_PATH = "gettyimages-495919732-640_adpp.mp4"
OUTPUT_PATH = "yolo_output.mp4"

cap = cv2.VideoCapture(VIDEO_PATH)

if not cap.isOpened():
    print("Error: Could not open video source.")
    exit()

model.overrides["imgsz"] = 480

# ---------------------------
# VideoWriter
# ---------------------------
fourcc = cv2.VideoWriter_fourcc(*"mp4v")
fps = int(cap.get(cv2.CAP_PROP_FPS))
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
out = cv2.VideoWriter(OUTPUT_PATH, fourcc, fps, (width, height))

frame_count = 0

# ---------------------------
# Loop
# ---------------------------
while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Skip frames
    if frame_count % (FRAME_SKIP + 1) != 0:
        # Still write original frame to output to keep timing consistent
        out.write(frame)
        frame_count += 1
        continue

    # -----------------------------------
    # YOLO inference
    # -----------------------------------
    results = model.predict(
        frame,
        conf=CONF,
        verbose=False,
        device="cpu",
        half=False
    )

    annotated = results[0].plot()

    cv2.imshow("YOLO Detection (Raspberry Pi 5)", annotated)

    # Save output frame
    out.write(annotated)

    frame_count += 1

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
out.release()
cv2.destroyAllWindows()

print("Done! Output saved to:", OUTPUT_PATH)
