import numpy as np
import cv2
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense, Dropout, Conv2D, MaxPooling2D, Flatten
from keras.callbacks import EarlyStopping
from keras.utils import to_categorical
from tensorflow import keras



class ModelMnist(object):

    def __init__(self):
        # loading model
        super().__init__()
        self.model = keras.models.load_model(PATH)


    def predict(self, image):
        input = cv2.resize(image, (28 , 28)).reshape((28 , 28,1)).astype('float32') / 255
        return self.model.predict_classes(np.array([input]))