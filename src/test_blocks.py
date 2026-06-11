import unittest
from block_types import BlockType, block_to_block_type, markdown_to_html_node

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

    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_codeblock(self):
        md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )

    def test_quotes(self):
        md = """
> This is text in a quote
> This is a **bold quote**
> This is an _italic_ quote
> This is some `code`
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><blockquote>This is text in a quote This is a <b>bold quote</b> This is an <i>italic</i> quote This is some <code>code</code></blockquote></div>",
        )
    
    def test_ordered_list(self):
        md = """
1. I'm making a list again
2. But I don't have to check it twice
3. This is where I complete me joke from earlier
4. To get to the other side
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ol><li>I'm making a list again</li><li>But I don't have to check it twice</li><li>This is where I complete me joke from earlier</li><li>To get to the other side</li></ol></div>",
        )
    
    def test_unordered_list(self):
        md = """
- This should be the same format
- I wonder why only code needs the line break
- Despite everything else having another line
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ul><li>This should be the same format</li><li>I wonder why only code needs the line break</li><li>Despite everything else having another line</li></ul></div>",
        )

    def test_headings(self):
        md = """
# How many headings can I go

## How much is too much

### Does this even work

#### Does God know what he has created

##### Is he afraid

###### Are you
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h1>How many headings can I go</h1><h2>How much is too much</h2><h3>Does this even work</h3><h4>Does God know what he has created</h4><h5>Is he afraid</h5><h6>Are you</h6></div>",
        )

if __name__ == "__main__":
    unittest.main()