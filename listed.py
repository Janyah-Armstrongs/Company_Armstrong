import os

# Get the current working directory
cwd = os.getcwd()

# Get a list of files in the directory
files = os.listdir(cwd)

# Initialize an empty list to store dictionaries
file_info = []

# Iterate over the files
for file_name in files:
    # Get the full path of the file
    file_path = os.path.join(cwd, file_name)

    # Check if it's a file (not a directory)
    if os.path.isfile(file_path):
        # Get the size of the file in bytes
        file_size = os.path.getsize(file_path)

    # Create a dictionary with file name and size
    file_dict = {
        "name": file_name,
        "size": file_size
}
    
    # Append the dictionary to the list
    file_info.append(file_dict)

# Print the list of dictionaries
print(file_info)


