
import unittest

from parameterized import parameterized

from blocktype import BlockType, block_to_block_type


class TestBlockType(unittest.TestCase):
    @parameterized.expand([
        ("# 1 Heading", BlockType.HEADING),
        ("## 2 Heading", BlockType.HEADING),
        ("### 3 Heading", BlockType.HEADING),
        ("#### 4 Heading", BlockType.HEADING),
        ("##### 5 Heading", BlockType.HEADING),
        ("###### 6 Heading", BlockType.HEADING),
        ("####### 7 Heading", BlockType.PARAGRAPH),
        ("```\ncode\n```", BlockType.CODE),
        ("> some quote", BlockType.QUOTE),
        (">still a quote", BlockType.QUOTE),
        ("> some quote\n> second line", BlockType.QUOTE),
        ("- unordered list", BlockType.UNORDERED_LIST),
        ("- unordered list\n- line 2", BlockType.UNORDERED_LIST),
        ("-not an unordered list", BlockType.PARAGRAPH),
        ("1. ordered list", BlockType.ORDERED_LIST),
        ("1. ordered list\n2. line 2", BlockType.ORDERED_LIST),
    ])
    def test_block_to_blocktype(self, document: str, block_type: BlockType) -> None:
        self.assertEqual(block_to_block_type(document), block_type, document)
