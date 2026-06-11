import unittest
from block_types import BlockType, block_to_block_type

class TestBlockTypes(unittest.TestCase):

    def test_block_types1(self):
        doc = "This should be a paragraph"
        self.assertEqual(block_to_block_type(doc), BlockType.PARAGRAPH)

    def test_block_types2(self):
        doc = "# Adding a few headings\n## Just to make sure it works\n### As an organization"
        self.assertEqual(block_to_block_type(doc), BlockType.HEADING)

    def test_block_types3(self):
        doc = "```\nThis should be simple enough\n```"
        self.assertEqual(block_to_block_type(doc), BlockType.CODE)

    def test_block_types4(self):
        doc = "- Adding an unordered list\n- Hopefully this doesn't mess something else up\n- This should be enough\n- I think I'll add another one"
        self.assertEqual(block_to_block_type(doc), BlockType.UNORDERED_LIST)

    def test_block_types5(self):
        doc = "1. Now let's see how ordering goes\n2. I don't feel the course about this showed enough\n3. This is a cry for help"
        self.assertEqual(block_to_block_type(doc), BlockType.ORDERED_LIST)

    def test_block_types6(self):
        doc = "> This is how quotes work right?\n> Hey, why did the chicken cross the road?"
        self.assertEqual(block_to_block_type(doc), BlockType.QUOTE)

    def test_bad_blocks1(self):
        doc = "Now this can test how NotEqual works in this sense\nAnd I'll just put the wrong Block Types\nNothing can go wrong"
        self.assertNotEqual(block_to_block_type(doc), BlockType.QUOTE)
    
    def test_bad_blocks2(self):
        doc = "- Now I'll add some wrong items\n2. That don't match format to see how it goes"
        self.assertNotEqual(block_to_block_type(doc), BlockType.UNORDERED_LIST)

    def test_bad_blocks3(self):
        doc = "```\nThis code will be messed up"
        self.assertNotEqual(block_to_block_type(doc), BlockType.CODE)

    def test_bad_blocks4(self):
        doc = "> To get to the other side, numbnuts\nAnd if I don't add a quote mark it should mess up, right?"
        self.assertNotEqual(block_to_block_type(doc), BlockType.QUOTE)