from enum import Enum

class TextType(Enum):
    PLAIN = "text"
    BOLD = "bold_text"
    ITALIC = "italic_text"
    CODE = "code_text"
    LINK = "url_link"
    IMAGE = "url_image"

class TextNode:
    def __init__(self, text, text_type, url=None):

        self.text= text
        self.text_type = text_type
        self.url = url

    def __eq__(self,other):
        return self.text == other.text and self.text_type == other.text_type and self.url == other.url

    def __repr__(self):
        text_repr = f"TextNode({self.text},{self.text_type},{self.url})"
        return text_repr