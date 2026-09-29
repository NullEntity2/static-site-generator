import unittest
from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_empty_init(self):
        node = HTMLNode()
        self.assertEqual(node.tag, None)
        self.assertEqual(node.value, None)
        self.assertEqual(node.children, None)
        self.assertEqual(node.props, None)

    def test_all_args_init(self):
        tag = "tag"
        value = ""
        children = []
        props = {}
        node = HTMLNode(tag, value, children, props)
        self.assertEqual(node.tag, tag)
        self.assertEqual(node.value, value)
        self.assertEqual(node.children, children)
        self.assertEqual(node.props, props)

    def test_to_html_throws(self):
        node = HTMLNode()
        with self.assertRaises(NotImplementedError):
            node.to_html()

    def test_props_to_html(self):
        props = {"href": "href", "target": "target"}
        node = HTMLNode(props=props)
        self.assertEqual(node.props_to_html(), f' href="href" target="target"')

    def test_props_to_html_missing_href(self):
        props = {"target": "target"}
        node = HTMLNode(props=props)
        self.assertEqual(node.props_to_html(), "")

    def test_props_to_html_missing_target(self):
        props = {"href": "href"}
        node = HTMLNode(props=props)
        self.assertEqual(node.props_to_html(), "")

    def test_repr(self):
        tag = "tag"
        value = "value"
        children = []
        props = {}
        node = HTMLNode(tag, value, children, props)
        self.assertEqual(str(node), "HTMLNode(tag, value, [], {})")