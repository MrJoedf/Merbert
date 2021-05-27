# Merbert
Command-line file management system that uses more natural-sounding commands than standard shell scripts.

When the application is first run, the "source" directory will be your default user directory. All directories you enter will be appended to the source directory.

To set the source directory to another directory, use the format: **setsource "path/folder"** (_Feature in progress_)

To move files to another directory, use the format: move "keyword" to "otherfolder"
  - This format will search for the keyword in the source folder. To narrow it, use the format: 
    -  move "keyword" in "source/otherfolder" to **"source/otherfolder/deepfolder"**

To make a new directory or file, use the format: make "newdir"
 - For more specific locations to make the directory, use the format:** make "newdir" in "folder"**

To delete files based on a keyword or file extension, use the format: **delete "keyword" in "folder"**
