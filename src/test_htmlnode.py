import unittest
from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_props_to_html_multiple(self):
        node = HTMLNode(tag="a", props={"href": "https://www.google.com", "target": "_blank"})
        self.assertEqual(node.props_to_html(), ' href="https://www.google.com" target="_blank"')

    def test_props_to_html_single(self):
        node = HTMLNode(tag="a", props={"href": "https://www.boot.dev"})
        self.assertEqual(node.props_to_html(), ' href="https://www.boot.dev"')

    def test_props_to_html_none(self):
        node = HTMLNode(tag="p")
        self.assertEqual(node.props_to_html(), "")

    def test_props_to_html_empty(self):
        node = HTMLNode(tag="p", props={})
        self.assertEqual(node.props_to_html(), "")

    def test_defaults_are_none(self):
        node = HTMLNode()
        self.assertIsNone(node.tag)
        self.assertIsNone(node.value)
        self.assertIsNone(node.children)
        self.assertIsNone(node.props)

    def test_values_stored(self):
        node = HTMLNode(tag="p", value="hello", children=[], props={"class": "greeting"})
        self.assertEqual(node.tag, "p")
        self.assertEqual(node.value, "hello")
        self.assertEqual(node.children, [])
        self.assertEqual(node.props, {"class": "greeting"})

    def test_to_html_raises(self):
        node = HTMLNode()
        with self.assertRaises(NotImplementedError):
            node.to_html()

    def test_repr(self):
        node = HTMLNode(tag="a", value="click", children=None, props={"href": "https://boot.dev"})
        self.assertEqual(repr(node), "HTMLNode(a, click, None, {'href': 'https://boot.dev'})")

    def test_children_stored(self):
        child1 = HTMLNode(tag="b", value="bold text")
        child2 = HTMLNode(tag="i", value="italic text")
        parent = HTMLNode(tag="p", children=[child1, child2])
        self.assertEqual(len(parent.children), 2)
        self.assertEqual(parent.children[0].tag, "b")
        self.assertEqual(parent.children[0].value, "bold text")
        self.assertEqual(parent.children[1].tag, "i")
        self.assertEqual(parent.children[1].value, "italic text")    

if __name__ == "__main__":
    unittest.main()