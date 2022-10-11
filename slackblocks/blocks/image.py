from . import Block, BlockType
from ..elements import Text, TextType


class ImageBlock(Block):
    """A simple image block, designed to make those cat photos really pop."""

    def __init__(
        self,
        image_url: str,
        alt_text: str = "",
        title: Text | str = None,
        block_id: str = None
    ):
        super().__init__(type_=BlockType.IMAGE, block_id=block_id)

        self.image_url = image_url
        self.alt_text = alt_text

        if title and isinstance(title, Text):
            if title.text_type == TextType.MARKDOWN:
                self.title = Text(
                    text=title.text,
                    type_=TextType.PLAINTEXT,
                    emoji=title.emoji,
                    verbatim=title.verbatim
                )
            else:
                self.title = title
        elif title:
            self.title = Text(text=title, type_=TextType.PLAINTEXT)
        else:
            self.title = Text(text=" ", type_=TextType.PLAINTEXT)

    def resolve(self) -> dict[str, str]:
        image = self._attributes()
        image["image_url"] = self.image_url
        image["alt_text"] = self.alt_text

        if self.title:
            image["title"] = self.title.resolve()

        return image
