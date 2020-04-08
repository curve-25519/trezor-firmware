# Automatically generated by pb2py
# fmt: off
from .. import protobuf as p

from .MoneroTransactionSourceEntry import MoneroTransactionSourceEntry

if __debug__:
    try:
        from typing import Dict, List  # noqa: F401
        from typing_extensions import Literal  # noqa: F401
    except ImportError:
        pass


class MoneroTransactionSetInputRequest(p.MessageType):
    MESSAGE_WIRE_TYPE = 503

    def __init__(
        self,
        *,
        src_entr: MoneroTransactionSourceEntry = None,
    ) -> None:
        self.src_entr = src_entr

    @classmethod
    def get_fields(cls) -> Dict:
        return {
            1: ('src_entr', MoneroTransactionSourceEntry, 0),
        }
