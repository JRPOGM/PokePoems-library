import os
import shutil

def copy_files_recursive(source_path, destination_path):
    if not os.path.exists(destination_path):
        os.mkdir(destination_path)

    for file in os.listdir(source_path):
        source = os.path.join(source_path, file)
        destination = os.path.join(destination_path, file)
        print(f" * {source} -> {destination}")
        if os.path.isfile(source):
            shutil.copy(source, destination)
        else:
            copy_files_recursive(source, destination)