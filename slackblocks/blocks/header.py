from . import Block, BlockType
from ..elements import Text, TextType


class HeaderBlock(Block):
    """A header is a plain-text block that displays in a larger, bold font."""

    def __init__(self, text: str | Text, block_id: str = None):
        super().__init__(type_=BlockType.HEADER, block_id=block_id)

        if isinstance(text, Text):
            self.text = text
        else:
            self.text = Text(text, type_=TextType.PLAINTEXT, verbatim=False)

    def resolve(self) -> dict[str, dict]:
        header = self._attributes()
        header["text"] = self.text.resolve()
        return header
