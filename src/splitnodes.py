from extractmarkdown import extract_markdown_images, extract_markdown_links
from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type == TextType.PLAIN_TEXT:
            segments = old_node.text.split(delimiter)
            if len(segments) % 2 == 0:
                raise Exception("Invalid markdown")

            current_group = []
            is_text_type_element = False
            for segment in segments:
                if is_text_type_element:
                    current_group.append(TextNode(segment, text_type))
                elif len(segment) > 0:
                    current_group.append(TextNode(segment, TextType.PLAIN_TEXT))
                is_text_type_element = not is_text_type_element

            new_nodes.extend(current_group)
        else:
            new_nodes.append(old_node)
    return new_nodes

def split_nodes_image(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type == TextType.PLAIN_TEXT:
            matches = extract_markdown_images(old_node.text)
            if len(matches) > 0:
                remaining_text = old_node.text
                for (image_alt, image_link) in matches:
                    sections = remaining_text.split(f"![{image_alt}]({image_link})", 1)
                    if sections[0]:
                        new_nodes.append(TextNode(sections[0], TextType.PLAIN_TEXT))
                    new_nodes.append(TextNode(image_alt, TextType.IMAGE_TEXT, image_link))
                    remaining_text = sections[1]
                if remaining_text:
                    new_nodes.append(TextNode(remaining_text, TextType.PLAIN_TEXT))
            else:
                new_nodes.append(old_node)
        else:
            new_nodes.append(old_node)
    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type == TextType.PLAIN_TEXT:
            matches = extract_markdown_links(old_node.text)
            if len(matches) > 0:
                remaining_text = old_node.text
                for (link_text, link) in matches:
                    sections = remaining_text.split(f"[{link_text}]({link})", 1)
                    if sections[0]:
                        new_nodes.append(TextNode(sections[0], TextType.PLAIN_TEXT))
                    new_nodes.append(TextNode(link_text, TextType.LINK_TEXT, link))
                    remaining_text = sections[1]
                if remaining_text:
                    new_nodes.append(TextNode(remaining_text, TextType.PLAIN_TEXT))
            else:
                new_nodes.append(old_node)
        else:
            new_nodes.append(old_node)
    return new_nodes