from . import Block, BlockType
from ..elements import Element, ElementType


class ContextBlock(Block):
    """Displays message context, which can include both images and text."""

    def __init__(
        self,
        elements: list[Element] | Element = None,
        block_id: str = None
    ):
        super().__init__(type_=BlockType.CONTEXT, block_id=block_id)

        self.elements = []

        if not isinstance(elements, list):
            elements = [elements]

        for element in elements:
            if element.type == ElementType.TEXT or element.type == ElementType.IMAGE:
                self.elements.append(element)

    def resolve(self):
        context = self._attributes()
        context["elements"] = [element.resolve() for element in self.elements]
        return context
