import unittest

from htmlnode import HtmlNode

class TestHtmlNode(unittest.TestCase):
    def test_to_html_raise_ex(self):
        with self.assertRaises(NotImplementedError):
            HtmlNode().to_html()

    def test_props_to_html(self):
        node = HtmlNode(props={"href": "https://www.aldoleka.com", "target": "_blank"})
        self.assertEqual(node.props_to_html(), ' href="https://www.aldoleka.com" target="_blank"')

    def test_props_to_html_2(self):
        node = HtmlNode(props={"href": "https://www.aldo.al"})
        self.assertEqual(node.props_to_html(), ' href="https://www.aldo.al"')