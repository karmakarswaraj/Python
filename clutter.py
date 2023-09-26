#Write a program to clear the clutter inside a folder on your computer.
#You should use os module to rename all the png images from 1.png all the way till n.png 
    #where n is the number of png files in that folder.
#Do the same for other file formats. For example:

    # sfdsf.png --> 1.png
    # vfsf.png --> 2.png
    # this.png --> 3.png
    # design.png --> 4.png
    # name.png --> 5.png

import os

directory = r"C:\Users\Swaraj\Desktop\COLLEGE\UDEMY CIR\ALL"

for file in os.listdir(directory):
    if file.endswith(".png"):
        #print(file)
        file_path = os.path.join(directory, file)
        # Rename the file (you need to provide the new name)

        new_filename = "new_name.txt"  # Replace "new_name.txt" with the desired new name

        new_file_path = os.path.join(directory, new_filename)

        os.rename(file_path, new_file_path)
        print(f"Renamed '{file}' to '{new_filename}'")
