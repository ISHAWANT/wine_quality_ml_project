import os,sys
import logging 

logging_str_format = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]" 

log_dir = 'wine_logs' 

logs_file_path = os.path.join(log_dir,"running_log.log") 
os.makedirs(log_dir,exist_ok=True) 

logging.basicConfig(
    level=logging.INFO,
    format= logging_str_format,
    
    handlers=[
        logging.FileHandler(logs_file_path),
        logging.StreamHandler(sys.stdout)
    ]

)

logger = logging.getLogger("ML Project Logger")