
"""
**Console Based File Organizer**
Description: A Python program to organize files into various category folders by type.
"""

import os
import shutil
from datetime import datetime

def create_folder(folder):
    """Create folders for different file types"""
    if not os.path.exists(folder):
      os.mkdir(folder)
      print(f"Created folder: {folder}")

def create_log(message):
    """Create a simple log file with timestamp"""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"[{timestamp}] {message}\n"

    with open("Logs/file_organizer.log", "a") as log_file:
        log_file.write(log_entry)

    #print(f"Logged: {message}")


def get_file_type(filename):
    """Return the folder name based on file extension"""
    # Get file extension
    extension = filename.lower().split('.')[-1]

    # Define file categories
    FILE_CATEGORIES = {
        "Images": ['jpg', 'jpeg', 'png', 'gif', 'bmp'],
        "Documents": ['pdf', 'doc', 'docx', 'txt', 'ppt', 'pptx', 'xls', 'xlx'],
        "Videos": ['mp4', 'mkv', 'avi', 'mov', 'flv'],
        "Audio": ['mp3', 'wav', 'aac', 'flac'],
        "Applications": ['exe', 'msi', 'apk'],
        "Archives": ['zip', 'rar', '7z', 'tar', 'gz'],
        "Logs": ['log'],
        "Others": []  # For uncategorized file types
    }
    #Creates Subfolder based on filetype
    for category, extensions in FILE_CATEGORIES.items():
        if extension in extensions:
            create_folder(category)
            return category
    create_folder("Others")
    return "Others"

def get_unique_filename(file_type, filename):
    """Handle duplicate file names by adding counter if needed"""
    destination = os.path.join(file_type, filename)
    
    # If file doesn't exist, return original destination
    if not os.path.exists(destination):
        return destination
    
    # Handle duplicates with counter
    counter = 1
    name, ext = os.path.splitext(filename)
    while os.path.exists(destination):
        new_name = f"{name}_({counter}){ext}"
        destination = os.path.join(file_type, new_name)
        counter += 1
    
    return destination

def organize_files():
    """Main function to organize files"""
    # Get folder to organize (default: Downloads)
    folder = input("Enter folder name (or press Enter for 'Downloads'): ").strip()
    if not folder:
        folder = "Downloads"

    # Check if folder exists
    if not os.path.exists(folder):
        print(f"Folder '{folder}' not found!")
        return

    print(f"\nOrganizing files in: {folder}")
    print("-" * 30)

    #"""Change dir to the target folder"""
    os.chdir(folder)  

    # Gets all files in the current folder
    files = os.listdir('.')
    files = [f for f in files if os.path.isfile(f)]

    if not files:
        print("No files to organize!")
        return

    # Move each file
    moved_count = 0
    for file in files:
        try:
            # Skip if file is already in a subfolder
            if '/' in file or '\\' in file:
                continue

            create_folder("Logs")

            # Gets the destination folder name baed on file type
            file_type = get_file_type(file)
            # Gets unique filename to avoid overwriting
            destination = get_unique_filename(file_type, file)

            # Move the file
            shutil.move(file, destination)
            moved_file_name = os.path.basename(destination)
            print(f"Moved: {file} To {file_type}/{moved_file_name}")
            create_log(f"Moved {file} to {file_type}/{moved_file_name}")
            moved_count += 1

      #Exception Handling
        except PermissionError:
            print(f" Permission denied: {file} (file may be in use)")
        except FileNotFoundError:
            print(f" File not found: {file}")
        except Exception as e:
            print(f" Error moving {file}: {e}")

  #Log Creation
    print(f"\nDone! Organized {moved_count} files.\nLogged in file_organizer.log!\n")
    create_log(f"Organized {moved_count} files in {folder}.")

def main():
    """Main program"""
    print("=== File Organizer ===")
    organize_files()

if __name__ == "__main__":
    main()
