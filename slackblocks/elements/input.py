from enum import Enum
from typing import Any, Optional
from . import Element, ElementType, Text, TextType


class InputElementType(Enum):
    PLAIN_TEXT_INPUT = "plain_text_input"
    URL_TEXT_INPUT = "url_text_input"
    EMAIL_TEXT_INPUT = "email_text_input"
    DATETIMEPICKER = "datetimepicker"
    CONVERSATIONS_SELECT = "conversations_select"


class Input(Element):
    """An interactive element that inserts an input element."""

    def __init__(
        self,
        input_type: InputElementType,
        block_id: str,
        label: str,
        action_id: str | None = None,
        placeholder: str | None = None,
        initial_value: Optional[str] = None,
        multiline: Optional[bool] = False,
        dispatch_action: Optional[bool] = False,
        optional: Optional[bool] = False
    ):
        super().__init__(type_=ElementType.INPUT)

        self.input_type = input_type
        self.block_id = block_id
        self.action_id = action_id
        self.label_text = Text(label, type_=TextType.PLAINTEXT, emoji=True)
        self.multiline = multiline
        self.initial_value = initial_value
        self.dispatch_action = dispatch_action
        self.optional = optional

        if placeholder:
            self.placeholder = Text(placeholder, type_=TextType.PLAINTEXT, emoji=True)

    def resolve(self) -> dict[str, Any]:
        input = self._attributes() | {
            "block_id": self.block_id,
            "element": {
                "type": self.input_type.value
            },
            "optional": self.optional,
            "label": self.label_text.resolve(),
            "dispatch_action": self.dispatch_action
        }

        if self.input_type == InputElementType.PLAIN_TEXT_INPUT:
            input["element"]["multiline"] = self.multiline

        if hasattr(self, "placeholder"):
            input["element"]["placeholder"] = self.placeholder.resolve()
        if self.action_id:
            input["action_id"] = self.action_id
        if self.initial_value:
            input["initial_value"] = self.initial_value

        return input
