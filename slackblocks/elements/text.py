import re
from enum import Enum
from typing import Any
from . import Element, ElementType


class TextType(Enum):
    """
    Allowable types for Slack Text objects.
    N.B: some usages of Text objects only allow the plaintext variety.
    """
    MARKDOWN = "mrkdwn"
    PLAINTEXT = "plain_text"


class Text(Element):
    """
    An object containing some text, formatted either as plain_text or using
    Slack's "mrkdwn"
    """
    _text: str = ""

    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, value):
        self._text = re.sub(r"(?<=\n)\s*", "", value)

    def __init__(
        self,
        text: str,
        type_: TextType = TextType.MARKDOWN,
        emoji: bool = False,
        verbatim: bool = False
    ):
        super().__init__(type_=ElementType.TEXT)

        self.text_type = type_
        self.text = text

        if self.text_type == TextType.MARKDOWN:
            self.verbatim = verbatim
            self.emoji = None
        elif self.text_type == TextType.PLAINTEXT:
            self.verbatim = None
            self.emoji = emoji

    def resolve(self) -> dict[str, Any]:
        text = {
            "type": self.text_type.value,
            "text": self.text,
        }

        if self.text_type == TextType.MARKDOWN:
            text["verbatim"] = self.verbatim
        elif self.type == TextType.PLAINTEXT and self.emoji:
            text["emoji"] = self.emoji

        return text

    def __str__(self) -> str:
        return self.json()
