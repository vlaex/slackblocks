from typing import Any, Optional
from . import Element, ElementType


class Image(Element):
    """
    An element to insert an image - this element can be used in section
    and context blocks only. If you want a block with only an image in it,
    you're looking for the image block.
    """

    def __init__(self, image_url: str, alt_text: Optional[str] = None):
        super().__init__(type_=ElementType.IMAGE)

        self.image_url = image_url
        self.alt_text = alt_text or image_url

    def resolve(self) -> dict[str, Any]:
        image = self._attributes() | {
            "image_url": self.image_url,
            "alt_text": self.alt_text
        }

        return image
