import os
from pathlib import Path
from block_types import markdown_to_html_node

def extract_title(markdown):
    lines = markdown.split("\n")
    for line in lines:
        if line.startswith("# "):
            return line[2:]
    return ValueError("Missing heading")

def generate_pages_recursive(dir_path_content: str, template_path: str, template_path_2: str, dest_dir_path: str, basepath: str) -> None:
    for filename in os.listdir(dir_path_content):
        from_path = os.path.join(dir_path_content, filename)
        dest_path = os.path.join(dest_dir_path, filename)
        if os.path.isfile(from_path):
            dest_path = Path(dest_path).with_suffix(".html")
            generate_page(from_path, template_path, dest_path, basepath)
            generate_page(from_path, template_path_2, dest_path, basepath)
        else:
            generate_pages_recursive(from_path, template_path, dest_path, basepath)
            generate_pages_recursive(from_path, template_path_2, dest_path, basepath)


def generate_page(from_path: str, template_path: str, dest_path: str | Path, basepath: str) -> None:
    print(f"Greeting page from {from_path} to {dest_path} using {template_path}.")
    source = open(from_path, "r")
    markdown_file = source.read()
    source.close()
    template = open(template_path, "r")
    template_content = template.read()
    template.close()
    node = markdown_to_html_node(markdown_file)
    html = node.to_html()
    title = extract_title(markdown_file)
    template_content = template_content.replace("{{ Title }}", title)
    template_content = template_content.replace("{{ Content }}", html)
    template_content = template_content.replace('href="/', 'href="' + basepath)
    template_content = template_content.replace('src="/', 'src="' + basepath)
    destination = os.path.dirname(dest_path)
    if destination != "":
        os.makedirs(destination, exist_ok=True)
    to_file = open(dest_path, "w")
    to_file.write(template_content)
    to_file.close()