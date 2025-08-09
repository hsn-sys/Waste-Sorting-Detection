import cv2
import numpy as np
import serial
import time
from tensorflow.keras.models import load_model

# Load your trained multi-class model
model = load_model('waste_model2.h5')

# Arduino connection
arduino = serial.Serial('COM4', 9600)  # Change to your port
time.sleep(2)

# Define your classes (must match training order!)
#class_names = ['cardboard', 'glass', 'metal', 'paper', 'plastic', 'trash']
recyclable_classes = {'recycle'}
class_names = ['recycle','nonrecycle']

# Open webcam
cap = cv2.VideoCapture(1)

print("Press 's' to capture and classify. Press 'q' to quit.")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    cv2.imshow("Waste Detector", frame)
    key = cv2.waitKey(1) & 0xFF

    if key == ord('s'):
        # Preprocess for model
        img = cv2.resize(frame, (224, 224))  # Change if your model input is different
        img = img.astype('float32') / 255.0
        img = np.expand_dims(img, axis=0)

        # Predict class
        preds = model.predict(img)[0][0]  # e.g., [0.1, 0.2, ..., 0.3]
        class_index = np.argmax(preds)
        predicted_class = class_names[class_index]
        confidence = preds[class_index]

        print(f"Predicted: {predicted_class} ({confidence:.2f})")

        # Send to Arduino: 'R' for recyclable, 'N' for trash
        if predicted_class in recyclable_classes:
            arduino.write(b'R')
        else:
            arduino.write(b'N')

        time.sleep(1)

    elif key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
