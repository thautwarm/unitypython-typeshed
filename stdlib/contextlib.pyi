from _typeshed import Self, StrOrBytesPath
from types import TracebackType
from typing import (  # noqa Y027
    Any,
    Awaitable,
    Callable,
    ContextManager,
    Generator,
    Generic,
    Iterator,
    Optional,
    TypeVar,
)
from typing_extensions import ParamSpec


__all__ = [
    "contextmanager",
    "AbstractContextManager",
    "ContextDecorator",
    "suppress",
]

AbstractContextManager = ContextManager

_T = TypeVar("_T")
_T_co = TypeVar("_T_co", covariant=True)
_F = TypeVar("_F", bound=Callable[..., Any])
_P = ParamSpec("_P")

_ExitFunc = Callable[[Optional[type[BaseException]], Optional[BaseException], Optional[TracebackType]], Optional[bool]]
_CM_EF = TypeVar("_CM_EF", AbstractContextManager[Any], _ExitFunc)

class ContextDecorator:
    def __call__(self, func: _F) -> _F: ...

class _GeneratorContextManager(AbstractContextManager[_T_co], ContextDecorator, Generic[_T_co]):
    # In Python <= 3.6, __init__ and all instance attributes are defined directly on this class.
    # In Python >= 3.7, __init__ and all instance attributes are inherited from _GeneratorContextManagerBase
    # _GeneratorContextManagerBase is more trouble than it's worth to include in the stub; see #6676
    def __init__(self, func: Callable[..., Iterator[_T_co]], args: tuple[Any, ...], kwds: dict[str, Any]) -> None: ...
    gen: Generator[_T_co, Any, Any]
    func: Callable[..., Generator[_T_co, Any, Any]]
    args: tuple[Any, ...]
    kwds: dict[str, Any]
    def __exit__(
        self, typ: type[BaseException] | None, value: BaseException | None, traceback: None
    ) -> bool | None: ...

def contextmanager(func: Callable[_P, Iterator[_T_co]]) -> Callable[_P, _GeneratorContextManager[_T_co]]: ...

_AF = TypeVar("_AF", bound=Callable[..., Awaitable[Any]])

class suppress(AbstractContextManager[None]):
    def __init__(self, *exceptions: type[BaseException]) -> None: ...
    def __exit__(
        self, exctype: type[BaseException] | None, excinst: BaseException | None, exctb: TracebackType | None
    ) -> bool: ...
