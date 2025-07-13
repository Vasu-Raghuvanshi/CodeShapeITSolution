# CodeShapeITSolution


# File Organizer - Console Python Tool

A Python console application that automatically organizes files in folders by moving them into categorized subfolders based on their file extensions.

## 🚀 Features

### Core Features
✅ **Smart File Detection**: Automatically detects file types based on extensions  
✅ **Category Folders**: Creates organized subfolders for different file types  
✅ **Duplicate Handling**: Handles file name conflicts with automatic renaming  
✅ **Enhanced Error Handling**: Graceful handling of permission errors and system issues  
✅ **Detailed Logging**: Comprehensive log files with timestamps  
✅ **Cross-Platform**: Works on Windows, Mac, and Linux  

## 📁 File Categories

The organizer sorts files into these categories:

- **📸 Images**: .jpg, .jpeg, .png, .gif, .bmp
- **🎬 Videos**: .mp4, .avi, .mkv, .mov, .flv  
- **🎵 Audio**: .mp3, .wav, .flac, .aac
- **📄 Documents**: .pdf, .doc, .docx, .txt, .ppt, .pptx, .xls, .xlsx
- **💾 Applications**: .exe, .msi, .apk
- **📦 Archives**: .zip, .rar, .7z, .tar, .gz
- **📋 Others**: Files with unrecognized extensions
## 🛡️ Error Handling

The application includes comprehensive error handling for:
- **Permission Errors**: Files in use or restricted access
- **File Not Found**: Missing files during organization
- **System Errors**: OS-level issues
- **Duplicate Names**: Automatic renaming with counters (e.g., file_(1).txt)

## 💻 Technical Requirements

- **Language**: Python 3.6+
- **Dependencies**: Standard library only (os, shutil, datetime)
- **Platform**: Cross-platform (Windows, Mac, Linux)

## 🎯 Use Cases

- **Downloads Folder**: Organize cluttered downloads
- **Desktop Cleanup**: Sort files on desktop
- **Project Organization**: Organize project assets
- **Backup Preparation**: Structure files before backup
- **File Server Management**: Organize shared folders

## 🔒 Safety Features

- **Non-destructive**: Only moves files, never deletes
- **Conflict Resolution**: Renames duplicates instead of overwriting
- **Comprehensive Logging**: Track all operations with timestamps
- **Error Recovery**: Graceful handling of all error conditions



# 🔧 How to Run

### Console Version
```bash
python main.py
```

## 📋 How to Use

1. **Run the program**: Execute `python main.py` in your terminal
2. **Choose folder**: 
   - Type the full path of the folder you want to organize
   - Or press Enter to use the default "Download" folder
3. **Watch it work**: The program will automatically:
   - Create category folders (Images, Videos, Documents, etc.)
   - Move files to their appropriate folders
   - Handle duplicate names by adding numbers
   - Show progress in the terminal
4. **Check results**: 
   - View organized files in their new folders
   - Check the log file in the "Logs" folder for details

## 📊 Sample Organization

**Before organizing:**
```
MyFolder/
├── vacation.jpg
├── presentation.pptx
├── song.mp3
├── movie.mp4
├── installer.zip
├── document.pdf
└── script.py
```

**After organizing:**
```
MyFolder/
├── Images/
│   └── vacation.jpg
├── Documents/
│   ├── presentation.pptx
│   └── document.pdf
├── Audio/
│   └── song.mp3
├── Videos/
│   └── movie.mp4
├── Archives/
│   └── installer.zip
├── Others/
│   └── script.py
└── Logs/
    └── file_organizer.log
```



# 📝 Assignment Information

**Organisation**: Code Shape IT Solutions
**Topic1**: Python Intern Task
**Task**: Console Based File Management and Organization Program  
**Language**: Python 3  
**Concepts**: File I/O, Error Handling, File System Operations

---

**Name**: Vasu Raghuvanshi
**E-mail**: vasuraghuvanshi001@gmail.com
**Date**: 13/07/2025
