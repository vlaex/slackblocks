from . import Block, BlockType
from ..elements import Element


class ActionsBlock(Block):
    """A block that is used to hold interactive elements."""

    def __init__(self, elements: list[Element] = None, block_id: str = None):
        super().__init__(type_=BlockType.ACTIONS, block_id=block_id)

        self.elements = elements

    def resolve(self):
        actions = self._attributes()
        actions["elements"] = [element.resolve() for element in self.elements]
        return actions
