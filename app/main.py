from flask import Flask, request, jsonify
from app.torch_utils import transform_image, get_prediction

app = Flask(__name__)

def allowed_file(file_name):
    return '.' in file_name and file_name.rsplit('.', 1)[1].lower() in {'png', 'jpeg', 'tif', 'jpg'}

@app.route('/predict', method=['POST'])
def predict():
    if request.method == 'POST':
        file = request.files.get('file')
        if file is None or file.filename == '':
            return jsonify({'error':'no file'})
        if not allowed_file(file.filename):
            return jsonify({'error':'format not supported'})    

        try:
            img_bytes = file.read()
            tensor = transform_image(img_bytes)
            prediction = get_prediction(tensor)
            data = {'prediction':prediction.item()}
            return jsonify(data)
        except Exception as e:
            print(e)
            return jsonify({'error': e})

    # Load image
    # image -> tensor
    # Prediction
    # return json
    return jsonify({'result': 1})