from typing import Optional
from ..blocks import Block
from ..elements import Text, TextType
from ..entry_with_mapping import EntryWithMapping
from ..utils import generate_uuid


class Modal(EntryWithMapping):
    """
    A modal object. (https://api.slack.com/surfaces/modals/using)
    """

    def __init__(
        self, 
        title: str,
        blocks: list[Block],
        submit_text: Optional[str] = None,
        view_id: Optional[str] = None,
        view_hash: Optional[str] = None,
        trigger_id: Optional[str] = None
    ):
        self.title = title
        self.blocks = blocks
        self.submit = submit_text
        self.view_id = view_id
        self.view_hash = view_hash
        self.trigger_id = trigger_id

    def resolve(self) -> dict[str, str | dict]:
        view = {
            "blocks": [block.resolve() for block in self.blocks],
            "type": "modal",
            "callback_id": generate_uuid()
        }

        view["title"] = Text(self.title, type_=TextType.PLAINTEXT).resolve()

        if self.submit:
            view["submit"] = Text(self.submit, type_=TextType().PLAINTEXT).resolve()

        modal = {}

        if self.trigger_id:
            modal["trigger_id"] = self.trigger_id
        else:
            modal["view_id"] = self.view_id
            modal["hash"] = self.view_hash

        modal["view"] = view

        return modal
