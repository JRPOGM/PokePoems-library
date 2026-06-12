import unittest
from textnode import TextNode, TextType
from inline_markdown import extract_markdown_images, markdown_to_blocks, extract_markdown_links, split_nodes_image, split_nodes_link, text_to_textnodes

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
        self.assertListEqual([TextNode("This is more ", TextType.TEXT), TextNode("text", TextType.BOLD), TextNode(" with a ", TextType.TEXT), TextNode("link", TextType.LINKS, "https://boot.dev"), TextNode(" and some normal ", TextType.TEXT), TextNode("codes", TextType.CODE)], nodes)


    def test_text_to_textnodes4(self):
        nodes = text_to_textnodes("This is test with an ![image](https://i.imgur.com/zjjcJKZ.png) and **absolutely nothing else**")
        self.assertListEqual([TextNode("This is test with an ", TextType.TEXT), TextNode("image", TextType.IMAGES, "https://i.imgur.com/zjjcJKZ.png"), TextNode(" and ", TextType.TEXT), TextNode("absolutely nothing else", TextType.BOLD)], nodes)

    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_mark_to_blocks_2(self):
        md = """
_This text is italic_

This is a paragraph with a **bold** word choice
This text has a `code block` inside it
And this is just normal text

- But I'm making a list
- And checking it twice
- But it's June so no this doesn't rhyme
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "_This text is italic_",
                "This is a paragraph with a **bold** word choice\nThis text has a `code block` inside it\nAnd this is just normal text",
                "- But I'm making a list\n- And checking it twice\n- But it's June so no this doesn't rhyme",   
            ],
        )

    def test_mark_to_blocks_3(self):
        md = """
I can write a few paragraphs, I don't see why that's a problem
It's a lot of code but so long as I understand this format it should be okay
Do you see a problem with it, **random parasite** on my shoulder?

I realize now you can't see who I'm talking to
But you will be thinking about a tiny worm whose head is a larger diameter than its tail
But that's also how I think biology works so _it's not like that's a gacha_

1. I'm going to rewrite biology
2. I'm going to talk to Frankenstein
3. You'll believe every word I say
"""
        blocks = markdown_to_blocks(md)
        self.assertNotEqual(
            blocks,
            [
                "This is mostly a test to see what I can get away with\nWhat are you gonna do, shoot me?\nDon't actually do that please",
                "I just need to make more tests of not equals\nSee what makes them different from one another\nI just don't get it all that well",
                "1. I'm submitting a formal complaint\n2. I don't care\n3. This is it",
            ],
        )

if __name__ == "__main__":
    unittest.main()