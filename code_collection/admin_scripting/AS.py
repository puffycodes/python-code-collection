
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

# open the log file for reading
with open(log_file, 'r') as log_fd:

    # process each line in the log file
    for line in log_fd:
        #print(line.strip())

        # extract the filename and owner from the line
        filename, owner = line.strip().split(':')
        #print(filename, owner)

        # check if the file exists
        current_file = os.path.join(resource_folder, filename)
        if os.path.isfile(current_file):
            print(current_file)

            # extract the name and extension of the file
            name, ext = os.path.splitext(filename)
            # construct the new name for the file
            new_name = f'{name}_{owner}{ext}'
            print(name, ext, '->', new_name)

            # rename the file
            move_to_filename = os.path.join(resource_folder, new_name)
            os.rename(current_file, move_to_filename)

            # log the action of renaming the file
            logger.info(f'renamed: {current_file} -> {move_to_filename}')
