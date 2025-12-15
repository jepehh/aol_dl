# Dataset

This folder contains the face recognition dataset used for training the attendance system.

## Structure

```
data/
├── raw/                    # Original images (23 people × ~10 images each)
│   ├── Cha Eun Woo/
│   ├── Cho Yi-hyun/
│   ├── Jason Patrick/
│   └── ...
└── preprocessed/              # Preprocessed face crops (auto-generated)
    ├── Cha Eun Woo/
    ├── Cho Yi-hyun/
    ├── Jason Patrick/
    └── ...
```

## Dataset Details

- **Total People:** 23
- **Images per person:** ~10
- **Total images:** ~230
- **Image format:** JPG
- **Preprocessing:** Face detection + cropping using dlib

## Sample Images

### Format
Each person's folder contains multiple images captured from different angles and lighting conditions:

```
Jason Patrick/
├── img_001.jpg
├── img_002.jpg
├── img_003.jpg
└── ...
```

### Example Images

#### Jason Patrick
![Sample 1](raw/Jason%20Patrick/jp_1.jpg)
![Sample 2](raw/Jason%20Patrick/jp_2.jpg)

*Note: Replace with actual image filenames from your dataset ex. C:\Users\jason\Documents\deep_learning_aol\data\raw\Jason Patrick\jp_1.jpg*

#### Cha Eun Woo
![Sample 1](raw/Cha%20Eun%20Woo/cew_1.jpg)
![Sample 2](raw/Cha%20Eun%20Woo/cew_2.jpg)

*Note: Replace with actual image filenames from your dataset ex. C:\Users\jason\Documents\deep_learning_aol\data\raw\Cha Eun Woo\cew_1.jpg*

## Data Collection

For this project, the images were collected from:
- Personal photos (Jason Patrick)
- Public celebrity datasets (22 Korean celebrities/idols)

## Preprocessing Pipeline

1. **Face Detection:** Using dlib's HOG-based detector
2. **Face Cropping:** Extract face region with padding
3. **Face Alignment:** Using 68 facial landmarks
4. **Output:** Cropped face images saved to `processed/` folder

Run preprocessing:
```bash
python scripts/1_preprocess_dataset.py
```

## Usage in Training

The processed images are used to:
1. Extract 128D face embeddings using dlib's ResNet model
2. Train a neural network classifier to recognize the 23 individuals
3. Generate the final model for the attendance system

## Adding New People

To add a new person to the dataset:

1. Create a new folder in `data/raw/` with the person's name
2. Add 10-15 images of the person (different angles, lighting)
3. Run preprocessing: `python scripts/1_preprocess_dataset.py`
4. Retrain the model: `python scripts/2_train_model.py`

## Data Privacy

⚠️ This dataset contains images of real people. Please ensure:
- Proper consent has been obtained for personal images
- Celebrity images are used only for educational/research purposes
- The dataset is not shared publicly without permission