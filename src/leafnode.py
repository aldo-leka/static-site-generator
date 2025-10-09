from htmlnode import HtmlNode


class LeafNode(HtmlNode):
    def __init__(self, tag, value, props = None):
        super().__init__(tag=tag, value=value, props=props)

    def to_html(self):
        # if not self.value:
        #     raise ValueError()
        if not self.tag:
            return self.value
        return f'<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>'