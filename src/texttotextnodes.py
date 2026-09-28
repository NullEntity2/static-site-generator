
from functools import reduce
from typing import Callable

from nodesplitters import split_nodes_delimiter, split_nodes_image, split_nodes_link
from textnode import TextNode, TextType


def text_to_textnodes(text: str) -> list[TextNode]:
    funcs = [
        lambda x: split_nodes_delimiter(x, "**", TextType.BOLD),
        lambda x: split_nodes_delimiter(x, "_", TextType.ITALIC),
        lambda x: split_nodes_delimiter(x, "`", TextType.CODE),
        lambda x: split_nodes_image(x),
        lambda x: split_nodes_link(x),
    ]
    nodes = [TextNode(text, TextType.TEXT)]
    return reduce(lambda x, y: y(x), funcs, nodes)