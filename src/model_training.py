import os
import numpy as np
import tensorflow as tf
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from src.config import TEST_SIZE, RANDOM_STATE, EPOCHS, BATCH_SIZE, NEURAL_NET_MODEL, LABEL_ENCODER, OUTPUTS_MODELS_DIR
from src.feature_extraction import extract_embeddings

def train_model():
    os.makedirs(OUTPUTS_MODELS_DIR, exist_ok=True)
    
    embeddings, labels = extract_embeddings()
    
    label_encoder = LabelEncoder()
    labels_encoded = label_encoder.fit_transform(labels)
    
    np.save(LABEL_ENCODER, label_encoder.classes_)
    
    X_train, X_test, y_train, y_test = train_test_split(
        embeddings, labels_encoded, test_size=TEST_SIZE, random_state=RANDOM_STATE, stratify=labels_encoded
    )
    
    num_classes = len(np.unique(y_train))
    y_train_onehot = tf.keras.utils.to_categorical(y_train, num_classes)
    y_test_onehot = tf.keras.utils.to_categorical(y_test, num_classes)
    
    model = tf.keras.Sequential([
        tf.keras.layers.InputLayer(input_shape=(embeddings.shape[1],)),
        tf.keras.layers.Dense(128, activation='relu'),
        tf.keras.layers.Dropout(0.5),
        tf.keras.layers.Dense(num_classes, activation='softmax')
    ])
    
    model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
    
    history = model.fit(
        X_train, y_train_onehot,
        validation_data=(X_test, y_test_onehot),
        epochs=EPOCHS,
        batch_size=BATCH_SIZE
    )
    
    model.save(NEURAL_NET_MODEL)
    print(f"Model saved to {NEURAL_NET_MODEL}")
    
    return history, X_test, y_test, label_encoder