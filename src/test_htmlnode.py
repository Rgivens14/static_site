import unittest
# Assuming HTMLNode is inside a file named htmlnode.py in the same src directory
from htmlnode import HTMLNode, LeafNode, ParentNode

class TestHTMLNode(unittest.TestCase):

    def test_props_to_html_with_multiple_props(self):
        # Test 1: Verifies that multiple properties are formatted correctly with spaces
        node = HTMLNode(
            tag="a", 
            props={"href": "https://www.google.com", "target": "_blank"}
        )
        self.assertEqual(
            node.props_to_html(), 
            ' href="https://www.google.com" target="_blank"'
        )

    def test_props_to_html_empty(self):
        # Test 2: Verifies that if props is None or empty, it returns an empty string
        node_none = HTMLNode(tag="p", props=None)
        node_empty = HTMLNode(tag="p", props={})
        
        self.assertEqual(node_none.props_to_html(), "")
        self.assertEqual(node_empty.props_to_html(), "")

    def test_props_to_html_single_prop(self):
        # Test 3: Verifies behavior with a single attribute
        node = HTMLNode(tag="img", props={"src": "cat.jpg"})
        self.assertEqual(node.props_to_html(), ' src="cat.jpg"')

    def test_repr(self):
        # Test 4: (Bonus) Ensures the __repr__ method outputs a proper string representation
        node = HTMLNode(tag="div", value="Hello", props={"class": "container"})
        expected_repr = "HTMLNode(div, Hello, children: None, {'class': 'container'})"
        self.assertEqual(repr(node), expected_repr)

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(
            node.to_html(),
            '<a href="https://www.google.com">Click me!</a>',
        )

    def test_leaf_to_html_no_tag(self):
        node = LeafNode(None, "Hello, world!")
        self.assertEqual(node.to_html(), "Hello, world!")

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_many_children(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>",
        )

    def test_headings(self):
        node = ParentNode(
            "h2",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<h2><b>Bold text</b>Normal text<i>italic text</i>Normal text</h2>",
        )

if __name__ == "__main__":
    unittest.main()