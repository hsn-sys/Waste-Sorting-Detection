import cv2
import tensorflow as tf
import numpy as np

img = cv2.imread("biological426.jpg")
img = cv2.resize(img,(256,256))
img_pred = tf.expand_dims(img,axis = 0)
#class_name = ['cardboard', 'glass', 'metal', 'paper', 'plastic', 'trash']
class_name = ['nonrecycle','recycle']


model = tf.keras.models.load_model('waste_model1.h5')
predict_label = class_name[np.argmax(model.predict(img_pred))]

print(f"IMG ORIGINAL {img.shape}")
print(f"IMG PRED {img_pred.shape}")
print(predict_label)


cv2.putText(img,f"{predict_label}",(25,35),1,cv2.FONT_HERSHEY_COMPLEX,(0,255,0),2)

cv2.imshow("CLASS",img)
cv2.waitKey()



