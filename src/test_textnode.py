import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
    def test_not_eq(self):
        node = TextNode("This is a text node", TextType.ITALIC)
        node2 = TextNode("This is a text node", TextType.BOLD)        
    def test_is_url_def(self):
        node = TextNode("This is a text node", TextType.ITALIC,"https://www.google.com")   
        self.assertIsNotNone(node.url)
    def test_is_url_none(self):
        node = TextNode("This is a text node", TextType.ITALIC)   
        self.assertIsNone(node.url)
    def test_text_type_equal(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)        
        self.assertIs(node.text_type,node2.text_type)
if __name__ == "__main__":
    unittest.main()