import subprocess
import shutil
import os
import datetime
import glob

def get_file_paths(root_dir,exclude_folder=None):
    file_paths=[]
    matches=["/**/SCons*","/**/*.py"]
    for match in matches:
        files=glob.glob(f"{root_dir}"+match,recursive=True)
        exclude= [path for path in files if not any(folder in path for folder in exclude_folder)]
        file_paths.extend(exclude)
    return file_paths
def check_file_status(paths):
    updated=[]
    need_to_update=[]

    for path in paths:
        p1=subprocess.run(['2to3',path],stdout=subprocess.PIPE,text=True)
        if len(p1.stdout)==0:
            updated.append({"path":path})
        else:
            need_to_update.append({"path":path,"output":p1.stdout})
    return need_to_update

def prRed(skk): print("\033[91m {}\033[00m" .format(skk))
def prCyan(skk): print("\033[96m {}\033[00m" .format(skk))
def main():
    directory_path = '/home/excellarate/example/'
    folder_to_exclude=['folder2']
    backup_folder_path = '/home/excellarate/Documents/'
    paths = get_file_paths(directory_path,exclude_folder=folder_to_exclude)
    need_to_update = check_file_status(paths)
    prCyan("\n============================")
    print("Python files need to update: " + str(len(need_to_update)))
    for item in need_to_update:
        prCyan("\n============================")
        print(item["path"])
        prRed(item["output"])
        prCyan("\n============================")
        backup_path = create_backup(item["path"], backup_folder_path)
        print(f"Backup created: {backup_path}")
        subprocess.run(['2to3', '-w', item["path"]])
        print(f"Converted {item['path']} to Python 3.")
        prCyan("\n============================")

def create_backup(Path, backup_folder):
    filename, file_extension = os.path.splitext(os.path.basename(Path))
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    backup_filename = f"backup_{filename}_{timestamp}{file_extension}"
    backup_path = os.path.join(backup_folder, backup_filename)
    shutil.copyfile(Path, backup_path)
    return backup_path
main()



