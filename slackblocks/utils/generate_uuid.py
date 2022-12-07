from uuid import uuid4


def generate_uuid() -> str:
    """Generate a UUID4 string"""
    return str(uuid4())
