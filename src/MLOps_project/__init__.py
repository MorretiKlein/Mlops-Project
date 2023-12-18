import os
import sys
import logging

logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"

log_dir = "logs"
log_filepath = os.path.join(log_dir,"running_logs.log")
os.makedirs(log_dir, exist_ok=True)


logging.basicConfig(
    level= logging.INFO,
    format= logging_str,
    handlers=[
        logging.FileHandler(log_filepath), # Gửi log message vào file "running_logs.log".
        logging.StreamHandler(sys.stdout) # In log message trực tiếp lên màn hình console.
    ]
)

logger = logging.getLogger("MLOPs_projectLogger")
