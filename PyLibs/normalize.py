import os
import re

def normalize_line(line):
    # Remove comments and strip leading/trailing whitespace
    line = line.split('//')[0].strip()
    
    # Normalize multiple spaces and tabs to a single space
    line = re.sub(r'\s+', ' ', line)
    
    # Remove extra space before or after symbols like '=', '<<', ';'
    line = re.sub(r'\s*([=<<;])\s*', r'\1', line)
    
    # Convert to lower case for case-insensitive comparison
    line = line.lower()
    
    return line

def normalize_file(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()

        normalized_lines = [normalize_line(line) for line in lines]

        with open(file_path, 'w') as file:
            for line in normalized_lines:
                file.write(line + '\n')  # Write each line with newline character

        print(f"Normalized {file_path}")

    except Exception as e:
        print(f"An error occurred while normalizing {file_path}: {e}")

def main():
    # Get the directory from the user
    dir_path = input("Enter the path to the directory for normalization: ").strip()

    # Check if the directory exists
    if not os.path.isdir(dir_path):
        print(f"The directory {dir_path} does not exist.")
        return

    # Loop through the files in the directory
    for filename in os.listdir(dir_path):
        # Process only .d files
        if filename.endswith('.d'):
            file_path = os.path.join(dir_path, filename)
            if os.path.isfile(file_path):
                normalize_file(file_path)

if __name__ == "__main__":
    main()
