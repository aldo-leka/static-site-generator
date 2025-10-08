from src.textnode import TextNode
from textnode import TextType


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