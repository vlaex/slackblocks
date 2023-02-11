from typing import Optional, Any
from . import Element, ElementType, Text, TextType, Confirm


class Button(Element):
    """An interactive element that inserts a button."""

    def __init__(
        self,
        text: str,
        action_id: Optional[str] = None,
        url: Optional[str] = None,
        value: Optional[str] = None,
        style: Optional[str] = None,
        confirm: Optional[Confirm] = None
    ):
        super().__init__(type_=ElementType.BUTTON)

        self.text = Text(text, verbatim=False, type_=TextType.PLAINTEXT)
        self.action_id = action_id
        self.url = url
        self.value = value
        self.style = style
        self.confirm = confirm

    def resolve(self) -> dict[str, Any]:
        button = self._attributes()
        button["text"] = self.text.resolve()

        if self.action_id:
            button["action_id"] = self.action_id
        if self.style:
            button["style"] = self.style
        if self.url:
            button["url"] = self.url
        if self.value:
            button["value"] = self.value
        if self.confirm:
            button["confirm"] = self.confirm.resolve()

        return button
