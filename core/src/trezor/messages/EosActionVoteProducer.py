# Automatically generated by pb2py
# fmt: off
import protobuf as p

if __debug__:
    try:
        from typing import Dict, List  # noqa: F401
        from typing_extensions import Literal  # noqa: F401
    except ImportError:
        pass


class EosActionVoteProducer(p.MessageType):

    def __init__(
        self,
        *,
        producers: List[int] = None,
        voter: int = None,
        proxy: int = None,
    ) -> None:
        self.producers = producers if producers is not None else []
        self.voter = voter
        self.proxy = proxy

    @classmethod
    def get_fields(cls) -> Dict:
        return {
            1: ('voter', p.UVarintType, 0),
            2: ('proxy', p.UVarintType, 0),
            3: ('producers', p.UVarintType, p.FLAG_REPEATED),
        }
