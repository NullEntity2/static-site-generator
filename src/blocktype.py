from enum import Enum
import re

class BlockType(Enum):
    PARAGRAPH = 1
    HEADING = 2
    CODE = 3
    QUOTE = 4
    UNORDERED_LIST = 5
    ORDERED_LIST = 6

def block_to_block_type(input: str) -> BlockType:
    if re.match(r"#{1,6} ", input):
        return BlockType.HEADING
    if re.match(r"```\n.*\n```", input, re.DOTALL):
        return BlockType.CODE
    lines = input.splitlines()
    if all(line.startswith(">") for line in lines):
        return BlockType.QUOTE
    if all(line.startswith("- ") for line in lines):
        return BlockType.UNORDERED_LIST
    for i, line in enumerate(lines):
        if not line.startswith(f"{i+1}. "):
            return BlockType.PARAGRAPH
    return BlockType.ORDERED_LIST