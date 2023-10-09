import os
import shutil
from bs4 import BeautifulSoup


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
            
            # Read the file
            with open(old_file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Use BeautifulSoup to parse the content
            soup = BeautifulSoup(content, 'html.parser')
            
            # Find the <body> tag and remove everything before it
            body_tag = soup.find('body')
            if body_tag:
                body_start_index = content.find(str(body_tag))
                if body_start_index != -1:
                    new_content = content[body_start_index:]
                else:
                    new_content = content
            else:
                new_content = content
            
            # Replace ".html" with ".md" in all <a> tags' href attributes
            for a_tag in soup.find_all('a'):
                if 'href' in a_tag.attrs:
                    a_tag['href'] = a_tag['href'].replace(old_extension, new_extension)
            
            # Write the modified content back to the file
            with open(new_file_path, 'w', encoding='utf-8') as f:
                f.write(str(soup))
            
            # Remove the old file
            os.remove(old_file_path)
            
            print(f'Modified and renamed: {old_file_path} -> {new_file_path}')