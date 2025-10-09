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
                nodes.append(ParentNode("p", text_to_children(" ".join(block.split("\n")))))
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
                parts = block.split("\n")
                for i in range(len(parts)):
                    parts[i] = f"<p>{parts[i][1:]}</p>"
                nodes.append(ParentNode("blockquote", text_to_children("\n".join(parts))))
            case BlockType.UNORDERED_LIST:
                lines = block.split("\n")
                list_items = []
                for i in range(len(lines)):
                    list_items.append(ParentNode("li", text_to_children(lines[i][2:])))
                nodes.append(ParentNode("ul", list_items))
            case BlockType.ORDERED_LIST:
                lines = block.split("\n")
                list_items = []
                for i in range(len(lines)):
                    list_items.append(ParentNode("li", text_to_children(lines[i][3:])))
                nodes.append(ParentNode("ol", list_items))

    return ParentNode("div", nodes)

def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    children = []
    for text_node in text_nodes:
        children.append(text_node.to_html_node())

    return children