import pytest
from slackblocks import Attachment


def test_invalid_usage_exception() -> None:
    with pytest.raises(ValueError):
        attachment = Attachment(blocks=[], color="0000000000000")
        print(attachment)
