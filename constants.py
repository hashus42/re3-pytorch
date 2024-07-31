import os.path

# Network Constants
CROP_SIZE = 227
CROP_PAD = 2
MAX_TRACK_LENGTH = 32
LSTM_SIZE = 512

LOG_DIR = os.path.join(os.path.dirname(__file__), 'logs')
GPU_ID = '0'

# Drawing constants
OUTPUT_WIDTH = 800
OUTPUT_HEIGHT = 600

SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080

PADDING = 2
