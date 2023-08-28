import subprocess
import shutil
import os
import datetime
import glob

def get_file_paths(root_dir,exclude_folder=None):
    file_paths=[]
    matches=["/**/SCons","/**/*.py"]
    for match in matches:
        files=glob.glob(f"{root_dir}"+match,recursive=True)
        exclude= [path for path in files if not any(folder in path for folder in exclude_folder)]
        file_paths.extend(exclude)
    return file_paths

def create_backup(Path, backup_folder):
    if not os.path.exists(backup_folder):
        os.makedirs(backup_folder)
    filename, file_extension = os.path.splitext(os.path.basename(Path))
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    backup_filename = f"backup_{filename}_{timestamp}{file_extension}"
    backup_path = os.path.join(backup_folder, backup_filename)
    shutil.copyfile(Path, backup_path)
    return backup_path

def main():
    directory_path = '/home/excellarate/example/'
    folder_to_exclude=['folder2']
    backup_folder='/home/excellarate/Documents/'
    paths = get_file_paths(directory_path,exclude_folder=folder_to_exclude)
    for path in paths:
        backup_path = create_backup(path,backup_folder)
        print(f"Backup created: {backup_path}")
        subprocess.run(['2to3','-w',path])
        print(f"Converted {path} to Python 3.")

main()