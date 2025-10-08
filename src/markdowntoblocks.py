from enum import Enum

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    for i in range(0, len(blocks)):
        blocks[i] = blocks[i].strip()

    return blocks

def block_to_block_type(block):
    # Heading
    for i in range(0, 6):
        hasj = "#"
        for j in range(i):
            hasj += "#"

        if block.startswith(f"{hasj} "):
            return BlockType.HEADING

    # Code
    count_backticks = 0
    for letter in block:
        if letter == "`":
            count_backticks += 1
    if block.startswith("```") and block.endswith("```") and count_backticks >= 6:
        return BlockType.CODE

    # Quote
    lines = block.split("\n")
    quote = True
    for line in lines:
        if not line.startswith(">"):
            quote = False
    if quote:
        return BlockType.QUOTE

    # Unordered List
    unordered_list = True
    for line in lines:
        if not line.startswith("- "):
            unordered_list = False
    if unordered_list:
        return BlockType.UNORDERED_LIST

    # Ordered List
    current = 1
    ordered_list = True
    for line in lines:
        if not line.startswith(f"{current}. "):
            ordered_list = False
        current += 1
    if ordered_list:
        return BlockType.ORDERED_LIST

    return BlockType.PARAGRAPH