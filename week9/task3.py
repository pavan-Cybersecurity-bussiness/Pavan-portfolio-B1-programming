import os

def main():
    print("---- Lab Task 3: File Manager ----\n")

    # Display current working directory
    current_dir = os.getcwd()
    print(f"Current Working Directory: {current_dir}\n")

    folder_name = "lab_files"
    folder_path = os.path.join(current_dir, folder_name)

    # Create a new folder called "lab_files"
    if not os.path.exists(folder_path):
        os.mkdir(folder_path)
        print(f"Folder '{folder_name}' created successfully.\n")
    else:
        print(f"Folder '{folder_name}' already exists.\n")

    # 3️Create three empty text files inside that folder
    file_names = ["file1.txt", "file2.txt", "file3.txt"]

    for file in file_names:
        file_path = os.path.join(folder_path, file)
        if not os.path.exists(file_path):
            open(file_path, 'w').close()
            print(f"Created file: {file}")
        else:
            print(f"File already exists: {file}")
    print()

    #  List all files in the folder
    print("Files inside 'lab_files':")
    files = os.listdir(folder_path)
    for file in files:
        print(f"- {file}")
    print()

    #  Rename one of the files
    old_name = os.path.join(folder_path, "file1.txt")
    new_name = os.path.join(folder_path, "renamed_file.txt")

    if os.path.exists(old_name):
        os.rename(old_name, new_name)
        print("file1.txt renamed to renamed_file.txt\n")
    else:
        print("file1.txt does not exist, cannot rename.\n")

    # Verify rename
    print("Updated file list:")
    for file in os.listdir(folder_path):
        print(f"- {file}")
    print()

    # Clean up: remove all files and folder
    print("Starting cleanup process...")

    for file in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file)
        os.remove(file_path)
        print(f"Deleted file: {file}")

    os.rmdir(folder_path)
    print(f"Deleted folder: {folder_name}")

    print("\nCleanup completed successfully.")

if __name__ == "__main__":
    main()