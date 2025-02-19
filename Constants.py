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
IMGBB_API_KEY = "bc8ef0e80f038925f3dadfbb769b87f7"

# Expiration time for uploaded images (in seconds)
IMGBB_EXPIRATION_TIME = 1800

# Azure OCR stuff
AZURE_OCR_SUBSCRIPTION_KEY = "fcb75213fafe4affa21a2ea34bf172a0"
AZURE_OCR_ENDPOINT = "https://tfgocr.cognitiveservices.azure.com/"

# Folders
INPUT_FOLDER = r"\User Files\Input Images"
OUTPUT_FOLDER = r"\User Files\Output Files"

# Suffix to indicate variables
VAR_SUFFIX = "_var"

# Suffix to indicate functions
FUNC_SUFFIX = '_func'

# Symbols used to mark pseudocode
DEFAULT = "DEFAULT"
TAB = "<TAB>"
VARIABLE_DECLARATIONS = "<VAR_DECLARATION>"
PRINT = "<PRINT>"
SCAN = "<SCAN>"
FUNCTION = "<FUNC>"
MAIN_FUNCTION = "<BASE_FUNC>"
CONDITIONAL_START = "<CONDITIONAL>"
CONDITIONAL_END = "</CONDITIONAL>"
CONDITION_BRANCH_START = "<CONDITION>"
CONDITION_BRANCH_END = "</CONDITION>"
END_CODE = "<END>"
INTEGER = "<INT>"
STRING = "<STRING>"
