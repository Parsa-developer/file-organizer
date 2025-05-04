📁 File Organizer 🗂️
Welcome to the File Organizer, a powerful Python tool to tidy up your messy directories! 🧹 This command-line application sorts files into categorized folders based on their extensions (e.g., Images, Documents, Videos). Say goodbye to clutter and hello to organization! 🚀

🌟 Features

📂 Automatically sorts files into folders like Images, Documents, Videos, and more.
🖼️ Supports common file types (e.g., .jpg, .pdf, .mp3) with a catch-all Others folder.
🔄 Handles duplicate file names by adding a suffix (e.g., file_copy1.jpg).
✅ Error handling for invalid directories or file move issues.
😊 User-friendly interface with emoji-enhanced feedback.


🛠️ Requirements

Python 3.x 🐍
No external libraries required (uses standard os, shutil, and pathlib)


📦 Installation

Clone this repository:git clone https://github.com/parsa-developer/file-organizer.git


Navigate to the project directory:cd file-organizer




🎯 Usage

Run the script:python file_organizer.py


Enter the full path to the directory you want to organize (e.g., C:\Users\YourName\Downloads or /home/user/downloads).
Watch as files are sorted into folders like Images, Documents, Videos, etc.
Choose to organize another directory or exit.


📸 Example
Welcome to the File Organizer! 📁
This tool organizes files into folders based on their extensions.

Enter the directory path to organize (or 'exit' to quit): /home/user/downloads
📂 Organizing files in: /home/user/downloads
✅ Moved 'photo.jpg' to 'Images' folder
✅ Moved 'report.pdf' to 'Documents' folder
✅ Moved 'song.mp3' to 'Music' folder
✅ Moved 'unknown.xyz' to 'Others' folder
🎉 Successfully organized 4 files!

Organize another directory? (yes/no): no
Goodbye! 🚀


🔧 Notes

Supported Categories: Images (.jpg, .png, etc.), Documents (.pdf, .docx, etc.), Videos (.mp4, .mkv, etc.), Music (.mp3, .wav, etc.), Archives (.zip, .rar, etc.), Scripts (.py, .js, etc.), and Others for uncategorized files.
Duplicates: If a file already exists in the destination folder, a suffix (e.g., _copy1) is added to avoid overwriting.
Cross-Platform: Works on Windows, macOS, and Linux thanks to pathlib.
Safety: Only moves files, not directories, to avoid unintended changes.


🚀 Future Improvements

🎨 Add a GUI with tkinter or PyQt for a visual interface.
📋 Support custom category mappings via a configuration file.
🔎 Add filters for file size or date to organize selectively.
🗑️ Include an option to delete empty folders after organizing.
📊 Generate a summary report of organized files.


🤝 Contributing
Want to make this organizer even better? 🌈 Fork the repo, submit pull requests, or open issues for bugs or feature ideas. Let’s keep those files tidy! 💪

📜 License
This project is licensed under the MIT License. See the LICENSE file for details.

Declutter your directories today! 📁 Give this repo a ⭐ if it helps you stay organized!
