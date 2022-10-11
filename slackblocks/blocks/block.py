from enum import Enum
from uuid import uuid4
from ..entry_with_mapping import EntryWithMapping


class BlockType(Enum):
    """
    Convenience class for identifying the different types of blocks available
    in the Slack Blocks API and their programmatic names.
    """
    SECTION = "section"
    DIVIDER = "divider"
    IMAGE = "image"
    ACTIONS = "actions"
    CONTEXT = "context"
    FILE = "file"
    HEADER = "header"


class Block(EntryWithMapping):
    """Basis block containing attributes and behaviour common to all blocks."""

    def __init__(self, type_: BlockType, block_id: str | None = None):
        self.type = type_
        self.block_id = block_id if block_id else str(uuid4())

    def __add__(self, other: "Block"):
        return [self, other]

    def _attributes(self):
        return {
            "type": self.type.value,
            "block_id": self.block_id
        }
