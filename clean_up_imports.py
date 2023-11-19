import os,re
import shutil
from bs4 import BeautifulSoup

#os.system('pdoc --html .')

# Define the directory where you want to start the search
#start_directory = 'html'

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

def remove_pyc_files(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.pyc'):
                file_path = os.path.join(root, file)
                os.remove(file_path)
                #print("Removed {}".format(file_path))

# Specify the directory from which you want to remove .pyc files
directory_to_search = 'bane'

remove_pyc_files(directory_to_search)

delete_pycache_folders('bane')
"""
def rename_and_edit_files(directory):
    # Define the old and new file extensions
    old_extension = '.html'
    new_extension = '.md'
    
    # Walk through the directory and its subdirectories
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(old_extension):
                old_file_path = os.path.join(root, file)
                new_file_path = os.path.join(root, file.replace(old_extension, new_extension))
                
                # Rename the file
                shutil.move(old_file_path, new_file_path)
                print(f'Renamed: {old_file_path} -> {new_file_path}')
                
                # Edit the file contents
                with open(new_file_path, 'r') as f:
                    content = f.read()
                
                # Remove everything before the <body> tag (case-insensitive)
                body_start = content.lower().find('<body>')
                if body_start != -1:
                    content = content[body_start:]
                
                # Replace .html with .md in all <a> tags' href attributes
                content = re.sub(r'href="([^"]*).html"', r'href="\1.md"', content)
                
                # Write the edited content back to the file
                with open(new_file_path, 'w') as f:
                    f.write(content)
                print(f'Edited: {new_file_path}')

rename_and_edit_files('html')
os.rename('html', 'docs')"""