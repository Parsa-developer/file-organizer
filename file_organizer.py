import os
import shutil
from pathlib import Path

File_Categories = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff'],
    'Documents': ['.pdf', '.doc', '.docx', '.txt', '.rtf', '.odt'],
    'Videos': ['.mp4', '.mkv', '.avi', '.mov', '.wmv'],
    'Music': ['.mp3', '.wav', '.flac', '.aac'],
    'Archives': ['.zip', '.rar', '.tar', '.gz', '.7z'],
    'Scripts': ['.py', '.js', '.sh', '.bat'],
    'Others': []
}

def get_category(extension):
    for category, extensions in File_Categories.items():
        if extension.lower() in extensions:
            return category
        return "Others"
    
def organize_files(directory):
    directory = Path(directory)

    if not directory.exists() or not directory.is_dir():
        print(f"❌ Error: '{directory}' is not a valid directory.")
        return
    print(f"📂 Organizing files in: {directory}")

    moved_files = 0

    for item in directory.iterdir():
        if item.is_file():
            extension = item.suffix.lower()
            category = get_category(extension)
            
            category_folder = directory / category
            category_folder.mkdir(exist_ok=True)
            
            destination = category_folder / item.name
            
            counter = 1
            while destination.exists():
                base_name = item.stem + f"_copy{counter}"
                destination = category_folder / f"{base_name}{item.suffix}"
                counter += 1
            
            try:
                shutil.move(str(item), str(destination))
                print(f"✅ Moved '{item.name}' to '{category}' folder")
                moved_files += 1
            except Exception as e:
                print(f"❌ Error moving '{item.name}': {e}")
    if moved_files == 0:
        print("ℹ️ No files were found to organize.")
    else:
        print(f"🎉 Successfully organized {moved_files} files!")

def main():
    print("Welcome to the File Organizer! 📁")
    print("This tool organizes files into folders based on their extensions.")
    
    while True:
        directory = input("\nEnter the directory path to organize (or 'exit' to quit): ").strip()
        
        if directory.lower() == 'exit':
            print("Thanks for using the File Organizer! 😊")
            break
        
        organize_files(directory)
        
        continue_organizing = input("\nOrganize another directory? (yes/no): ").lower()
        if continue_organizing != 'yes':
            print("Goodbye! 🚀")
            break

if __name__ == "__main__":
    main()