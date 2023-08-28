import glob
import subprocess

directory_path='/home/excellarate/example/'
def get_file_paths(root_dir):
    file_paths=[]
    scons_files=glob.glob(f"{root_dir}/**/SCons",recursive=True)
    py_files=glob.glob(f"{root_dir}/**/*.py",recursive=True)
    file_paths.extend(scons_files)
    file_paths.extend(py_files)
    return file_paths

paths=get_file_paths(directory_path)
for path in paths:
    print(path)
for path in paths:
    p1=subprocess.run(['2to3',path],stdout=subprocess.PIPE,text=True)
    #print(p1.stdout)
    if len(p1.stdout)==0:
        print("This file doesn't required any modifications:",path)
    else:
        print("This file needs modification:",path)