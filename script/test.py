import os
import shutil
folder_path = r"C:\Users\Ezekiel's Computer\OneDrive\Documents"


for filename in os.listdir(folder_path):
    if os.path.isdir(os.path.join(folder_path, filename)):
        continue
    ext = filename.split('.')[-1].lower()
    ext_folder=os.path.join(folder_path,ext)
    if not os.path.exists(ext_folder):
        os.makedirs(ext_folder)
        shutil.move(os.path.join(folder_path, filename),os.path.join(ext_folder,filename))
print("Done")