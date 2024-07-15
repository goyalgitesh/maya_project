import tensorflow as tf
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Input, Conv2D, MaxPooling2D, Flatten, Dense, Dropout

class FacialRecognitionModel:
    def __init__(self):
        self.model = self._build_model()
        self.model.load_weights('path_to_your_weights.h5')

    def _build_model(self):
        input_shape = (128, 128, 3)
        inputs = Input(shape=input_shape)
        
        x = Conv2D(32, (3, 3), activation='relu')(inputs)
        x = MaxPooling2D((2, 2))(x)
        x = Conv2D(64, (3, 3), activation='relu')(x)
        x = MaxPooling2D((2, 2))(x)
        x = Conv2D(64, (3, 3), activation='relu')(x)
        
        x = Flatten()(x)
        x = Dense(64, activation='relu')(x)
        x = Dropout(0.5)(x)
        outputs = Dense(128, activation='softmax')(x)
        
        model = Model(inputs=inputs, outputs=outputs)
        model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
        return model

    async def predict(self, face_image):
        prediction = self.model.predict(face_image)
        return tf.argmax(prediction, axis=1).numpy()[0]