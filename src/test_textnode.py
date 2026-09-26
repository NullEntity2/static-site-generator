import unittest
from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.ITALIC)
        self.assertNotEqual(node, node2)

    def test_constructor(self):
        node = TextNode("Hello", TextType.ITALIC, "test url")
        self.assertEqual(node.text, "Hello")
        self.assertEqual(node.text_type, TextType.ITALIC)
        self.assertEqual(node.url, "test url")

    def test_constructor_no_url(self):
        node = TextNode("Hello", TextType.ITALIC)
        self.assertEqual(node.text, "Hello")
        self.assertEqual(node.text_type, TextType.ITALIC)
        self.assertEqual(node.url, None)


if __name__ == "__main__":
    unittest.main()