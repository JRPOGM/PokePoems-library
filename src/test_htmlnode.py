import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode

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
        node = HTMLNode("p", "What a strange world", None, {"class": "primary"})
        self.assertEqual(node.__repr__(), "HTMLNode(p, What a strange world, children: None, {'class': 'primary'})")

    def test_repr(self):
        node = HTMLNode("p", "What a strange world", None, {"class": "primary"})
        self.assertNotEqual(node.__repr__(), "HTMLNode(six, What a funny world, children: None, {'class': 'primary'})")

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_p(self):
        node = LeafNode("a", "Goodbye cruel world")
        self.assertNotEqual(node.to_html(), "<b>Goodbye cruel world</b>")

    def test_repr(self):
        node = LeafNode("j", "What a strange little creature", {"class": "secondary"})
        self.assertEqual(node.__repr__(), "LeafNode(j, What a strange little creature, {'class': 'secondary'})")

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span><b>grandchild</b></span></div>")

    def test_to_html_with_children(self):
        child_node = LeafNode("spin", "children")
        parent_node = ParentNode("div", [child_node])
        self.assertNotEqual(parent_node.to_html(), "<div><span>child</span></div>")

if __name__ == "__main__":
    unittest.main()