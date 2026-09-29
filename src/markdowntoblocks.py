
def markdown_to_blocks(document: str) -> list[str]:
    return list(filter(lambda x: x, map(lambda x: x.strip(), document.split("\n\n"))))
