def remove_lines_with_same_variable_different_value(file1_path, file2_path):
    # Helper function to parse lines into a dictionary of variable-value pairs
    def parse_lines(lines):
        variable_dict = {}
        for line in lines:
            stripped_line = line.strip()
            # Skip comments and empty lines
            if stripped_line.startswith('#') or stripped_line == '':
                continue
            # Split the line by '=' to get variable and value
            parts = stripped_line.split('=', 1)
            if len(parts) == 2:
                variable, value = parts
                variable = variable.strip()
                value = value.strip()
                variable_dict[variable] = value
        return variable_dict
    
    # Read the content of file1 and file2
    with open(file1_path, 'r') as file1:
        file1_lines = file1.readlines()

    with open(file2_path, 'r') as file2:
        file2_lines = file2.readlines()

    # Parse lines into dictionaries
    file1_variables = parse_lines(file1_lines)
    file2_lines_filtered = []
    file2_variables = parse_lines(file2_lines)

    # Filter out lines from file2 where the variable exists in file1 with a different value
    for line2 in file2_lines:
        stripped_line2 = line2.strip()
        # Skip comments and empty lines and lines containing '{' or '}'
        if stripped_line2.startswith('#') or stripped_line2 == '' or '{' in stripped_line2 or '}' in stripped_line2:
            file2_lines_filtered.append(line2)
            continue
        
        # Split the line by '=' to get variable and value
        parts2 = stripped_line2.split('=', 1)
        if len(parts2) == 2:
            variable2, value2 = parts2
            variable2 = variable2.strip()
            value2 = value2.strip()

            # Check if the variable exists in file1 with a different value
            if variable2 in file1_variables and file1_variables[variable2] != value2:
                continue  # Skip this line

        # If not skipped, add to filtered lines
        file2_lines_filtered.append(line2)

    # Write the filtered lines back to file2
    with open(file2_path, 'w') as file2:
        file2.writelines(file2_lines_filtered)

if __name__ == "__main__":
    # Ask for file paths
    file1_path = input("Enter the path to file 1: ")
    file2_path = input("Enter the path to file 2: ")

    # Perform the line removal
    remove_lines_with_same_variable_different_value(file1_path, file2_path)

    print("Lines with the same variable but different values have been removed from file 2.")
