


from htmlnode import HTMLNode
from textnode import TextNode, TextType, text_node_to_html_node
from extractors import extract_markdown_images, extract_markdown_links


def split_nodes_delimiter(old_nodes: list[TextNode], delimiter: str, text_type: TextType) -> list[TextNode]:
    new_nodes: list[TextNode] = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        
        tokens = old_node.text.split(delimiter)
        if len(tokens) % 2 == 0:
            raise ValueError(f'"{old_node.text}" is missing closing delimiter {delimiter}')

        for i in range(len(tokens)):
            if not tokens[i]:
                continue
            if i % 2 == 0:
                new_node = TextNode(tokens[i], TextType.TEXT)
            else:
                new_node = TextNode(tokens[i], text_type)
            new_nodes.append(new_node)
    return new_nodes

def split_nodes_image(old_nodes: list[TextNode]) -> list[TextNode]:
    new_nodes = []
    for old_node in old_nodes:
        links = extract_markdown_images(old_node.text)
        if old_node.text_type != TextType.TEXT or not links:
            new_nodes.append(old_node)
            continue
        text = old_node.text
        for name, url in links:
            tokens = text.split(f'![{name}]({url})', 1)
            if tokens[0]:
                new_nodes.append(TextNode(tokens[0], TextType.TEXT))
            new_nodes.append(TextNode(name, TextType.IMAGE, url))
            text = tokens[1]
        if text:
            new_nodes.append(TextNode(text, TextType.TEXT))
    return new_nodes


def split_nodes_link(old_nodes: list[TextNode]) -> list[TextNode]:
    new_nodes = []
    for old_node in old_nodes:
        links = extract_markdown_links(old_node.text)
        if old_node.text_type != TextType.TEXT or not links:
            new_nodes.append(old_node)
            continue
        text = old_node.text
        for name, url in links:
            tokens = text.split(f'[{name}]({url})', 1)
            if tokens[0]:
                new_nodes.append(TextNode(tokens[0], TextType.TEXT))
            new_nodes.append(TextNode(name, TextType.LINK, url))
            text = tokens[1]
        if text:
            new_nodes.append(TextNode(text, TextType.TEXT))
    return new_nodes