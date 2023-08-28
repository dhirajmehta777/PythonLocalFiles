import subprocess
import shutil
import os
import datetime
import glob

def create_backup(file_path, backup_folder):
    if not os.path.exists(backup_folder):
        os.makedirs(backup_folder)

        # Get the filename and extension
    filename, file_extension = os.path.splitext(os.path.basename(file_path))

    # Create a backup filename with timestamp
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    backup_filename = f"backup_{filename}_{timestamp}{file_extension}"

    # Create the backup path
    backup_path = os.path.join(backup_folder, backup_filename)

    # Copy the original file to the backup location
    shutil.copyfile(file_path, backup_path)

    return backup_path

def convert_python2_to_python3(script_path):
    subprocess.call(['2to3', '-w', script_path])

# Replace 'your_directory_path' with the actual path to the directory containing your Python 2 scripts
directory_path = 'your_directory_path'
backup_folder = 'backup'  # Replace with the path where you want to store backups
script_pattern = '*.py'   # Replace with the pattern for your Python 2 scripts

# Get a list of Python script paths using glob
script_paths = glob.glob(os.path.join(directory_path, script_pattern))

for script_path in script_paths:
    try:
        backup_path = create_backup(script_path, backup_folder)
        print(f"Backup created: {backup_path}")

        convert_python2_to_python3(script_path)
        print(f"Converted {script_path} to Python 3.")
    except Exception as e:
        print(f"An error occurred while processing {script_path}:", e)