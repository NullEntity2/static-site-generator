import re


def extract_markdown_images(text: str) -> list[tuple[str, str]]:
    matches = re.findall(r"\!\[(.*?)\]\((.*?)\)", text)
    return matches

def extract_markdown_links(text: str) -> list[tuple[str, str]]:
    matches = re.findall(r"(?<!!)\[(.*?)\]\((.*?)\)", text)
    return matches

def extract_title(text: str) -> str:
    matches = re.findall(r"# (.*)", text)
    if not matches:
        raise ValueError("input text must have a h1")
    return matches[0].strip()