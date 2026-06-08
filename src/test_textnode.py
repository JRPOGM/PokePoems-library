import unittest
from textnode import TextType, TextNode

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

if __name__ == "__main__":
    unittest.main()
