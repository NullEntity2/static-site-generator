


from textnode import TextNode, TextType, text_node_to_html_node


def split_nodes_delimiter(old_nodes: list[TextNode], delimiter: str, text_type: TextType) -> list[TextNode]:
    new_nodes = []
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

