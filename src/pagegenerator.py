
import os

from extractors import extract_title
from markdowntohtmlnode import markdown_to_html_node


def generate_page(from_path: str, template_path: str, dest_path: str) -> None:
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    contents = read_file(from_path)
    template = read_file(template_path)

    html_node = markdown_to_html_node(contents)
    html = html_node.to_html()

    title = extract_title(contents)

    populated_template = template.replace("{{ Title }}", title).replace("{{ Content }}", html)

    write_file(populated_template, dest_path)

def read_file(file_path: str) -> str:
    with open(file_path, "r") as f:
        return f.read()

def write_file(contents: str, dest_path: str) -> None:
    dir_name = os.path.dirname(dest_path)
    os.makedirs(dir_name, exist_ok=True)

    with open(dest_path, "w") as f:
        f.write(contents)