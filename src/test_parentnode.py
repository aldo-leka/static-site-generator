import unittest

from parentnode import ParentNode
from leafnode import LeafNode

class TestParentNode(unittest.TestCase):
    def test_to_html(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )

        html = node.to_html()
        self.assertEqual(html, "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>")

    def test_to_html2(self):
        node = ParentNode(
            "p",
            [
                ParentNode(
                    "p",
                    [LeafNode("b", "Bold text"),
                    LeafNode(None, "Normal text"),
                    LeafNode("i", "italic text"),
                    LeafNode(None, "Normal text")
                ]),
            ],
        )

        html = node.to_html()
        self.assertEqual(html, "<p><p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p></p>")

    def test_to_html3(self):
        node = ParentNode(
            "p",
            [
                ParentNode(
                    "p",
                    [LeafNode("b", "Bold text"),
                     LeafNode(None, "Normal text"),
                     LeafNode("i", "italic text"),
                     LeafNode(None, "Normal text")
                     ]),
                ParentNode(
                    "p",
                    [LeafNode("b", "Bold text"),
                     LeafNode(None, "Normal text"),
                     LeafNode("i", "italic text"),
                     LeafNode(None, "Normal text")
                     ]),
            ],
        )

        html = node.to_html()
        self.assertEqual(html, "<p><p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p><p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p></p>")

def test_to_html_with_children(self):
    child_node = LeafNode("span", "child")
    parent_node = ParentNode("div", [child_node])
    self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

def test_to_html_with_grandchildren(self):
    grandchild_node = LeafNode("b", "grandchild")
    child_node = ParentNode("span", [grandchild_node])
    parent_node = ParentNode("div", [child_node])
    self.assertEqual(
        parent_node.to_html(),
        "<div><span><b>grandchild</b></span></div>",
    )