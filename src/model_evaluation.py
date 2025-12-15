import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix, classification_report, ConfusionMatrixDisplay
from src.config import PLOTS_DIR
import os

def evaluate_model(history, model, X_test, y_test, label_encoder):
    os.makedirs(PLOTS_DIR, exist_ok=True)
    
    plt.figure(figsize=(10, 6))
    plt.plot(history.history['accuracy'], label='Train Accuracy', color='blue')
    plt.plot(history.history['val_accuracy'], label='Validation Accuracy', color='orange')
    plt.title("Training and Validation Accuracy")
    plt.xlabel("Epochs")
    plt.ylabel("Accuracy")
    plt.legend()
    plt.savefig(os.path.join(PLOTS_DIR, "accuracy_metrics.jpg"))
    plt.close()
    
    plt.figure(figsize=(10, 6))
    plt.plot(history.history['loss'], label='Train Loss', color='blue')
    plt.plot(history.history['val_loss'], label='Validation Loss', color='orange')
    plt.title("Training and Validation Loss")
    plt.xlabel("Epochs")
    plt.ylabel("Loss")
    plt.legend()
    plt.savefig(os.path.join(PLOTS_DIR, "loss_metrics.jpg"))
    plt.close()
    
    y_test_pred = np.argmax(model.predict(X_test), axis=1)
    
    print("\nClassification Report:\n")
    print(classification_report(y_test, y_test_pred, target_names=label_encoder.classes_))
    
    cm = confusion_matrix(y_test, y_test_pred)
    plt.figure(figsize=(10, 8))
    disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=label_encoder.classes_)
    disp.plot(cmap=plt.cm.Blues, ax=plt.gca(), xticks_rotation="vertical")
    plt.title("Confusion Matrix")
    plt.savefig(os.path.join(PLOTS_DIR, "confusion_matrix.jpg"))
    plt.close()
    
    print(f"Evaluation complete. Plots saved to {PLOTS_DIR}")