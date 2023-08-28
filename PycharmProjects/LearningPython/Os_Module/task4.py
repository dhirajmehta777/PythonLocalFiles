import glob
import subprocess

def get_file_paths(root_dir,exclude_folder=None):
    file_paths=[]
    matches=["/**/SCons","/**/*.py"]
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
    paths = get_file_paths(directory_path,exclude_folder=folder_to_exclude)
    need_to_update = check_file_status(paths)
    prCyan("\n============================")
    print("Python files need to update: " + str(len(need_to_update)))
    for item in need_to_update:
        prCyan("\n============================")
        print(item["path"])
        prRed(item["output"])
main()
