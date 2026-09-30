import os
import shutil

from textnode import TextNode, TextType


def main():
    if os.path.exists("public"):
        shutil.rmtree("public")
    copytree("static", "public")

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

if __name__ == "__main__":
    main()