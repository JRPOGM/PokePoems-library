import unittest
from textnode import TextNode, TextType
from inline_markdown import extract_markdown_images, extract_markdown_links, split_nodes_image, split_nodes_link

class TestExtractions(unittest.TestCase):
    def test_extract_markdown_images(self):
        matches = extract_markdown_images("This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)")
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_markdown_link(self):
        matches = extract_markdown_links("This is text with a [link](https://www.youtube.com)")
        self.assertListEqual([("link", "https://www.youtube.com")], matches)

    def test_markdown_links(self):
        matches = extract_markdown_links("This is text with a [link](https://www.youtube.com) and [another link](https://github.com/JRPOGM/PokePoems-library)")
        self.assertListEqual([("link", "https://www.youtube.com"), ("another link", "https://github.com/JRPOGM/PokePoems-library")], matches)

    def test_split_images(self):
        node = TextNode("This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)", TextType.TEXT)
        new_nodes = split_nodes_image([node])
        self.assertListEqual([TextNode("This is text with an ", TextType.TEXT), TextNode("image", TextType.IMAGES, "https://i.imgur.com/zjjcJKZ.png")], new_nodes)

    def test_split_links(self):
        node = TextNode("This is text with a [link](https://boot.dev)", TextType.TEXT)
        new_nodes = split_nodes_link([node])
        self.assertListEqual([TextNode("This is text with a ", TextType.TEXT), TextNode("link", TextType.LINKS, "https://boot.dev")], new_nodes)

    def test_split_image_single(self):
        node = TextNode("![image](https://www.example.COM/IMAGE.PNG)", TextType.TEXT)
        new_nodes = split_nodes_image([node])
        self.assertListEqual([TextNode("image", TextType.IMAGES, "https://www.example.COM/IMAGE.PNG")], new_nodes)

if __name__ == "__main__":
    unittest.main()