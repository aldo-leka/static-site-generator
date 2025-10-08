def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    for i in range(0, len(blocks)):
        blocks[i] = blocks[i].strip()

    return blocks