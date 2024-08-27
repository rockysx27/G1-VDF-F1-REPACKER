import os
import subprocess
import shutil

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

# Function to generate the list of directories based on the number of directories
def generate_directories(base_path, start, end):
    return [os.path.join(base_path, f"{i}\\_work") for i in range(start, end + 1)]


# Base path for directories
base_path = 'D:\\EX'

# Generate the list of directories
directories = generate_directories(base_path, start_directory, end_directory)

# Path to the GothicVDFS executable
gothic_vdfs_path = 'GothicVDFS.exe'

# Path to the export directory
export_dir = base_path

# Ensure the export directory exists
os.makedirs(export_dir, exist_ok=True)

# Function to generate a VM file
def generate_vm_file(directory):
    directory = os.path.abspath(directory)
    vm_file_path = os.path.join(directory, 'script.vm')
    
    print(f"Generating VM file at: {vm_file_path}")
    
    if not os.path.exists(directory):
        print(f"Directory does not exist: {directory}")
        return None
    
    vm_content = (
        '[BEGINVDF]\n'
        'Comment=Some VDFS archive\n'
        f'BaseDir={directory}\n'
        f'VDFName={os.path.basename(os.path.dirname(directory))}.vdf\n'
        '[FILES]\n'
        'Data\\Textures\\_Compiled\\*\n'  # Include all .TEX files in Data\Textures
        'Data\\Meshes\\_Compiled\\*\n'
        'Data\\Scripts\\_Compiled\\*\n'
        'Data\\Anims\\_Compiled\\*\n'
        'Data\\Meshes\\_Compiled\\*\n'
        'Data\\Worlds\\*\n'
        'Data\\Worlds\\Addon\\*\n'
        'Data\\Worlds\\OldWorld\\*\n'
        'Data\\Worlds\\NewWorld\\*\n'
        'Data\\Worlds\\ShValley\\*\n'
        'Data\\Worlds\\VobTree\\*\n'
        'Data\\Sound\\Speech\\*\n'
        'Data\\Sound\\Sfx\\*\n'
        '[EXCLUDE]\n'
        '[INCLUDE]\n'
        '[ENDVDF]\n'
    )
    
    try:
        with open(vm_file_path, 'w') as vm_file:
            vm_file.write(vm_content)
    except Exception as e:
        print(f"Error writing VM file: {e}")
        return None
    
    return vm_file_path

# Function to build VDF for a given directory
def build_vdf(directory):
    try:
        vm_file_path = generate_vm_file(directory)
        if vm_file_path is None:
            print(f"Skipping directory due to VM file generation error: {directory}")
            return
        
        command = [gothic_vdfs_path, '/B', vm_file_path]
        
        working_dir = os.path.abspath(directory)
        
        print(f"Running command: {' '.join(command)}")
        
        result = subprocess.run(command, cwd=working_dir, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print(f"Build successful for directory: {directory}")
        print(result.stdout.decode())
        
        # Determine the parent directory name for VDF file naming
        parent_dir_name = os.path.basename(os.path.dirname(directory))
        
        # Find and move VDF files to the export directory
        vdf_files = [f for f in os.listdir(working_dir) if f.endswith('.vdf')]
        for vdf_file in vdf_files:
            new_vdf_path = os.path.join(export_dir, f"{name}_{parent_dir_name}.vdf")
            shutil.move(os.path.join(working_dir, vdf_file), new_vdf_path)
            print(f"Moved {vdf_file} to {new_vdf_path}")
            
    except Exception as e:
        print(f"Error processing directory {directory}: {e}")

# Main script execution
def main():
    for directory in directories:
        build_vdf(directory)

if __name__ == "__main__":
    main()
