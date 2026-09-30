import os
import shutil

from pagegenerator import generate_page

def main():
    if os.path.exists("public"):
        shutil.rmtree("public")
    copytree("static", "public")
    generate_pages_recursive("content", "template.html", "public")

def copytree(src: str, dest: str) -> None:
    os.makedirs(dest, exist_ok=True)
    for name in os.listdir(src):
        src_path = os.path.join(src, name)
        dest_path = os.path.join(dest, name)
        if os.path.isfile(src_path):
            print(f"Copying {src_path} -> {dest_path}")
            shutil.copy(src_path, dest_path)
        else:
            copytree(src_path, dest_path)

def generate_pages_recursive(dir_path_content: str, template_path: str, dest_dir_path: str) -> None:
    for name in os.listdir(dir_path_content):
        src_path = os.path.join(dir_path_content, name)
        if os.path.isfile(src_path):
            if name.endswith(".md"):
                dest_path = os.path.join(dest_dir_path, name[:-3] + ".html")
                generate_page(src_path, template_path, dest_path)
        else:
            generate_pages_recursive(src_path, template_path, os.path.join(dest_dir_path, name))

if __name__ == "__main__":
    main()