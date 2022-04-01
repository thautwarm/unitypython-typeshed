from abc import ABC
from typing import Any
class Enum(ABC):
    @property
    def name(self) -> str: ...

    @property
    def value(self) -> object: ...

def auto() -> Any: ...