from textnode import TextNode, TextType


def main():
    text_node = TextNode("This is some anhor text", TextType.LINK, "http://google.com")
    print(text_node)

if __name__ == "__main__":
    main()