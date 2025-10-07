from enum import Enum
from leafnode import LeafNode

class TextType(Enum):
    PLAIN_TEXT = "plain"
    BOLD_TEXT = "bold"
    ITALIC_TEXT = "italic"
    CODE_TEXT = "code"
    LINK_TEXT = "link"
    IMAGE_TEXT = "image"

class TextNode:
    def __init__(self, text, text_type, url = None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        return self.text == other.text and self.text_type == other.text_type and self.url == other.url

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"

    def to_html_node(self):
        match self.text_type:
            case TextType.PLAIN_TEXT:
                return LeafNode(None, self.text)
            case TextType.BOLD_TEXT:
                return LeafNode("b", self.text)
            case TextType.ITALIC_TEXT:
                return LeafNode("i", self.text)
            case TextType.CODE_TEXT:
                return LeafNode("code", self.text)
            case TextType.LINK_TEXT:
                return LeafNode("a", self.text, {"href": self.url})
            case TextType.IMAGE_TEXT:
                return LeafNode("img", "", {"src": self.url, "alt": self.text})
            case _:
                raise Exception(f"Unknown TextType: {self.text_type}")