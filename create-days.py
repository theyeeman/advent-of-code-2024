import shutil
import os.path

NUM_DAYS = 25
SRC_DIRECTORY = "./dayx"
OVERWRITE_EXISTING = False

for day_num in range(1, NUM_DAYS+1):
    dest_directory = f"./day{day_num}"

    if not OVERWRITE_EXISTING and os.path.isdir(dest_directory):
        print(f"{dest_directory} already exists, skipping...")
    else:
        print(f"Creating directory {dest_directory}")
        shutil.copytree(SRC_DIRECTORY, dest_directory)