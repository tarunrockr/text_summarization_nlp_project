import os
import logging
from datetime import datetime, date


today_date = datetime.today().strftime("%d_%m_%Y")
log_dir = 'logs'
log_folder_path =  os.path.join(os.getcwd(), log_dir, today_date)
# Creating folders if it not exists
os.makedirs(log_folder_path, exist_ok=True)

date_time = datetime.now().strftime("%d_%m_%Y")
file_name = 'log_'+date_time+'.log'
file_name = os.path.join(log_folder_path, file_name)
print("Filename: ",file_name)

logging.basicConfig(
    filename = file_name,
    level    = logging.INFO,
    format   = "[%(asctime)s] %(lineno)d %(name)s  - %(levelname)s:%(message)s"
)

# print("Today date: ", today_date)
# print("getcwd", os.path.join(os.getcwd(), log_dir, today_date) )

