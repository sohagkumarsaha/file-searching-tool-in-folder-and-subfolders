# This file can be used to search a file in a folder or  sub-folders
# import libraries and default functions
import os  # Import the os module for operating system related functionality
import glob  # Import the glob module for pattern matching file paths

def find_files(file_name, folder_path):
    # Initialize an empty list to store the file paths
    files = []
    
    # Use the glob module to search for files with the specified name in the given folder path
    for infile in glob.glob(os.path.join(folder_path, '**', file_name + '.*'), recursive=True):
        # Append each file path to the list
        files.append(infile)
    
    # Return the list of file paths
    return files

# Example usage:
# Provide the file name and the folder path where you want to search for the files
# file_paths = find_files('name_of_file_to_be_search_one', r'C:\Users\ssaha42\folder\path')
file_paths = find_files('name_of_file_to_be_search_two', r'C:\Users\ssaha42\folder\path')

# Check if any files were found
if file_paths:
    print('Files found at:')
    # Print each file path
    for file_path in file_paths:
        print(file_path)
else:
    print('No files found.')
