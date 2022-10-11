from typing import Any
from . import Block, BlockType
from ..elements import Text, Element


class SectionBlock(Block):
    """
    A section is one of the most flexible blocks available -
    it can be used as a simple text block, in combination with text fields,
    or side-by-side with any of the available block elements.
    """

    def __init__(
        self,
        text: str | Text,
        block_id: str = None,
        fields: list[Text] = None,
        accessory: Element = None
    ):
        super().__init__(type_=BlockType.SECTION, block_id=block_id)

        if isinstance(text, Text):
            self.text = text
        else:
            self.text = Text(text)

        self.fields = fields
        self.accessory = accessory

    def resolve(self) -> dict[str, Any]:
        section = self._attributes()
        section["text"] = self.text.resolve()

        if self.fields:
            section["fields"] = [field.resolve() for field in self.fields]
        if self.accessory:
            section["accessory"] = self.accessory.resolve()

        return section
