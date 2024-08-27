import os
import shutil

# Path to the configuration file
config_file_path = 'D:\\EX\\config.txt'

def read_config(config_file):
    start_directory = 1
    end_directory = 9
    name = ''
    directory_patterns = {
        'textures': 'textures\\_compiled',
        'scripts': 'scripts\\_compiled',
        'sound': 'sound\\speech',
        'worlds': 'worlds\\addon',
        'anims': 'anims\\_compiled',
        'meshes': 'meshes\\_compiled'
    }
    
    if os.path.exists(config_file):
        with open(config_file, 'r') as file:
            for line in file:
                if line.startswith('start_directory'):
                    start_directory = int(line.split('=')[1].strip())
                elif line.startswith('end_directory'):
                    end_directory = int(line.split('=')[1].strip())
                elif line.startswith('name'):
                    name = line.split('=')[1].strip()
                elif line.startswith('textures_directory'):
                    directory_patterns['textures'] = line.split('=')[1].strip()
                elif line.startswith('scripts_directory'):
                    directory_patterns['scripts'] = line.split('=')[1].strip()
                elif line.startswith('sound_directory'):
                    directory_patterns['sound'] = line.split('=')[1].strip()
                elif line.startswith('worlds_directory'):
                    directory_patterns['worlds'] = line.split('=')[1].strip()
                elif line.startswith('anims_directory'):
                    directory_patterns['anims'] = line.split('=')[1].strip()
                elif line.startswith('meshes_directory'):
                    directory_patterns['meshes'] = line.split('=')[1].strip()
                    
    return start_directory, end_directory, name, directory_patterns

# Read configuration
start_directory, end_directory, name, directory_patterns = read_config(config_file_path)

# Function to generate destination directories based on patterns
def generate_dest_dirs(base_path, start, end, patterns):
    dest_dirs = {}
    for key, pattern in patterns.items():
        for i in range(start, end + 1):
            dest_dirs[f"{key}_{i}"] = os.path.join(base_path, f"{i}\\_work\\data\\{pattern}")
    return dest_dirs

# Base path for directories
base_path = 'D:\\EX'

# Define source directories
source_dirs = {
    'textures': os.path.join(base_path, '_work', 'data', directory_patterns['textures']),
    'scripts': os.path.join(base_path, '_work', 'data', directory_patterns['scripts']),
    'sound': os.path.join(base_path, '_work', 'data', directory_patterns['sound']),
    'worlds': os.path.join(base_path, '_work', 'data', directory_patterns['worlds']),
    'anims': os.path.join(base_path, '_work', 'data', directory_patterns['anims']),
    'meshes': os.path.join(base_path, '_work', 'data', directory_patterns['meshes']),
}

# Define file extension to destination category mapping
extension_mapping = {
    '.tex': 'textures',
    '.dds': 'textures',
    '.png': 'textures',
    '.bmp': 'textures',
    '.d': 'scripts',
    '.mdm': 'anims',
    '.mmb': 'anims',
    '.man': 'anims',
    '.msb': 'anims',
    '.mdh': 'anims',
    '.mms': 'anims',
    '.mrm': 'meshes',
    '.dll': 'scripts',
    '.txt': 'scripts',
    '.xml': 'scripts',
    '.ogg': 'sound',
    '.wav': 'sound',
    '.mp3': 'sound',
    '.dat': 'worlds',
    '.bsp': 'worlds',
    '.vob': 'worlds',
    '.shv': 'worlds',
    '.vbt': 'worlds',
    '.zen': 'worlds',  # Gothic-specific extensions
    '.pak': 'worlds',    # Additional extension
    '.bin': 'worlds'     # Additional extension
}

# Convert all extensions to lowercase for consistent comparison
extension_mapping = {k.lower(): v for k, v in extension_mapping.items()}

# Generate destination directories
dest_dirs = generate_dest_dirs(base_path, start_directory, end_directory, directory_patterns)

# Ensure all destination directories exist
for dest_dir in dest_dirs.values():
    os.makedirs(dest_dir, exist_ok=True)

# Function to move files based on their extension
def move_files(source_dirs, dest_dirs):
    for category, source_dir in source_dirs.items():
        if os.path.exists(source_dir):
            files = os.listdir(source_dir)
            for file in files:
                source_file = os.path.join(source_dir, file)
                if os.path.isfile(source_file):
                    file_ext = os.path.splitext(file)[1].lower()
                    dest_category = extension_mapping.get(file_ext, None)
                    if dest_category:
                        # Determine destination directory based on file index
                        dest_dir = dest_dirs.get(f"{dest_category}_{(files.index(file) % (end_directory - start_directory + 1) + start_directory)}", None)
                        if dest_dir:
                            dest_file = os.path.join(dest_dir, file)
                            shutil.move(source_file, dest_file)
                            print(f"Moved {file} from {source_dir} to {dest_file}")
                        else:
                            print(f"No destination directory found for {file} (extension: {file_ext})")
                    else:
                        print(f"File extension {file_ext} not mapped to a category for file {file}")
        else:
            print(f"Source directory does not exist: {source_dir}")

move_files(source_dirs, dest_dirs)

print("Files have been distributed among the specified directories.")
