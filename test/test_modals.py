from slackblocks import Modal, SectionBlock


def test_modals():
    trigger_id = "test-trigger-id"
    modal_title = "test"

    modal = Modal(title=modal_title, blocks=[], trigger_id=trigger_id).resolve()

    del modal["view"]["callback_id"]

    assert modal == {
        "trigger_id": trigger_id,
        "view": {
            "blocks": [],
            "type": "modal",
            "title": {
                "text": modal_title,
                "type": "plain_text",
            }
        },
    }

