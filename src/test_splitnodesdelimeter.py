import unittest

from splitnodesdelimeter import split_nodes_delimiter
from textnode import TextNode, TextType

class TestSplitNodesDelimeter(unittest.TestCase):
    def test_split_nodes1(self):
        node = TextNode("This is text with a `code block` word", TextType.PLAIN_TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE_TEXT)
        self.assertEqual(new_nodes, [
            TextNode("This is text with a ", TextType.PLAIN_TEXT),
            TextNode("code block", TextType.CODE_TEXT),
            TextNode(" word", TextType.PLAIN_TEXT),
        ])

    def test_split_nodes2(self):
        node = TextNode("`code block`", TextType.PLAIN_TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE_TEXT)
        self.assertEqual(new_nodes, [
            TextNode("code block", TextType.CODE_TEXT)
        ])

    def test_split_nodes3(self):
        node = TextNode("what `` happens ``now?", TextType.PLAIN_TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE_TEXT)
        self.assertEqual(new_nodes, [
            TextNode("what ", TextType.PLAIN_TEXT),
            TextNode("", TextType.CODE_TEXT),
            TextNode(" happens ", TextType.PLAIN_TEXT),
            TextNode("", TextType.CODE_TEXT),
            TextNode("now?", TextType.PLAIN_TEXT)
        ])

    def test_split_nodes_4(self):
        node = TextNode("what `` happens `now?", TextType.PLAIN_TEXT)
        with self.assertRaises(Exception):
            split_nodes_delimiter([node], "`", TextType.CODE_TEXT)

    def test_split_nodes5(self):
        node = TextNode("__", TextType.PLAIN_TEXT)
        new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC_TEXT)
        self.assertEqual(new_nodes, [
            TextNode("", TextType.ITALIC_TEXT)
        ])

    def test_split_nodes6(self):
        node = TextNode("____", TextType.PLAIN_TEXT)
        node2 = TextNode("Hello _some italic text_ there!", TextType.PLAIN_TEXT)
        new_nodes = split_nodes_delimiter([node, node2], "_", TextType.ITALIC_TEXT)
        self.assertEqual(new_nodes, [
            TextNode("", TextType.ITALIC_TEXT),
            TextNode("", TextType.ITALIC_TEXT),
            TextNode("Hello ", TextType.PLAIN_TEXT),
            TextNode("some italic text", TextType.ITALIC_TEXT),
            TextNode(" there!", TextType.PLAIN_TEXT)
        ])

    def test_split_nodes7(self):
        node = TextNode("__**bold text**__", TextType.PLAIN_TEXT)
        node2 = TextNode("Hello _some ** bold ** text_ there!", TextType.PLAIN_TEXT)
        new_nodes = split_nodes_delimiter([node, node2], "**", TextType.BOLD_TEXT)
        self.assertEqual(new_nodes, [
            TextNode("__", TextType.PLAIN_TEXT),
            TextNode("bold text", TextType.BOLD_TEXT),
            TextNode("__", TextType.PLAIN_TEXT),
            TextNode("Hello _some ", TextType.PLAIN_TEXT),
            TextNode(" bold ", TextType.BOLD_TEXT),
            TextNode(" text_ there!", TextType.PLAIN_TEXT)
        ])