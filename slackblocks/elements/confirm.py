from . import Element, ElementType, Text, TextType


class Confirm(Element):
    """
    An object that defines a dialog that provides a confirmation step
    to any interactive element. This dialog will ask the user to confirm
    their action by offering confirm and deny buttons.
    """

    def __init__(self, title: str, text: str, confirm: str, deny: str):
        super().__init__(type_=ElementType.CONFIRM)

        self.title = Text(title, type_=TextType.PLAINTEXT)
        self.text = Text(text)
        self.confirm = Text(confirm, type_=TextType.PLAINTEXT)
        self.deny = Text(deny, type_=TextType.PLAINTEXT)

    def resolve(self) -> dict[str, dict]:
        return {
            "title": self.title.resolve(),
            "text": self.text.resolve(),
            "confirm": self.confirm.resolve(),
            "deny": self.deny.resolve()
        }
