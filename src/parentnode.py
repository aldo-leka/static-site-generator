from htmlnode import HtmlNode


class ParentNode(HtmlNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag=tag, children=children, props=props)

    def to_html(self):
        if not self.tag:
            raise ValueError("no tag")
        if not self.children:
            raise ValueError("no children")
        repr = f"<{self.tag}>"
        for child in self.children:
            repr += child.to_html()
        repr += f"</{self.tag}>"

        return repr