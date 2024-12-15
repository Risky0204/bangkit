from flask import Flask, request, jsonify
import numpy as np
import tensorflow as tf
import pickle

# Inisialisasi Flask
app = Flask(__name__)

# Muat model dan scaler
model = tf.keras.models.load_model('model.h5')
scaler = pickle.load(open('scaler.pkl', 'rb'))

# Endpoint untuk prediksi
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Ambil data JSON dari request
        data = request.json
        input_data = np.array([data['features']])  # Contoh input JSON: {"features": [-0.8, 120, 50, 120, 5, 1500, 0.8]}
        
        # Normalisasi input
        input_scaled = scaler.transform(input_data)
        
        # Prediksi model
        prediction = model.predict(input_scaled)
        risk_class = np.argmax(prediction, axis=1)[0]
        risk_map = {0: "rendah", 1: "sedang", 2: "tinggi"}
        
        # Format response
        result = {
            "Prediksi Risiko": risk_map[risk_class],
            "Skor Risiko": prediction.tolist()  # Probabilitas untuk setiap kelas
        }
        return jsonify(result)
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
