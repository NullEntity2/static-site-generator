
import unittest

from extractors import extract_markdown_images, extract_markdown_links, extract_title


class TestExtractors(unittest.TestCase):
    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_markdown_2_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![foo](bar)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png"), ("foo", "bar")], matches)

    def test_extract_markdown_links(self):
        matches = extract_markdown_links(
            "This is text with an [link](https://google.com/)"
        )
        self.assertListEqual([("link", "https://google.com/")], matches)

    def test_extract_markdown_2_links(self):
        matches = extract_markdown_links(
            "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        )
        self.assertListEqual([("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")], matches)

    def test_extract_title(self):
        match = extract_title("# h1")
        self.assertEqual(match, "h1")

    def test_extract_title_multiple_lines(self):
        match = extract_title("Hello\nWorld\n# h1")
        self.assertEqual(match, "h1")

    def test_extract_title_no_h1_raises(self):
        with self.assertRaises(ValueError):
            extract_title("no h1")