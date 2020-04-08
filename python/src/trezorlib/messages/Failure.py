# Automatically generated by pb2py
# fmt: off
from .. import protobuf as p

if __debug__:
    try:
        from typing import Dict, List  # noqa: F401
        from typing_extensions import Literal  # noqa: F401
        EnumTypeFailureType = Literal[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 99]
    except ImportError:
        pass


class Failure(p.MessageType):
    MESSAGE_WIRE_TYPE = 3

    def __init__(
        self,
        *,
        code: EnumTypeFailureType = None,
        message: str = None,
    ) -> None:
        self.code = code
        self.message = message

    @classmethod
    def get_fields(cls) -> Dict:
        return {
            1: ('code', p.EnumType("FailureType", (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 99)), 0),
            2: ('message', p.UnicodeType, 0),
        }
