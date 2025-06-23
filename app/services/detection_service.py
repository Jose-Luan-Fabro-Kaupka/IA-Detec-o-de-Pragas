from ultralytics import YOLO
from PIL import Image
import io
import pandas as pd

model = YOLO('/Users/joseluanfabrokaupka/Projetos/sistemas-inteligentes/model/best.pt')

def detect_image(image_bytes):
    from PIL import Image
    import io

    img = Image.open(io.BytesIO(image_bytes)).convert("RGB")
    results = model.predict(img, imgsz=640, conf=0.25)

    output = []
    for r in results:
        for box in r.boxes:
            cls_id = int(box.cls[0])
            output.append({
                'classe': model.names[cls_id],
                'confiança': float(box.conf[0]),
                'bbox': box.xyxy[0].tolist()
            })
    return output
