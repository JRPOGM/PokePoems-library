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
        os.path.join(direct_path_content, "pokemon/bulbasaur/index.md"),
        template_path,
        os.path.join(direct_path_public, "pokemon/bulbasaur/index.html"))
    generate_page(
        os.path.join(direct_path_content, "pokemon/charmander/index.md"),
        template_path,
        os.path.join(direct_path_public, "pokemon/charmander/index.html"))
    generate_page(
        os.path.join(direct_path_content, "pokemon/squirtle/index.md"),
        template_path,
        os.path.join(direct_path_public, "pokemon/squirtle/index.html"))
    generate_page(
        os.path.join(direct_path_content, "pokemon/caterpie/index.md"),
        template_path,
        os.path.join(direct_path_public, "pokemon/caterpie/index.html"))
    generate_page(
        os.path.join(direct_path_content, "pokemon/weedle/index.md"),
        template_path,
        os.path.join(direct_path_public, "pokemon/weedle/index.html"))
    generate_page(
        os.path.join(direct_path_content, "pokemon/pidgey/index.md"),
        template_path,
        os.path.join(direct_path_public, "pokemon/pidgey/index.html"))
    generate_page(
        os.path.join(direct_path_content, "pokemon/rattata/index.md"),
        template_path,
        os.path.join(direct_path_public, "pokemon/rattata/index.html"))
    generate_page(
        os.path.join(direct_path_content, "pokemon/spearow/index.md"),
        template_path,
        os.path.join(direct_path_public, "pokemon/spearow/index.html"))
    generate_page(
        os.path.join(direct_path_content, "pokemon/ekans/index.md"),
        template_path,
        os.path.join(direct_path_public, "pokemon/ekans/index.html"))
    generate_page(
        os.path.join(direct_path_content, "pokemon/sandshrew/index.md"),
        template_path,
        os.path.join(direct_path_public, "pokemon/sandshrew/index.html"))
    generate_page(
        os.path.join(direct_path_content, "pokemon/nidoranf/index.md"),
        template_path,
        os.path.join(direct_path_public, "pokemon/nidoranf/index.html"))
    generate_page(
        os.path.join(direct_path_content, "pokemon/nidoranm/index.md"),
        template_path,
        os.path.join(direct_path_public, "pokemon/nidoranm/index.html"))
    generate_page(
        os.path.join(direct_path_content, "pokemon/vulpix/index.md"),
        template_path,
        os.path.join(direct_path_public, "pokemon/vulpix/index.html"))
    generate_page(
        os.path.join(direct_path_content, "pokemon/zubat/index.md"),
        template_path,
        os.path.join(direct_path_public, "pokemon/zubat/index.html"))
    generate_page(
        os.path.join(direct_path_content, "pokemon/oddish/index.md"),
        template_path,
        os.path.join(direct_path_public, "pokemon/oddish/index.html"))

main()
