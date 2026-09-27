

from htmlnode import HTMLNode
from functools import reduce


class ParentNode(HTMLNode):
    def __init__(self, tag: str, children: list[HTMLNode], props: dict[str, str] | None = None) -> None:
        super().__init__(tag, None, children, props)

    def to_html(self):
        if not self.tag:
            raise ValueError("tag must be set")
        if not self.children:
            raise ValueError("children must be set")
        children_html = reduce(lambda x, y: x + y.to_html(), self.children, "")
        return f"<{self.tag}>{children_html}</{self.tag}>"