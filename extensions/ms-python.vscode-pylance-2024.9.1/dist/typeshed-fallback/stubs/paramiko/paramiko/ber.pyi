from collections.abc import Iterable
from typing import Any

class BERException(Exception): ...

class BER:
    content: bytes
    idx: int
    def __init__(self, content: bytes = b"") -> None: ...
    def asbytes(self) -> bytes: ...
    def decode(self) -> None | int | list[int]: ...
    def decode_next(self) -> None | int | list[int]: ...
    @staticmethod
    def decode_sequence(data: bytes) -> list[int | list[int]]: ...
    def encode_tlv(self, ident: int, val: bytes) -> None: ...
    def encode(self, x: Any) -> None: ...
    @staticmethod
    def encode_sequence(data: Iterable[str]) -> bytes: ...
