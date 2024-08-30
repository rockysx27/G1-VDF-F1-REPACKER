def remove_matching_lines(file1_path, file2_path):
    # Read the content of file1 and file2
    with open(file1_path, 'r') as file1:
        file1_lines = file1.readlines()

    with open(file2_path, 'r') as file2:
        file2_lines = file2.readlines()

    # Define characters that should not be removed from file2
    essential_characters = {'{', '}'}

    def contains_essential_character(line):
        return any(char in line for char in essential_characters)

    # Remove lines from file2 that match any line in file1 (ignoring comments and whitespace)
    file2_lines_filtered = []
    for line2 in file2_lines:
        stripped_line2 = line2.strip()
        # Skip comments, empty lines, or lines with essential characters
        if stripped_line2.startswith('#') or stripped_line2 == '' or contains_essential_character(stripped_line2):
            file2_lines_filtered.append(line2)
        else:
            match_found = False
            for line1 in file1_lines:
                stripped_line1 = line1.strip()
                if stripped_line1 == stripped_line2:
                    match_found = True
                    break
            if not match_found:
                file2_lines_filtered.append(line2)

    # Write the filtered lines back to file2
    with open(file2_path, 'w') as file2:
        file2.writelines(file2_lines_filtered)

if __name__ == "__main__":
    # Ask for file paths
    file1_path = input("Enter the path to file 1: ")
    file2_path = input("Enter the path to file 2: ")

    # Perform the line removal
    remove_matching_lines(file1_path, file2_path)

    print("Matching lines have been removed from file 2.")
