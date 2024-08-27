import os
import shutil

def merge_files(src_file, dest_file):
    # Open the destination file in append mode and the source file in read mode
    with open(dest_file, 'a') as dest_f, open(src_file, 'r') as src_f:
        # Append the content of the source file to the destination file
        dest_f.write(src_f.read())

def main():
    # Get the first directory from the user
    dir1 = input("Enter the path to the first directory (e.g., 'G2' path): ").strip()

    # Automatically generate dir2 by replacing 'G2' with 'G1'
    if "G2" in dir1:
        dir2 = dir1.replace("G2", "G1")
    else:
        print("The directory path does not contain 'G2'. Unable to generate dir2.")
        return

    # Check if the directories exist
    if not os.path.isdir(dir1):
        print(f"The directory {dir1} does not exist.")
        return
    if not os.path.isdir(dir2):
        print(f"The directory {dir2} does not exist.")
        return

    # Loop through the files in the first directory
    for filename in os.listdir(dir1):
        file1_path = os.path.join(dir1, filename)
        
        # Ensure we are working with files only
        if os.path.isfile(file1_path):
            file2_path = os.path.join(dir2, filename)
            
            if os.path.exists(file2_path):
                # If the file exists in the second directory, merge the contents
                print(f"Merging {filename} from {dir1} into {dir2}")
                merge_files(file1_path, file2_path)
            else:
                # If the file does not exist in the second directory, move it
                print(f"Moving {filename} from {dir1} to {dir2}")
                shutil.move(file1_path, file2_path)

if __name__ == "__main__":
    main()
