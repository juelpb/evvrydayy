import os
import shutil
from datetime import datetime

def copy_and_rename_with_date(src_file, dest_dir,postfix, initials):
    """
    Copies a file to the destination directory and renames it with a date-based timestamp.

    :param src_file: Path to the source file
    :param dest_dir: Path to the destination directory
    """
    # Ensure destination directory exists
    os.makedirs(dest_dir, exist_ok=True)

    # Extract the file name and extension
    base_name, ext = os.path.splitext(os.path.basename(src_file))

    # Generate a new file name with the current date
    date_str = datetime.now().strftime("%Y-%m-%d")
    new_file_name = f"{base_name}_{postfix}_{initials}_{date_str}{ext}"

    # Full path for the new file
    dest_file = os.path.join(dest_dir, new_file_name)

    # Copy the file and rename it
    shutil.copy(src_file, dest_file)

    print(f"File copied and renamed to: {dest_file}")

# Example usage:
# copy_and_rename_with_date("path/to/source/file.txt", "path/to/destination")


def search_file(directory, keywords, filetype):
    """
    Searches for files in a directory containing specified keywords and filetype.

    :param directory: Directory to search in
    :param keywords: List of keywords the file name might contain
    :param filetype: The file extension to filter by (e.g., ".txt")
    :return: The selected file path or None if no files found
    """
    if not os.path.exists(directory):
        print("The specified directory does not exist.")
        return None

    # Ensure keywords is a list
    if isinstance(keywords, str):
        keywords = [keywords]

    # Find matching files
    matching_files = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(filetype) and all(keyword in file for keyword in keywords):
                matching_files.append(os.path.join(root, file))

    # Handle the results
    if not matching_files:
        print("No matching files found.")
        return None
    elif len(matching_files) == 1:
        print(f"Found one file: {matching_files[0]}")
        return matching_files[0]
    else:
        print("Multiple files found:")
        for idx, file in enumerate(matching_files, start=1):
            print(f"{idx}: {file}")
        choice = int(input("Enter the number of the file you want to select: ")) - 1
        if 0 <= choice < len(matching_files):
            return matching_files[choice]
        else:
            print("Invalid choice.")
            return None

# Example usage:
# selected_file = search_file("path/to/directory", ["report", "2023"], ".pdf")
# print(f"Selected file: {selected_file}")


def sk_ek_ina_generator():
    section_folder = ""
    sk_folder = ""
    inits = "JPB"
    
    user_input = input("Do you to do EK/SK or innarbeide SK?\n[1] EK\n[2] SK\n[3] INA")
    
    if user_input == "1":
        file_to_rename = search_file(section_folder, sk_folder, )
        copy_and_rename_with_date(file_to_rename, sk_folder,"EK", inits)
