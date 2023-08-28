import glob
import subprocess

def list_python_and_scons_files(root_dir, exclude_folders=None):
    # if exclude_folders is None:
    #     exclude_folders=[]
    scons_files = glob.glob(f"{root_dir}/**/SCons", recursive=True)
    python_files = glob.glob(f"{root_dir}/**/*.py", recursive=True)
    python_files=[path for path in python_files if not any(folder in path for folder in exclude_folders)]
    scons_files=[path for path in scons_files if not any(folder in path for folder in exclude_folders )]
    return python_files+scons_files
directory_path='/home/excellarate/example/'
folders_to_exclude=['folder2']
file_paths=list_python_and_scons_files(directory_path,exclude_folders=folders_to_exclude)
for path in file_paths:
    print(path)