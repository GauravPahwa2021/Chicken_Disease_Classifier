import os
import sys
import logging
from datetime import datetime

logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"
log_file = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
log_dir = "logs"
log_filepath = os.path.join(os.getcwd(),log_dir,log_file)
os.makedirs(log_dir,exist_ok=True)

log_file_path = os.path.join(log_filepath,log_file)

logging.basicConfig(
    
    level = logging.INFO,
    format = logging_str,

    handlers = [
        logging.FileHandler(log_filepath),
        logging.StreamHandler(sys.stdout)
    ]
)