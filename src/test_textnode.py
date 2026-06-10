import unittest
from textnode import TextType, TextNode, text_node_to_html_node, split_nodes_delimiter

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_eq(self):
        node = TextNode("This is a text node", TextType.ITALIC)
        node2 = TextNode("This is a text node", TextType.ITALIC)
        self.assertEqual(node, node2)

    def test_eq(self):
        node = TextNode("This is a text node", TextType.TEXT)
        node2 = TextNode("This is a text node", TextType.TEXT)
        self.assertEqual(node, node2)

    def test_uneq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.ITALIC)
        self.assertNotEqual(node, node2)

    def test_uneq(self):
        node = TextNode("This is a text node", TextType.TEXT)
        node2 = TextNode("This is a text node", TextType.ITALIC)
        self.assertNotEqual(node, node2)

    def test_uneq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.TEXT)
        self.assertNotEqual(node, node2)

    def test_eq(self):
        node = TextNode("This is a text node", TextType.TEXT, "http://www.boot.dev")
        node2 = TextNode("This is a text node", TextType.TEXT, "http://www.boot.dev")
        self.assertEqual(node, node2)
    
    def test_repr(self):
        node = TextNode("This is some anchor text", TextType.LINKS, "https://www.boot.dev")
        self.assertEqual("TextNode(This is some anchor text, link, http://www.boot.dev)", repr(node))

    def test_repr(self):
        node = TextNode("This is some nice text", TextType.CODE, "https://www.boot.dev")
        self.assertEqual("TextNode(This is some nice text, code, http://www.boot.dev)", repr(node))

    def test_repr(self):
        node = TextNode("This is some anchor text", TextType.IMAGES, "https://www.boot.dev")
        self.assertNotEqual("TextNode(This is some nice text, text, http://www.boot.dev)", repr(node))

    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_text_two(self):
        node = TextNode("This is not a text node", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is not a text node")

    def test_text_three(self):
        node = TextNode("This is some text", TextType.ITALIC)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.value, "This is some text")

    def test_delim_bold(self):
        node = TextNode("This is text with a **bolded** word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertListEqual([TextNode("This is text with a ", TextType.TEXT), TextNode("bolded", TextType.BOLD), TextNode(" word", TextType.TEXT),], new_nodes)

    def test_delim_italic(self):
        node = TextNode("This is text with an _italic_ word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC)
        self.assertListEqual([TextNode("This is text with an ", TextType.TEXT), TextNode("italic", TextType.ITALIC), TextNode(" word", TextType.TEXT),], new_nodes)

    def test_delim_bold(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertListEqual([TextNode("This is text with a ", TextType.TEXT), TextNode("code block", TextType.CODE), TextNode(" word", TextType.TEXT),], new_nodes)

    def test_delim_bold_and_italic(self):
        node = TextNode("This is text with a **bold** and _italic_ word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        new_nodes = split_nodes_delimiter(new_nodes, "_", TextType.ITALIC)
        self.assertListEqual([TextNode("This is text with a ", TextType.TEXT), TextNode("bold", TextType.BOLD), TextNode(" and ", TextType.TEXT), TextNode("italic", TextType.ITALIC), TextNode(" word", TextType.TEXT),], new_nodes)

if __name__ == "__main__":
    unittest.main()
