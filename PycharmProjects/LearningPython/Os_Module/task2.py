import os
directory_path='/home/excellarate/example/'
def get_file_paths(root_dir):
    file_paths=[]
    for root,_,files in os.walk(root_dir):
        for file in files:
            file_path=os.path.join(root,file)
            if file.endswith('.py') or file.startswith('SCons'):
                file_paths.append(file_path)
        return file_paths


file_paths=get_file_paths(directory_path)
for path in file_paths:
    print(path)