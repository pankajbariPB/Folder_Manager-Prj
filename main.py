"""
Project Title: Folder Manager
==================================================================================================

Author:
Pankaj Bari

Version:
1

Description:
Folder Manager is a simple yet powerful Python script that helps you organize your files effortlessly.
 It automatically scans a target directory and sorts all files into subfolders based on their file extensions 
 (e.g., .pdf files go into a pdf folder). This keeps your folders neat, tidy,
and easy to navigate—perfect for managing downloads, documents, or any cluttered directory.
✨ Features
1. Automatic File Organization: Sorts files into subfolders by extension.
2. No Setup Required: Just specify your folder path and run the script.
3. Handles All File Types: Supports files with or without extensions.
4. Safe & Efficient: Skips directories and creates folders only as needed.
5. Cross-Platform: Works on Windows, macOS, and Linux.

🚀 How It Works
Specify the folder you want to organize.

Run the script.

All files are moved into subfolders named after their extensions (e.g., jpg, pdf, no_extension).

"""
# C:\Users\panka\Downloads\test.pdf
# C:\Users\panka\Downloads\pdf\text.pdf
import os,shutil

folder_path= r"C:\Users\panka\Downloads" 

try:
    for item in os.listdir(folder_path):
        item_path=os.path.join(folder_path,item)
        if os.path.isfile(item_path):
            _ ,extension=os.path.splitext(item)
            ext_folder=os.path.join(folder_path,extension[1:].lower() or "no_extension")

            os.makedirs(ext_folder,exist_ok=True)
            shutil.move(item_path,os.path.join(ext_folder,item))

except Exception as ex:
    print(ex.__name__)     

else :
    print(f"{os.path.basename(os.path.normpath(folder_path))} {'managed sucessful'}")