from blocktype import BlockType, block_to_block_type
from htmlnode import HTMLNode
from markdowntoblocks import markdown_to_blocks
from parentnode import ParentNode
from textnode import TextNode, TextType, text_node_to_html_node
from texttotextnodes import text_to_textnodes


def text_to_children(text: str) -> list[HTMLNode]:
    return [text_node_to_html_node(node) for node in text_to_textnodes(text)]

def paragraph_to_htmlnode(block: str) -> HTMLNode:
    block = " ".join(block.splitlines())
    return ParentNode("p", text_to_children(block))

def heading_to_htmlnode(block: str) -> HTMLNode:
    level = len(block) - len(block.lstrip("#"))
    text = block[level + 1:]
    return ParentNode(f"h{level}", text_to_children(text))

def code_to_htmlnode(block: str) -> HTMLNode:
    text = block[4:-3]
    # don't parse children of code blocks
    code = text_node_to_html_node(TextNode(text, TextType.CODE))
    return ParentNode("pre", [code])

def quote_to_htmlnode(block: str) -> HTMLNode:
    lines = [line.lstrip(">").strip() for line in block.splitlines()]
    return ParentNode("blockquote", text_to_children(" ".join(lines)))

def unordered_list_to_htmlnode(block: str) -> HTMLNode:
    items: list[HTMLNode] = [ParentNode("li", text_to_children(line[2:])) for line in block.splitlines()]
    return ParentNode("ul", items)

def ordered_list_to_htmlnode(block: str) -> HTMLNode:
    items: list[HTMLNode] = [ParentNode("li", text_to_children(line.split(". ", 1)[1])) for line in block.splitlines()]
    return ParentNode("ol", items)

def markdown_to_html_node(markdown: str) -> HTMLNode:
    blocks = markdown_to_blocks(markdown)
    children: list[HTMLNode] = []
    for block in blocks:
        block_type = block_to_block_type(block)
        match block_type:
            case BlockType.PARAGRAPH:
                children.append(paragraph_to_htmlnode(block))
            case BlockType.HEADING:
                children.append(heading_to_htmlnode(block))
            case BlockType.CODE:
                children.append(code_to_htmlnode(block))
            case BlockType.QUOTE:
                children.append(quote_to_htmlnode(block))
            case BlockType.UNORDERED_LIST:
                children.append(unordered_list_to_htmlnode(block))
            case BlockType.ORDERED_LIST:
                children.append(ordered_list_to_htmlnode(block))
    return ParentNode("div", children)
