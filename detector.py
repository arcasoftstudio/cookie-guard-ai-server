from ultralytics import YOLO
import numpy as np

# Carica il modello YOLOv8 (puoi sostituire con uno personalizzato)
model = YOLO("yolov8n.pt")  # oppure "cookie_button.pt" se ne hai uno addestrato

def detect_button(image_pil):
    image_np = np.array(image_pil)

    results = model.predict(source=image_np, conf=0.3)
    detections = results[0].boxes.xyxy.cpu().numpy()

    if len(detections) == 0:
        return {"status": "not_found"}

    # Prende il centro del primo box rilevato
    x1, y1, x2, y2 = detections[0]
    x = int((x1 + x2) / 2)
    y = int((y1 + y2) / 2)

    return {
        "status": "ok",
        "x": x,
        "y": y
    }
