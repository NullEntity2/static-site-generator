import unittest

from nodesplitters import split_nodes_delimiter
from textnode import TextNode, TextType


class TestSplitNodesDelimiter(unittest.TestCase):
    def test_code_block(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)

        expected = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" word", TextType.TEXT),
        ]
        self.assertSequenceEqual(new_nodes, expected)

    def test_2_code_blocks(self):
        node = TextNode("This `is text` with two `code block` words", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)

        expected = [
            TextNode("This ", TextType.TEXT),
            TextNode("is text", TextType.CODE),
            TextNode(" with two ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" words", TextType.TEXT),
        ]
        self.assertSequenceEqual(new_nodes, expected)

    def test_code_block_extra_delim(self):
        node = TextNode("This is text with two `code block words", TextType.TEXT)

        with self.assertRaises(ValueError):
            split_nodes_delimiter([node], "`", TextType.CODE)

    def test_2_code_blocks_extra_delim(self):
        node = TextNode("This `is text` with two `code block words", TextType.TEXT)

        with self.assertRaises(ValueError):
            split_nodes_delimiter([node], "`", TextType.CODE)

    def test_two_code_blocks_next_to_each_other(self):
        node = TextNode("This is text with two `code block`` words`", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)

        expected = [
            TextNode("This is text with two ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" words", TextType.CODE),
        ]
        self.assertSequenceEqual(new_nodes, expected)