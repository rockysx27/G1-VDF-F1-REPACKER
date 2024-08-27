import os
import re

def parse_variable(line):
    """Extract variable name and value from a declaration line."""
    match = re.match(r'^\s*const\s+int\s+(\w+)\s*=\s*(\d+)\s*;', line)
    if match:
        var_name = match.group(1)
        var_value = match.group(2)
        return var_name, var_value
    return None, None

def process_file(file_path):
    try:
        # Read the lines from the file
        with open(file_path, 'r') as file:
            lines = file.readlines()

        variables = {}
        unique_lines = []

        for line in lines:
            var_name, var_value = parse_variable(line)
            if var_name:
                if var_name not in variables:
                    # Add the variable if it's not already in the dictionary
                    variables[var_name] = var_value
                    unique_lines.append(line)
                else:
                    # If variable name already exists, check if the value is the same
                    if variables[var_name] != var_value:
                        print(f"Variable '{var_name}' has different values: {variables[var_name]} and {var_value}.")
                    # If different, we still keep one instance
            else:
                # Keep non-variable lines unchanged
                unique_lines.append(line)

        # Write only unique lines back to the file
        with open(file_path, 'w') as file:
            file.writelines(unique_lines)

        print(f"Processed {file_path}: handled variable duplicates based on names.")

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
                process_file(file_path)

if __name__ == "__main__":
    main()
