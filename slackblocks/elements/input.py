from typing import Any, Optional
from . import Element, ElementType, Text, TextType


class Input(Element):
    """An interactive element that inserts a plain-text input element."""

    def __init__(
        self,
        label: str,
        action_id: str | None = None,
        placeholder: str | None = None,
        initial_value: Optional[str] = None,
        multiline: Optional[bool] = False,
        dispatch_action: Optional[bool] = False,
        optional: Optional[bool] = False
    ):
        super().__init__(type_=ElementType.INPUT)

        if placeholder:
            self.placeholder = Text(placeholder, type_=TextType.PLAINTEXT, emoji=True)
        if action_id:
            self.action_id = action_id

        self.label_text = Text(label, type_=TextType.PLAINTEXT, emoji=True)
        self.multiline = multiline
        self.initial_value = initial_value
        self.dispatch_action = dispatch_action
        self.optional = optional

    def resolve(self) -> dict[str, Any]:
        input_element = self._attributes() | {
            "element": {
                "type": "plain_text_input",
                "multiline": self.multiline
            },
            "optional": self.optional,
            "label": self.label_text.resolve(),
            "dispatch_action": self.dispatch_action
        }

        if hasattr(self, "placeholder"):
            input_element["element"]["placeholder"] = self.placeholder.resolve()
        if hasattr(self, "action_id"):
            input_element["action_id"] = self.action_id
        if self.initial_value:
            input_element["initial_value"] = self.initial_value

        return input_element
