import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from src.model_training import train_model
from src.model_evaluation import evaluate_model
import tensorflow as tf

if __name__ == "__main__":
    print("Starting model training...")
    history, X_test, y_test, label_encoder = train_model()
    print("Training complete!")
    
    print("\nEvaluating model...")
    model = tf.keras.models.load_model("models/neural_net_model.h5")
    evaluate_model(history, model, X_test, y_test, label_encoder)
    print("Evaluation complete!")