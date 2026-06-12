import os
import shutil

from copystatic import copy_files_recursive
from gencontent import generate_page

direct_path_static = "./static"
direct_path_public = "./public"
direct_path_content = "./content"
template_path = "./template.html"

def main():
    print("Deleting public directory...")
    if os.path.exists(direct_path_public):
        shutil.rmtree(direct_path_public)
    print("Copying static files to public directory...")
    copy_files_recursive(direct_path_static, direct_path_public)
    print("Generating page...")
    generate_page(os.path.join(direct_path_content, "index.md"),
                  template_path,
                  os.path.join(direct_path_public, "index.html"))
    generate_page(
        os.path.join(direct_path_content, "blog/glorfindel/index.md"),
        template_path,
        os.path.join(direct_path_public, "blog/glorfindel/index.html"))
    generate_page(
        os.path.join(direct_path_content, "blog/tom/index.md"),
        template_path,
        os.path.join(direct_path_public, "blog/tom/index.html"))
    generate_page(
        os.path.join(direct_path_content, "blog/majesty/index.md"),
        template_path,
        os.path.join(direct_path_public, "blog/majesty/index.html"))

main()
