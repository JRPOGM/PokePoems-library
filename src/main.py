import os
import shutil
import sys

from copystatic import copy_files_recursive
from gencontent import generate_pages_recursive

direct_path_static = "./static"
direct_path_public = "./docs"
direct_path_content = "./content"
template_path = "./template.html"
default_basepath = "/"

def main():
    basepath = default_basepath
    if len(sys.argv) > 1:
        basepath = sys.argv[1]
    print("Deleting public directory...")
    if os.path.exists(direct_path_public):
        shutil.rmtree(direct_path_public)
    print("Copying static files to public directory...")
    copy_files_recursive(direct_path_static, direct_path_public)
    print("Generating page...")
    generate_pages_recursive(direct_path_content, template_path, direct_path_public, basepath)
main()
