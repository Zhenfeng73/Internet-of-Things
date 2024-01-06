from keras.models import load_model  # TensorFlow is required for Keras to work
import cv2  # Install opencv-python
import numpy as np

# Load the model
model = load_model("keras_Model.h5", compile=False)

# CAMERA can be 0 or 1 based on default camera of your computer
camera = cv2.VideoCapture('http://192.168.1.13:81/stream')

labels = ["Right", "Left", "Ahead", "Stop"]

def image_detector():
    # Grab the webcamera's image.
    ret, image = camera.read()

    # Resize the raw image into (224-height,224-width) pixels
    image = cv2.resize(image, (224, 224), interpolation=cv2.INTER_AREA)

    # Show the image in a window
    cv2.imshow("Webcam Image", image)

    # Make the image a numpy array and reshape it to the models input shape.
    image = np.asarray(image, dtype=np.float32).reshape(1, 224, 224, 3)

    # Normalize the image array
    image = (image / 127.5) - 1

    probabilities=model.predict(image)

    print(labels[np.argmax(probabilities)])
    return labels[np.argmax(probabilities)]






