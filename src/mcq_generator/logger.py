#this file is used to store the log of each and every information 

import logging
import os 
from datetime import datetime

log_file_name = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

log_folder_path = os.path.join(os.getcwd(),"logs")        #getcwd is -> current working directory 

os.makedirs(log_folder_path, exist_ok=True)

log_file_path = os.path.join(log_folder_path, log_file_name)


# above INFO level it is going to capture all the information 
logging.basicConfig(level = logging.INFO,
        filename=log_file_path,
        format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s"
)
