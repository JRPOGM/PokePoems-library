import re
import enum
import os
from textnode import TextNode, TextType, split_nodes_delimiter
from block_types import markdown_to_html_node

def extract_markdown_images(text):
    matches = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return matches

def extract_markdown_links(text):
    matches = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return matches

def split_nodes_image(old_nodes: list[TextNode]) -> list[TextNode]:
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        texts = node.text
        images = extract_markdown_images(texts)
        if len(images) == 0:
            new_nodes.append(node)
            continue
        for image in images:
            sections = texts.split(f"![{image[0]}]({image[1]})", 1)
            if len(sections) != 2:
                raise ValueError("invalid markdown, image section not closed")
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], TextType.TEXT))
            new_nodes.append(TextNode(image[0], TextType.IMAGES, image[1]))
            texts = sections[1]
        if texts != "":
            new_nodes.append(TextNode(texts, TextType.TEXT))
    return new_nodes


def split_nodes_link(old_nodes: list[TextNode]) -> list[TextNode]:
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        texts = node.text
        links = extract_markdown_links(texts)
        if len(links) == 0:
            new_nodes.append(node)
            continue
        for link in links:
            sections = texts.split(f"[{link[0]}]({link[1]})", 1)
            if len(sections) != 2:
                raise ValueError("invalid markdown, link section not closed")
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], TextType.TEXT))
            new_nodes.append(TextNode(link[0], TextType.LINKS, link[1]))
            texts = sections[1]
        if texts != "":
            new_nodes.append(TextNode(texts, TextType.TEXT))
    return new_nodes

def text_to_textnodes(text):
    nodes = [TextNode(text, TextType.TEXT)]
    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    return nodes

def markdown_to_blocks(markdown):
    block_strings = []
    block_level = markdown.split('\n\n')
    for blocks in block_level:
        strip_blocks = blocks.strip()
        if strip_blocks != "":
            block_strings.append(strip_blocks)
    return block_strings

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
    node= markdown_to_html_node(markdown_file)
    html = node.to_html
    title = extract_title(markdown_file)
    template_content = template_content.replace("{{ Title }}", title)
    template_content = template_content.replace("{{ Content }}", html)
    destination = os.path.dirname(dest_path)
    if destination != "":
        os.markdir(destination, exist_ok=True)
    to_file = open(dest_path, "w")
    to_file.write(template_content)