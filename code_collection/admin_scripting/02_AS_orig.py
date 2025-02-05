import os
import shutil
import zipfile
import socket
from datetime import datetime

#Define paths
folder_path = r"C:\Admin Scripting\Practical Test"  # Folder where files are located
log_file_path = r"C:\Admin Scripting\Practical Test\pythun\log.txt"  # Log file with filename-owner mappings
base_folder_path = r"C:\Admin Scripting\Practical Test"  # Where you want the new folder and zip to be created

#Create a dictionary to store the filename-owner mappings
file_owners = {}

#Read the log file and populate the dictionary
with open(log_file_path, "r") as log_file:
    for line in log_file:
        if line.strip():  # Avoid processing empty lines
            filename, owner = line.strip().split(":")
            file_owners[filename] = owner

#Get current date, time, and hostname
current_date = datetime.now().strftime("%Y%m%d")
current_time = datetime.now().strftime("%H%M%S")
hostname = socket.gethostname()

#Create the new folder name based on current date and hostname
new_folder_name = f"{current_date}_{hostname}"

#Define the full path for the new folder
new_folder_path = os.path.join(base_folder_path, new_folder_name)

#Create the new folder if it doesn't exist
os.makedirs(new_folder_path, exist_ok=True)
print(f"New folder created at: {new_folder_path}")

#Loop through the files in the folder, rename them, then move to the new folder
for filename in os.listdir(folder_path):
    file_path = os.path.join(folder_path, filename)

$unknown yet, to make it move the 'renamed files' into a new one that zip it, hasnt been figured out yet
    def check_and_move(file, list_of_patterns, destination):
        for pattern in list_of_patterns:
            if file.startswith(pattern):
                shutil.move(file, destination)

    #Only process files (not directories)
    if os.path.isfile(file_path):
        #Check if the filename exists in the mapping
        if filename in file_owners:
            owner = file_owners[filename]
            #Split the filename and extension
            name, ext = os.path.splitext(filename)
            # Create the new filename with the owner appended
            new_filename = f"{name}_{owner}{ext}"

            #Create the full path for the new filename
            new_file_path = os.path.join(folder_path, new_filename)

            #Rename the file
            os.rename(file_path, new_file_path)
            print(f"Renamed: {filename} -> {new_filename}")

            #Move the renamed file to the new folder
            shutil.move(new_file_path, new_folder_path)
            print(f"Moved: {new_filename} to {new_folder_path}")

#Define the zip file name
zip_filename = f"{current_date}{current_time}{hostname}.zip"
zip_file_path = os.path.join(base_folder_path, zip_filename)

#Create a zip file and add all files from the new folder
with zipfile.ZipFile(zip_file_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
    for foldername, subfolders, filenames in os.walk(new_folder_path):
        for filename in filenames:
            file_path = os.path.join(foldername, filename)
            zipf.write(file_path, os.path.relpath(file_path, new_folder_path))
            print(f"Added to zip: {file_path}")

#Optional: Clean up the new folder after zipping, if desired
#shutil.rmtree(new_folder_path)

print(f"All files are renamed, moved, and zipped into: {zip_file_path}")
