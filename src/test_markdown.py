import unittest
from inline_markdown import extract_markdown_images, extract_markdown_links

class TestExtractions(unittest.TestCase):
    def test_extract_markdown_images(self):
        matches = extract_markdown_images("This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)")
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_markdown_link(self):
        matches = extract_markdown_links("This is text with a [link](https://www.youtube.com)")
        self.assertListEqual([("link", "https://www.youtube.com")], matches)

    def test_markdown_links(self):
        matches = extract_markdown_links("This is text with a [link](https://www.youtube.com) and [another link](https://github.com/JRPOGM/PokePoems-library)")
        self.assertListEqual([("link", "https://www.youtube.com"), ("another  link", "https://github.com/JRPOGM/PokePoems-library")], matches)
