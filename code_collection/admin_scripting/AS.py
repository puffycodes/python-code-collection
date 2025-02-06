
import os
import socket
import shutil
import logging
from datetime import datetime

# define the locations of the files
top_folder = os.getcwd()
resource_folder = os.path.join(top_folder, 'resource')

log_file = os.path.join(resource_folder, 'log.txt')
admin_script_log_file = os.path.join(top_folder, 'admin_script_log.log')

print(f'top folder: {top_folder}')
print(f'log file: {log_file}')
print(f'process log file: {admin_script_log_file}')

# define the logging file location
logging.basicConfig(filename=admin_script_log_file, level=logging.INFO)
logger = logging.getLogger()

# get the current date and time and hostname
time_now = datetime.now()
current_date = time_now.strftime('%Y%m%d')
current_time = time_now.strftime('%H%M%S')
hostname = socket.gethostname()

print(f'date: {current_date}, time: {current_time}')
print(f'hostname: {hostname}')

# process the log file

with open(log_file, 'r') as log_fd:
    for line in log_fd:
        #print(line.strip())
        filename, owner = line.strip().split(':')
        #print(filename, owner)

        current_file = os.path.join(resource_folder, filename)
        if os.path.isfile(current_file):
            print(current_file)

            name, ext = os.path.splitext(filename)
            new_name = f'{name}_{owner}{ext}'
            print(name, ext, '->', new_name)

            move_to_filename = os.path.join(resource_folder, new_name)

            os.rename(current_file, move_to_filename)
            logger.info(f'renamed: {current_file} -> {move_to_filename}')
