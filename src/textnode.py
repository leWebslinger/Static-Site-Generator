from enum import Enum

class TextType(Enum):
    PLAIN_TEXT = "text"
    BOLD_TEXT = "bold_text"
    ITALIC_TEXT = "italic_text"
    CODE_TEXT = "code_text"
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