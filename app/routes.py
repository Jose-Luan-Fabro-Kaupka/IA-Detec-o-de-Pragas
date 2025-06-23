import importlib.util
from app.services import detection_service

@app.route('/detect', methods=['POST'])
def detect():
    if 'image' not in request.files:
        return jsonify({'error': 'Nenhuma imagem enviada'}), 400

    file = request.files['image']
    img_bytes = file.read()
    img = Image.open(io.BytesIO(img_bytes)).convert('RGB')

    # Detecção com o modelo
    results = model(img, size=640)
    detections = results.pandas().xyxy[0]  # Bounding boxes com pandas

    output = []
    for _, row in detections.iterrows():
        output.append({
            'classe': row['name'],
            'confiança': float(row['confidence']),
            'bbox': [float(row['xmin']), float(row['ymin']), float(row['xmax']), float(row['ymax'])]
        })

    return jsonify({'detecções': output})

