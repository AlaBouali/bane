import os
import shutil

# Define the directory where you want to start the search
start_directory = 'html'

# Define the old and new file extensions
old_extension = '.html'
new_extension = '.md'

def delete_pycache_folders(root_directory):
    for dirpath, dirnames, filenames in os.walk(root_directory):
        for dirname in dirnames:
            if dirname == "__pycache__":
                pycache_path = os.path.join(dirpath, dirname)
                print(f"Deleting {pycache_path}")
                shutil.rmtree(pycache_path)

delete_pycache_folders('bane')

# Walk through the directory and its subdirectories
for root, _, files in os.walk(start_directory):
    for file in files:
        if file.endswith(old_extension):
            old_file_path = os.path.join(root, file)
            new_file_path = os.path.join(root, file.replace(old_extension, new_extension))
            
            # Rename the file
            shutil.move(old_file_path, new_file_path)
            print(f'Renamed: {old_file_path} -> {new_file_path}')
