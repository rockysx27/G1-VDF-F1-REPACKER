import os
import re

def normalize_line(line):
    # Remove comments and strip leading/trailing whitespace
    line = line.split('//')[0].strip()
    # Normalize multiple spaces and tabs to a single space
    line = re.sub(r'\s+', ' ', line)
    # Convert to lower case for case-insensitive comparison
    line = line.lower()
    return line

def is_critical_line(line):
    # Define what constitutes a critical line (e.g., containing '{' or '}')
    return any(c in line for c in '{}')

def remove_duplicates(file_path):
    try:
        # Read the lines from the file
        with open(file_path, 'r') as file:
            lines = file.readlines()

        seen_lines = {}
        unique_lines = []

        for line in lines:
            normalized_line = normalize_line(line)

            if is_critical_line(line):
                # If the line is critical, add it to unique_lines and skip deduplication
                unique_lines.append(line)
                seen_lines[normalized_line] = line
            elif normalized_line not in seen_lines:
                # If this normalized line hasn't been seen, keep it and store its line
                seen_lines[normalized_line] = line
                unique_lines.append(line)
            else:
                print(f"Duplicate found (ignoring comments and formatting): {line.strip()}")

        # Write only unique lines back to the file
        with open(file_path, 'w') as file:
            file.writelines(unique_lines)

        print(f"Processed {file_path}: removed duplicates based on normalized code.")

    except Exception as e:
        print(f"An error occurred while processing {file_path}: {e}")

def main():
    # Get the directory from the user
    dir_path = input("Enter the path to the directory: ").strip()

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
                remove_duplicates(file_path)

if __name__ == "__main__":
    main()
