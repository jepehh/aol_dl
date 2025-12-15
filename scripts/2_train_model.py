import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from src.model_training import train_model
from src.model_evaluation import evaluate_model
import tensorflow as tf
from src.config import NEURAL_NET_MODEL

if __name__ == "__main__":
    print("Starting model training...")
    history, X_test, y_test, label_encoder = train_model()
    print("Training complete!")
    
    print("\nEvaluating model...")
    model = tf.keras.models.load_model(NEURAL_NET_MODEL)
    evaluate_model(history, model, X_test, y_test, label_encoder)
    print("Evaluation complete!")