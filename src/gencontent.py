import os
from block_types import markdown_to_html_node

def extract_title(markdown):
    lines = markdown.split("\n")
    for line in lines:
        if line.startswith("# "):
            return line[2:]
    return ValueError("Missing heading")

def generate_page(from_path, template_path, dest_path):
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
    destination = os.path.dirname(dest_path)
    if destination != "":
        os.markdir(destination, exist_ok=True)
    to_file = open(dest_path, "w")
    to_file.write(template_content)