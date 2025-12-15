import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from src.data_preprocessing import preprocess_dataset

if __name__ == "__main__":
    print("Starting dataset preprocessing...")
    preprocess_dataset()
    print("Preprocessing complete!")