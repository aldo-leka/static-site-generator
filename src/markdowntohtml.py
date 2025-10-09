from markdowntoblocks import markdown_to_blocks, block_to_block_type, BlockType
from parentnode import ParentNode
from textnode import TextNode, TextType
from texttotextnodes import text_to_textnodes


def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    nodes = []
    for block in blocks:
        match block_to_block_type(block):
            case BlockType.PARAGRAPH:
                nodes.append(ParentNode("p", text_to_children(block)))
            case BlockType.HEADING:
                h_count = 0
                for letter in block:
                    if letter != "#":
                        break
                    h_count += 1

                nodes.append(ParentNode(f"h{h_count}", text_to_children(block[h_count + 1:])))
            case BlockType.CODE:
                child = TextNode(block[3:-3].lstrip("\n"), TextType.PLAIN_TEXT).to_html_node()
                parent = ParentNode("code", [child])
                nodes.append(ParentNode("pre", [parent]))
            case BlockType.QUOTE:
                nodes.append(ParentNode("blockquote", text_to_children(block)))
            case BlockType.UNORDERED_LIST:
                parents = []
                for child in text_to_children(block):
                    parents.append(ParentNode("li", [child]))
                nodes.append(ParentNode("ul", parents))
            case BlockType.ORDERED_LIST:
                parents = []
                for child in text_to_children(block):
                    parents.append(ParentNode("li", [child]))
                nodes.append(ParentNode("ol", parents))

    return ParentNode("div", nodes)

def text_to_children(text):
    text = " ".join(text.split("\n"))
    text_nodes = text_to_textnodes(text)
    children = []
    for text_node in text_nodes:
        children.append(text_node.to_html_node())

    return children