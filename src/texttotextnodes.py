from splitnodes import split_nodes_delimiter, split_nodes_image, split_nodes_link
from textnode import TextNode, TextType


def text_to_textnodes(text):
    node = TextNode(text, TextType.PLAIN_TEXT)
    bold = split_nodes_delimiter([node], "**", TextType.BOLD_TEXT)
    italic = split_nodes_delimiter(bold, "_", TextType.ITALIC_TEXT)
    code = split_nodes_delimiter(italic, "`", TextType.CODE_TEXT)
    image = split_nodes_image(code)
    return split_nodes_link(image)