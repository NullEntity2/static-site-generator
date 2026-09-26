class HTMLNode:
    def __init__(self, 
                 tag: str | None = None, 
                 value: str | None = None, 
                 children: list[HTMLNode] | None = None,
                 props: dict[str, str] | None = None) -> None:
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("must be implemented by child classes")

    def props_to_html(self):
        if not self.props:
            return ""
        if "href" not in self.props or "target" not in self.props:
            return ""
        return f' href="{self.props["href"]}" target="{self.props["target"]}"'

    def __repr__(self) -> str:
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"