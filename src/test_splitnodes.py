import unittest

from splitnodes import split_nodes_delimiter, split_nodes_image, split_nodes_link
from textnode import TextNode, TextType

class TestSplitNodes(unittest.TestCase):
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

    def test_split_nodes8(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.PLAIN_TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.PLAIN_TEXT),
                TextNode("image", TextType.IMAGE_TEXT, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.PLAIN_TEXT),
                TextNode(
                    "second image", TextType.IMAGE_TEXT, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )

    def test_split_nodes9(self):
        node = TextNode(
            " ![image](https://i.imgur.com/zjjcJKZ.png))",
            TextType.PLAIN_TEXT,
        )
        node2 = TextNode("![image](https://i.imgur.com/zjjcJKZ.png) ", TextType.PLAIN_TEXT)
        new_nodes = split_nodes_image([node, node2])
        self.assertListEqual(
            [
                TextNode(" ", TextType.PLAIN_TEXT),
                TextNode("image", TextType.IMAGE_TEXT, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(")", TextType.PLAIN_TEXT),
                TextNode("image", TextType.IMAGE_TEXT, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" ", TextType.PLAIN_TEXT),
            ],
            new_nodes,
        )

    def test_split_nodes10(self):
        node = TextNode(
            "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
            TextType.PLAIN_TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with a link ", TextType.PLAIN_TEXT),
                TextNode("to boot dev", TextType.LINK_TEXT, "https://www.boot.dev"),
                TextNode(" and ", TextType.PLAIN_TEXT),
                TextNode(
                    "to youtube", TextType.LINK_TEXT, "https://www.youtube.com/@bootdotdev"
                ),
            ],
            new_nodes,
        )