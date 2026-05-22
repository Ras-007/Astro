# File Organizer using os module

import os
import shutil

path = input("Enter folder path: ")

image_extensions = [".jpg", ".jpeg", ".png"]
pdf_extensions = [".pdf"]
video_extensions = [".mp4", ".mkv", ".avi"]

for file in os.listdir(path):

    file_path = os.path.join(path, file)

    if os.path.isfile(file_path):

        ext = os.path.splitext(file)[1].lower()

        if ext in image_extensions:
            folder = "Images"

        elif ext in pdf_extensions:
            folder = "PDFs"

        elif ext in video_extensions:
            folder = "Videos"

        else:
            continue

        destination = os.path.join(path, folder)

        if not os.path.exists(destination):
            os.makedirs(destination)

        shutil.move(file_path, os.path.join(destination, file))

print("Files organized successfully.")
