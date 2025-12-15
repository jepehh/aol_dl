import os
import yaml

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONFIG_PATH = os.path.join(BASE_DIR, "config", "config.yaml")

with open(CONFIG_PATH, 'r') as f:
    config = yaml.safe_load(f)

DATA_RAW = os.path.join(BASE_DIR, config['data']['raw'])
DATA_PROCESSED = os.path.join(BASE_DIR, config['data']['processed'])

MODELS_DIR = os.path.join(BASE_DIR, config['models']['pretrained_dir'])
SHAPE_PREDICTOR = os.path.join(BASE_DIR, config['models']['shape_predictor'])
FACE_REC_MODEL = os.path.join(BASE_DIR, config['models']['face_recognition'])

OUTPUTS_DIR = os.path.join(BASE_DIR, config['outputs']['base_dir'])
OUTPUTS_MODELS_DIR = os.path.join(BASE_DIR, config['outputs']['models_dir'])
PLOTS_DIR = os.path.join(BASE_DIR, config['outputs']['plots_dir'])
ATTENDANCE_DIR = os.path.join(BASE_DIR, config['outputs']['attendance_dir'])

NEURAL_NET_MODEL = os.path.join(BASE_DIR, config['outputs']['neural_net_model'])
LABEL_ENCODER = os.path.join(BASE_DIR, config['outputs']['label_encoder'])

CONFIDENCE_THRESHOLD = config['training']['confidence_threshold']
TEST_SIZE = config['training']['test_size']
RANDOM_STATE = config['training']['random_state']
EPOCHS = config['training']['epochs']
BATCH_SIZE = config['training']['batch_size']