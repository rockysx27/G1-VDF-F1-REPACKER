import os

# Path to the configuration file
config_file_path = 'D:\\EX\\config.txt'

def read_config(config_file):
    start_directory = 1
    end_directory = 9
    name = ''
    if os.path.exists(config_file):
        with open(config_file, 'r') as file:
            for line in file:
                if line.startswith('start_directory'):
                    start_directory = int(line.split('=')[1].strip())
                elif line.startswith('end_directory'):
                    end_directory = int(line.split('=')[1].strip())
                elif line.startswith('name'):
                    name = line.split('=')[1].strip()
    return start_directory, end_directory, name

# Read the start, end directory numbers, and name from the configuration file
start_directory, end_directory, name = read_config(config_file_path)

# Function to generate the list of directories based on the number range
def generate_directories(base_path, start, end):
    directories = []
    for i in range(start, end + 1):
        directories.append(os.path.join(base_path, f"{i}\\_work\\data\\textures\\_compiled"))
        directories.append(os.path.join(base_path, f"{i}\\_work\\data\\scripts\\_compiled"))
        directories.append(os.path.join(base_path, f"{i}\\_work\\data\\sound\\speech"))
        directories.append(os.path.join(base_path, f"{i}\\_work\\data\\worlds\\addon"))
        directories.append(os.path.join(base_path, f"{i}\\_work\\data\\worlds\\newworld"))
        directories.append(os.path.join(base_path, f"{i}\\_work\\data\\worlds\\oldworld"))
        directories.append(os.path.join(base_path, f"{i}\\_work\\data\\worlds\\shvalley"))
        directories.append(os.path.join(base_path, f"{i}\\_work\\data\\worlds\\vobtree"))
        directories.append(os.path.join(base_path, f"{i}\\_work\\data\\anims\\_compiled"))
    return directories

# Base path for directories
base_path = 'D:\\EX'

# Generate the list of directories
directories = generate_directories(base_path, start_directory, end_directory)

# Include the base _work directory for cleanup
directories.append(os.path.join(base_path, '_work', 'data', 'textures', '_compiled'))
directories.append(os.path.join(base_path, '_work', 'data', 'scripts', '_compiled'))
directories.append(os.path.join(base_path, '_work', 'data', 'sound', 'speech'))
directories.append(os.path.join(base_path, '_work', 'data', 'worlds', 'addon'))
directories.append(os.path.join(base_path, '_work', 'data', 'worlds', 'newworld'))
directories.append(os.path.join(base_path, '_work', 'data', 'worlds', 'oldworld'))
directories.append(os.path.join(base_path, '_work', 'data', 'worlds', 'shvalley'))
directories.append(os.path.join(base_path, '_work', 'data', 'worlds', 'vobtree'))
directories.append(os.path.join(base_path, '_work', 'data', 'anims', '_compiled'))

# Loop through each directory
for directory in directories:
    # Ensure the directory exists
    if os.path.exists(directory):
        # Get the list of files in the directory
        files = os.listdir(directory)
        
        # Loop through each file in the directory
        for file in files:
            # Determine the file path
            file_path = os.path.join(directory, file)
            
            # Check if it's a file (not a directory) and delete it
            if os.path.isfile(file_path):
                os.remove(file_path)
                print(f"Deleted: {file_path}")
    else:
        print(f"Directory does not exist: {directory}")

print("Cleanup complete. All files have been deleted from the specified directories.")
