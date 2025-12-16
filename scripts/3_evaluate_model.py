import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, classification_report, ConfusionMatrixDisplay
from src.feature_extraction import extract_embeddings
from src.config import TEST_SIZE, RANDOM_STATE, LABEL_ENCODER, NEURAL_NET_MODEL, PLOTS_DIR

if __name__ == "__main__":
    print("Loading model and data...")
    
    model = tf.keras.models.load_model(NEURAL_NET_MODEL)
    label_encoder_classes = np.load(LABEL_ENCODER, allow_pickle=True)
    label_encoder = LabelEncoder()
    label_encoder.classes_ = label_encoder_classes
    
    embeddings, labels = extract_embeddings()
    labels_encoded = label_encoder.transform(labels)
    
    _, X_test, _, y_test = train_test_split(
        embeddings, labels_encoded, test_size=TEST_SIZE, random_state=RANDOM_STATE, stratify=labels_encoded
    )
    
    print("Evaluating model on test set...")
    y_test_pred = np.argmax(model.predict(X_test), axis=1)
    
    print("\nClassification Report:\n")
    print(classification_report(y_test, y_test_pred, target_names=label_encoder.classes_))
    
    os.makedirs(PLOTS_DIR, exist_ok=True)
    cm = confusion_matrix(y_test, y_test_pred)
    plt.figure(figsize=(10, 8))
    disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=label_encoder.classes_)
    disp.plot(cmap=plt.cm.Blues, ax=plt.gca(), xticks_rotation="vertical")
    plt.title("Confusion Matrix - Re-evaluation")
    plt.savefig(os.path.join(PLOTS_DIR, "confusion_matrix_reeval.jpg"))
    plt.close()
    
    print(f"\nConfusion matrix saved to {PLOTS_DIR}/confusion_matrix_reeval.jpg")
    print("\nNote: Accuracy/Loss plots require training history.")
    print("To get those plots, run: python scripts/2_train_model.py")
    print("Evaluation complete!")