from flask import Flask, render_template, request, redirect, url_for, jsonify
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import pymysql
import os

app = Flask(__name__)
i=1
# Load the saved model
model = load_model(r"D:\Dataset\Brain tumer\App\Brain_Tumer.h5")

# MySQL configurations
db = pymysql.connect(host='localhost',
                     user='root',
                     password='gold',
                     database='patient_list')
cursor = db.cursor()

@app.route('/')
def index():
    return render_template('index.html')

def preprocess_image(image_path):
    img = image.load_img(image_path, target_size=(224, 224))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    return img_array

def predict_image(image_path):
    img_array = preprocess_image(image_path)
    predictions = model.predict(img_array)
    predicted_class_index = np.argmax(predictions)
    class_labels = ['glioma', 'meningioma', 'notumer', 'pituitary']
    predicted_class = class_labels[predicted_class_index]
    return predicted_class

@app.route('/predict', methods=['POST'])
def predict():
    global i  # Declare i as global

    if 'image' not in request.files:
        return jsonify({'error': 'No file uploaded'}), 400

    image_file = request.files['image']
    name = request.form['name']
    if image_file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    if image_file:
        # Create directory if it doesn't exist
        Img_folder = os.path.join(app.root_path, 'Img')
        if not os.path.exists(Img_folder):
            os.makedirs(Img_folder)

        image_path = os.path.join(Img_folder, f"{name}.jpg")
        image_file.save(image_path)
        predicted_disease = predict_image(image_path)

        # Store data in database
        cursor.execute("INSERT INTO patient (Sno, Name, Disease) VALUES (%s, %s, %s)", (str(i), name, predicted_disease))
        i += 1
        db.commit()

        return redirect(url_for('index'))


@app.route('/delete/<int:id>', methods=['POST'])
def delete(id):
    cursor.execute("DELETE FROM patient WHERE SNo=%s", (id,))
    db.commit()
    return redirect(url_for('view'))

@app.route('/view')
def view():
    cursor.execute("SELECT * FROM patient")
    patients = cursor.fetchall()
    return render_template('view.html', patients=patients)

if __name__ == '__main__':
    app.run(debug=True)
