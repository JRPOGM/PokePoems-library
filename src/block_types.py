from enum import Enum
from htmlnode import HTMLNode, ParentNode
from inline_markdown import text_to_textnodes, markdown_to_blocks
from textnode import text_node_to_html_node, TextNode, TextType

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

def block_to_block_type(block):
    lines = block.split("\n")
    if block.startswith(("# ", "## ", "### ", "#### ", "##### ", "###### ")):
        return BlockType.HEADING
    if block.startswith("```") and block.endswith("```"):
        return BlockType.CODE
    if lines[0].startswith("> "):
        for line in lines:
            if not line.startswith("> "):
                return BlockType.PARAGRAPH
        return BlockType.QUOTE
    if lines[0].startswith("- "):
        for line in lines:
            if not line.startswith("- "):
                return BlockType.PARAGRAPH
        return BlockType.UNORDERED_LIST
    i = 1
    if lines[0].startswith(f"1. "):
        for line in lines:
            if not line.startswith(f"{i}. "):
                return BlockType.PARAGRAPH
            i += 1
        return BlockType.ORDERED_LIST
    return BlockType.PARAGRAPH

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    child = []
    for block in blocks:
        html = block_type_declaration(block)
        child.append(html)
    return ParentNode("div", child, None)

def text_to_child(text):
    texts = text_to_textnodes(text)
    children = []
    for node in texts:
        html = text_node_to_html_node(node)
        children.append(html)
    return children

def paragraph_correction(block):
    line = block.split("\n")
    paragraph = " ".join(line)
    child = text_to_child(paragraph)
    return ParentNode("p", child)

def heading_correction(block):
    line = 0
    for start in block:
        if start == "#":
            line += 1
        else:
            break
    if line + 1 >= len(block):
        raise ValueError(f"Wrong heading: {line}")
    text = block[line + 1 :]
    child = text_to_child(text)
    return ParentNode(f"h{line}", child)

def code_correction(block):
    if not block.startswith("```") or not block.endswith("```"):
        raise ValueError("Not a code block")
    text = block[4:-3]
    text_node = TextNode(text, TextType.TEXT)
    child = text_node_to_html_node(text_node)
    code = ParentNode("code", [child])
    return ParentNode("pre", [code])

def ordered_correction(block):
    lines = block.split("\n")
    html = []
    for line in lines:
        part = line.split(". ", 1)
        text = part[1]
        child = text_to_child(text)
        html.append(ParentNode("li", child))
    return ParentNode("ol", html)

def unordered_correction(block):
    lines = block.split("\n")
    html = []
    for line in lines:
        text = line[2:]
        child = text_to_child(text)
        html.append(ParentNode("li", child))
    return ParentNode("ul", html)

def quote_correction(block):
    lines = block.split("\n")
    new_lines = []
    for line in lines:
        if not line.startswith("> "):
            raise ValueError("Not a quote buddy")
        new_lines.append(line.lstrip("> ").strip())
    content = " ".join(new_lines)
    child = text_to_child(content)
    return ParentNode("blockquote", child)

def block_type_declaration(block):
    block_type = block_to_block_type(block)
    if block_type == BlockType.PARAGRAPH:
        return paragraph_correction(block)
    if block_type == BlockType.HEADING:
        return heading_correction(block)
    if block_type == BlockType.CODE:
        return code_correction(block)
    if block_type == BlockType.QUOTE:
        return quote_correction(block)
    if block_type == BlockType.UNORDERED_LIST:
        return unordered_correction(block)
    if block_type == BlockType.ORDERED_LIST:
        return ordered_correction(block)
    raise ValueError("Not a block type")