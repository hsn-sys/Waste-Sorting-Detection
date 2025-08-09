import cv2
import tensorflow as tf
import numpy as np


cap = cv2.VideoCapture(0)

#class_name = ['cardboard', 'glass', 'metal', 'paper', 'plastic', 'trash']
class_name = ['nonrecycle','recycle']

while True:
    _,img = cap.read()

    img_pred = cv2.resize(img,(256,256))
    img_pred = tf.expand_dims(img_pred,axis = 0)

    model = tf.keras.models.load_model('waste_model1.h5')
    predict_label = class_name[np.argmax(model.predict(img_pred))]
        
        
    cv2.putText(img,f"{predict_label}",(25,35),1,cv2.FONT_HERSHEY_COMPLEX,(0,255,0),2)

    cv2.imshow("CLASS",img)
    k = cv2.waitKey(1) &0xff
    if k == ord('q'):
        break