import logging
import os
from datetime import datetime

LOG_FILE= f"logs/{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log"
logs_path=os.path.join(os.getcwd(),"logs",LOG_FILE)
os.makedirs(os.path.dirname(logs_path),exist_ok=True)

LOG_FILE_PATH=os.path.join(os.getcwd(),"logs",LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO,

)  


