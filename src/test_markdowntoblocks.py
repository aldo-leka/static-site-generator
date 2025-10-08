import unittest

from markdowntoblocks import markdown_to_blocks, block_to_block_type, BlockType


class TestMarkdownToBlocks(unittest.TestCase):
    def test_markdowntoblocks1(self):
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

    def test_block_to_block_type1(self):
        self.assertEqual(block_to_block_type("###### "), BlockType.HEADING)

    def test_block_to_block_type2(self):
        self.assertEqual(block_to_block_type("####### "), BlockType.PARAGRAPH)

    def test_block_to_block_type3(self):
        self.assertEqual(block_to_block_type("# "), BlockType.HEADING)

    def test_block_to_block_type4(self):
        self.assertEqual(block_to_block_type("```test```"), BlockType.CODE)

    def test_block_to_block_type5(self):
        self.assertEqual(block_to_block_type("`````"), BlockType.PARAGRAPH)

    def test_block_to_block_type6(self):
        self.assertEqual(block_to_block_type(">\n>\n>"), BlockType.QUOTE)

    def test_block_to_block_type7(self):
        self.assertEqual(block_to_block_type(">\n>\n"), BlockType.PARAGRAPH)

    def test_block_to_block_type8(self):
        self.assertEqual(block_to_block_type("- \n- \n- "), BlockType.UNORDERED_LIST)

    def test_block_to_block_type9(self):
        self.assertEqual(block_to_block_type("\n- \n- "), BlockType.PARAGRAPH)

    def test_block_to_block_type10(self):
        self.assertEqual(block_to_block_type("1. \n2. \n3. "), BlockType.ORDERED_LIST)

    def test_block_to_block_type11(self):
        self.assertEqual(block_to_block_type("2. \n2. \n3. "), BlockType.PARAGRAPH)