import unittest

from markdowntohtml import markdown_to_html_node

class TestMarkdownToHtml(unittest.TestCase):
    def test_markdowntohtml1(self):
        md = "## some `test` this is"
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(html, "<div><h2>some <code>test</code> this is</h2></div>")

    def test_markdowntohtml2(self):
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

    def test_markdowntohtml3(self):
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

    def test_markdowntohtml4(self):
        md = """
This is **bolded** paragraph
text in a p

This is another paragraph with _italic_

```
This is text that _should_ remain
the **same** even with inline stuff
```
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p</p><p>This is another paragraph with <i>italic</i></p><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )