from enum import Enum
from typing import Any
from ..entry_with_mapping import EntryWithMapping


class ElementType(Enum):
    """
    Convenience class for referencing the various message elements Slack
    provides.
    """
    TEXT = "text"
    IMAGE = "image"
    BUTTON = "button"
    CONFIRM = "confirm"
    INPUT = "input"


class Element(EntryWithMapping):
    """
    Basis element containing attributes and behaviour common to all elements.
    """

    def __init__(self, type_: ElementType):
        super().__init__()
        self.type = type_

    def _attributes(self) -> dict[str, Any]:
        return {
            "type": self.type.value
        }
