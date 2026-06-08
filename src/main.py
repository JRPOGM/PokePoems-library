from textnode import TextNode, TextType

def main():
    node = TextNode("This is some anchor text", TextType.LINKS, "https://www.boot.dev")
    print(node)

main()
