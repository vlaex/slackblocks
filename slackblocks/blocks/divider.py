from . import Block, BlockType


class DividerBlock(Block):
    """
    A content divider, like an <hr>, to split up different blocks inside of
    a message. The divider block is nice and neat, requiring only a type.
    """

    def __init__(self, block_id: str = None):
        super().__init__(type_=BlockType.DIVIDER, block_id=block_id)

    def resolve(self):
        return self._attributes()
