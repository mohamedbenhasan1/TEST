# Brain Tumor Prediction Web Application

## Overview

This project is a web application developed using Flask to predict brain tumor types based on MRI images. The application utilizes a pre-trained VGG19 model for image classification. It allows users to upload MRI images, processes them through the model, and provides predictions on the type of tumor present in the image. Furthermore, the application stores patient data and their corresponding predicted tumor types in a MySQL database.

## Features

- **Brain Tumor Prediction**: Upload MRI images to predict the type of brain tumor (glioma, meningioma, pituitary, or no tumor).
- **Patient Data Storage**: Save patient names and predicted tumor types in a MySQL database.
- **User-Friendly Interface**: A simple and intuitive web interface for easy interaction.

## Technologies Used

- **Flask**: Web framework used for building the application.
- **TensorFlow**: Machine learning library for model loading and prediction.
- **MySQL**: Database for storing patient data.
- **HTML/CSS**: Front-end design for the web interface.

## Installation

### Prerequisites

- Python 3.x
- Git
- MySQL

### Steps

1. Clone the repository:

    ```bash
    git clone https://github.com/GoldSharon/brain-tumor-prediction.git
    ```

2. Navigate to the project directory:

    ```bash
    cd brain-tumor-prediction
    ```

3. Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Run the Flask application:

    ```bash
    python app.py
    ```

2. Open your web browser and navigate to `http://127.0.0.1:5000/`.

3. Upload an MRI image and enter the patient's name to predict the brain tumor type.

## Database Configuration

The application uses a MySQL database to store patient data. Update the MySQL connection settings in the `app.py` file before running the application:

```python
db = pymysql.connect(host='localhost',
                     user='root',
                     password='your-password',
                     database='patient_list')
