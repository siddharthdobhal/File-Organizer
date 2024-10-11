import os
import shutil

# Define the path to the directory you want to organize
directory = "D:/try"  # Replace with your directory path

# Loop through all the files in the specified directory
for filename in os.listdir(directory):
    # Check if it's a file and not a directory
    file_path = os.path.join(directory, filename)
    if os.path.isfile(file_path):
        # Get the file extension and name
        file_extension = filename.split('.')[-1].lower()
        folder_name = f"{file_extension}_files"  # Create a folder name based on file extension
        
        # Create a new folder for this file extension if it doesn't exist
        folder_path = os.path.join(directory, folder_name)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
        
        # Move the file to the newly created folder
        shutil.move(file_path, folder_path)
        
print("Files organized successfully!")
