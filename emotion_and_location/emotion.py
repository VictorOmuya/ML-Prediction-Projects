from PIL import Image
from matplotlib import pyplot as plt
import numpy as np
import face_recognition
import keras
from keras.models import load_model
import cv2

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Flatten
from tensorflow.keras.layers import Conv2D
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.layers import MaxPooling2D
from tensorflow.keras.preprocessing.image import ImageDataGenerator

from PyQt5.QtWidgets import QApplication,QWidget, QVBoxLayout, QPushButton, QFileDialog , QLabel, QTextEdit, QMessageBox


def messages(title, message):
    mess = QMessageBox()
    mess.setWindowTitle(title)
    mess.setText(message)
    mess.setStandardButtons(QMessageBox.Ok)
    mess.exec_()
    
    
def detection(imgpath):
      
    image = face_recognition.load_image_file(imgpath)
    face_locate = face_recognition.face_locations(image)
        
    if len(face_locate) > 0:
            
        model = Sequential()

        model.add(Conv2D(32, kernel_size=(3, 3), activation='relu', input_shape=(48, 48, 1)))
        model.add(Conv2D(64, kernel_size=(3, 3), activation='relu'))
        model.add(MaxPooling2D(pool_size=(2, 2)))
        model.add(Dropout(0.25))
            
        model.add(Conv2D(128, kernel_size=(3, 3), activation='relu'))
        model.add(MaxPooling2D(pool_size=(2, 2)))
        model.add(Conv2D(128, kernel_size=(3, 3), activation='relu'))
        model.add(MaxPooling2D(pool_size=(2, 2)))
        model.add(Dropout(0.25))
            
        model.add(Flatten())
        model.add(Dense(1024, activation='relu'))
        model.add(Dropout(0.5))
        model.add(Dense(7, activation='softmax'))
            
        
            #emotion_dict= {'Angry': 5, 'Sad': 0, 'Neutral': 4, 'Disgust': 1, 'Surprise': 6, 'Anxious': 3, 'Happy': 2}
            #model = load_model("emotion_detector_models/model_v6_23.hdf5")
            
        emotion_dict = {"Angry" : 0 , "Disgusted": 1 , "Fearful": 2, "Happy": 3, "Neutral":4, "Sad":5, "Surprised":6}
        model.load_weights("emotion_detector_models/model.h5")
            
        face_image  = cv2.imread(imgpath)
            
        face_image = cv2.resize(face_image, (48,48))
        face_image = cv2.cvtColor(face_image, cv2.COLOR_BGR2GRAY)
        face_image = np.reshape(face_image, [1, face_image.shape[0], face_image.shape[1], 1])
        
        predicted_class = np.argmax(model.predict(face_image))
        
        label_map = dict((v,k) for k,v in emotion_dict.items()) 
        
        predicted_label = label_map[predicted_class]
        messages("Result", "This person's emotion is " + "'"+ predicted_label+ "'")
        
    elif len(face_locate) == 0:
        messages("Result", "No human face detected,\nupload another image please")
        
