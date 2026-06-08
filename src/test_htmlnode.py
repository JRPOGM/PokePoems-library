import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_to_htmp_props(self):
        node = HTMLNode("div", "Hello, world!", None, {"class": "greeting", "href": "http://boot.dev"})
        self.assertEqual(node.props_to_html(), ' class="greeting" href="http://boot.dev"')

    def test_value(self):
        node = HTMLNode("div", "I wish I could read")
        self.assertEqual(node.tag, "div")
        self.assertEqual(node.value, "I wish I could read")
        self.assertEqual(node.children, None)
        self.assertEqual(node.props, None)

    def test_value(self):
        node = HTMLNode("power", "See what we can")
        self.assertNotEqual(node.tag, "strength")
        self.assertNotEqual(node.value, "I know where I am")
        self.assertEqual(node.children, None)
        self.assertEqual(node.props, None)

    def test_repr(self):
        node = HTMLNode("p", "What a strange world", None,  {"class": "primary"})
        self.assertEqual(node.__repr__(), "HTMLNode(p, What a strange world, children: None, {'class': 'primary'})")

if __name__ == "__main__":
    unittest.main()