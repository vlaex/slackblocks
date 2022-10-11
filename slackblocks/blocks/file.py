from . import Block, BlockType


class FileBlock(Block):
    """Displays a remote file."""

    def __init__(self, external_id: str, source: str, block_id: str):
        super().__init__(type_=BlockType.FILE, block_id=block_id)

        self.external_id = external_id
        self.source = source

    def resolve(self) -> dict[str, str]:
        file = self._attributes() | {
            "external_id": self.external_id,
            "source": self.source
        }

        return file
