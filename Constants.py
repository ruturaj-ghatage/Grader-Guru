# Path to block detection model
block_detection_model = './best(L).pt'

# If any detection have less than this value, it will not be considered
CONFIDENCE_THRESHOLD = 0.4

# Value used to get double detections
DUPLICATE_THRESHOLD = 20

# Value used to limit arrow do-while loop
DO_WHILE_LOOPS = 10

# Value used to set block ID prefix
BLOCK_PREFIX = "Block"

# IMGBB URL
IMGBB_URL = "https://api.imgbb.com/1/upload"

# API key for upload images
IMGBB_API_KEY = "1f8cd84903460565f6153993e1247b14"

# Expiration time for uploaded images (in seconds)
IMGBB_EXPIRATION_TIME = 1800

# Azure OCR stuff


# Folders
INPUT_FOLDER = r"\User_Files\InputImages"
OUTPUT_FOLDER = r"\User_Files\OutputFiles"

# Suffix to indicate variables
VAR_SUFFIX = "_var"

# Suffix to indicate functions
FUNC_SUFFIX = '_func'


