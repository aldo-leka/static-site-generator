import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD_TEXT)
        node2 = TextNode("This is a text node", TextType.BOLD_TEXT)
        self.assertEqual(node, node2)

    def test_ne_by_text(self):
        node = TextNode("This is a text node", TextType.BOLD_TEXT)
        node2 = TextNode("This is a text node #2", TextType.BOLD_TEXT)
        self.assertNotEqual(node, node2)

    def test_ne_by_texttype(self):
        node = TextNode("This is a text node", TextType.BOLD_TEXT)
        node2 = TextNode("This is a text node", TextType.PLAIN_TEXT)
        self.assertNotEqual(node, node2)

    def test_eq_repr(self):
        node = TextNode("This is a text node", TextType.BOLD_TEXT)
        self.assertEqual(node.__repr__(), "TextNode(This is a text node, bold, None)")

    def test_to_html_node_plain(self):
        node = TextNode("This is a text node", TextType.PLAIN_TEXT)
        html_node = node.to_html_node()
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_to_html_node_bold(self):
        node = TextNode("This is a bold node", TextType.BOLD_TEXT)
        html_node = node.to_html_node()
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is a bold node")

    def test_to_html_node_italic(self):
        node = TextNode("This is a italic node", TextType.ITALIC_TEXT)
        html_node = node.to_html_node()
        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.value, "This is a italic node")

    def test_to_html_node_link(self):
        node = TextNode("This is a link node", TextType.LINK_TEXT, "https://google.com")
        html_node = node.to_html_node()
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "This is a link node")
        self.assertEqual(html_node.props["href"], "https://google.com")

    def test_to_html_node_image(self):
        node = TextNode("This is an image node", TextType.IMAGE_TEXT, "https://google.com")
        html_node = node.to_html_node()
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(html_node.props["src"], "https://google.com")
        self.assertEqual(html_node.props["alt"], "This is an image node")

    def test_to_html_node_unknown(self):
        node = TextNode("This is an unknown node", "unknown")
        with self.assertRaises(Exception):
            node.to_html_node()