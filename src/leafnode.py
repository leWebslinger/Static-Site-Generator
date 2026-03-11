from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag=tag, value=value, children=None, props=props)
    def to_html(self):
        if self.value is None:
            raise ValueError
        elif self.tag is None or self.tag =="":
            return self.value
        else:
            result= f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

            return result
    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"


