# This file can be used to search specific text in a folder (sub-folders as well)

import os
import glob
from tqdm import tqdm  # Import tqdm for displaying progress

                    
def find_text_in_files(target_text, folder_path):
    matching_files = []

    # Walk through the folder and its subfolders
    for root, dirs, files in tqdm(os.walk(folder_path), desc="Searching for text", unit=" files"):
        for file_name in files:
            file_path = os.path.join(root, file_name)

            # Open each file and read its contents
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
                # Check if the target text is present in the file
                if target_text in file.read():
                    matching_files.append(file_path)

    return matching_files

                    
                    
    # Return the list of file paths containing the target text
    return matching_files

# Example usage:
# Provide the target text and the folder path where you want to search for the text in files
target_text = 'text_to_be_search'
folder_path = r'C:\Users\ssaha42\file\path'

# Perform the search
matching_files = find_text_in_files(target_text, folder_path)

# Check if any files containing the target text were found
if matching_files:
    print(f'Text found in files at:')
    for file_path in matching_files:
        print(file_path)
else:
    print('Text not found in any files.')
