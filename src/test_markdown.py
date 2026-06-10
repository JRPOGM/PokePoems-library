import unittest
from textnode import TextNode, TextType
from inline_markdown import extract_markdown_images, extract_markdown_links, split_nodes_image, split_nodes_link, text_to_textnodes

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

    def test_split_link_single(self):
        node = TextNode("[link](https://boot.dev)", TextType.TEXT)
        new_nodes = split_nodes_link([node])
        self.assertListEqual([TextNode("link", TextType.LINKS, "https://boot.dev")], new_nodes)

    def test_text_to_textnodes(self):
        nodes = text_to_textnodes("This is **text** with an _italic_ word and a `code block` and an ![image](https://i.imgur.com/zjjcJKZ.png) and a [link](https://boot.dev)")
        self.assertListEqual([TextNode("This is ", TextType.TEXT), TextNode("text", TextType.BOLD), TextNode(" with an ", TextType.TEXT), TextNode("italic", TextType.ITALIC), TextNode(" word and a ", TextType.TEXT), TextNode("code block", TextType.CODE), TextNode(" and an ", TextType.TEXT), TextNode("image", TextType.IMAGES, "https://i.imgur.com/zjjcJKZ.png"), TextNode(" and a ", TextType.TEXT), TextNode("link", TextType.LINKS, "https://boot.dev")], nodes)

    def test_text_to_textnodes2(self):
        nodes = text_to_textnodes("This is _text_ with only **words**")
        self.assertListEqual([TextNode("This is ", TextType.TEXT), TextNode("text", TextType.ITALIC), TextNode(" with only ", TextType.TEXT), TextNode("words", TextType.BOLD)], nodes)


    def test_text_to_textnodes3(self):
        nodes = text_to_textnodes("This is more **text** with a [link](https://boot.dev) and some normal `codes`")
        self.assertListEqual([TextNode("This is more ", TextType.TEXT), TextNode("text", TextType.BOLD), TextNode(" with a ", TextType.TEXT), TextNode("link", TextType.LINKS, "https://boot.dev"), TextNode(" and some normal ", TextType.Text), TextNode("codes", TextType.CODE)], nodes)


    def test_text_to_textnodes4(self):
        nodes = text_to_textnodes("This is test with an ![image](https://i.imgur.com/zjjcJKZ.png) and **absolutely nothing else**")
        self.assertListEqual([TextNode("This is test with an ", TextType.TEXT), TextNode("image", TextType.IMAGES, "https://i.imgur.com/zjjcJKZ.png"), TextNode(" and ", TextType.TEXT), TextNode("absolutely nothing else", TextType.BOLD)], nodes)


if __name__ == "__main__":
    unittest.main()