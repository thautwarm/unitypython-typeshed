import collections  # Needed by aliases like DefaultDict, see mypy issue 2986
import sys
from _typeshed import Self as TypeshedSelf, SupportsKeysAndGetItem
from abc import ABCMeta, abstractmethod
from types import (
    BuiltinFunctionType,
    # FrameType,
    FunctionType,
    MethodType,
    ModuleType,
    # TracebackType,
)
from typing_extensions import (
    Literal as _Literal,
    ParamSpec as _ParamSpec,
    final as _final,
)

from types import MethodDescriptorType, MethodWrapperType, WrapperDescriptorType

# from types import GenericAlias

__all__ = [
    "Annotated",
    "Any",
    "Callable",
    "ClassVar",
    "Concatenate",
    "Final",
    "ForwardRef",
    "Generic",
    "Literal",
    "Optional",
    "ParamSpec",
    "Protocol",
    "Tuple",
    "Type",
    "TypeVar",
    "Union",
    # "AbstractSet",
    # "ByteString",
    "Container",
    "ContextManager",
    "Hashable",
    # "ItemsView",
    "Iterable",
    "Iterator",
    # "KeysView",
    # "Mapping",
    # "MappingView",
    # "MutableMapping",
    # "MutableSequence",
    # "MutableSet",
    "Sequence",
    "Sized",
    # "ValuesView",
    "Awaitable",
    "AsyncIterator",
    "AsyncIterable",
    "Coroutine",
    "Collection",
    "AsyncGenerator",
    # "AsyncContextManager",
    "Reversible",
    "SupportsAbs",
    # "SupportsBytes",
    # "SupportsComplex",
    # "SupportsFloat",
    # "SupportsIndex",
    # "SupportsInt",
    "SupportsRound",
    # "ChainMap",
    # "Counter",
    # "Deque",
    "Dict",
    # "DefaultDict",
    "List",
    # "OrderedDict",
    "Set",
    # "FrozenSet",
    # "NamedTuple",
    "TypedDict",
    "Generator",
    # "BinaryIO",
    # "IO",
    # "Match",
    # "Pattern",
    # "TextIO",
    "AnyStr",
    "cast",
    "final",
    "get_args",
    "get_origin",
    "get_type_hints",
    # "is_typeddict",
    "NewType",
    "no_type_check",
    "no_type_check_decorator",
    "NoReturn",
    "overload",
    # "ParamSpecArgs",
    # "ParamSpecKwargs",
    "runtime_checkable",
    "Text",
    "TYPE_CHECKING",
    "TypeAlias",
    "TypeGuard",
]

Any = object()

@_final
class TypeVar:
    __name__: str
    __bound__: Any | None
    __constraints__: tuple[Any, ...]
    __covariant__: bool
    __contravariant__: bool
    def __init__(
        self,
        name: str,
        *constraints: Any,
        bound: Any | None = ...,
        covariant: bool = ...,
        contravariant: bool = ...
    ) -> None: ...
    if sys.version_info >= (3, 10):
        def __or__(self, other: Any) -> _SpecialForm: ...
        def __ror__(self, other: Any) -> _SpecialForm: ...

# Used for an undocumented mypy feature. Does not exist at runtime.
_promote = object()

# N.B. Keep this definition in sync with typing_extensions._SpecialForm

@_final
class _SpecialForm:
    def __getitem__(self, typeargs: Any) -> object: ...
    def __or__(self, other: Any) -> _SpecialForm: ...
    # def __ror__(self, other: Any) -> _SpecialForm: ...

_F = TypeVar("_F", bound=Callable[..., Any])
_P = _ParamSpec("_P")
_T = TypeVar("_T")

def overload(func: _F) -> _F: ...

# Unlike the vast majority module-level objects in stub files,
# these `_SpecialForm` objects in typing need the default value `= ...`,
# due to the fact that they are used elswhere in the same file.
# Otherwise, flake8 erroneously flags them as undefined.
# `_SpecialForm` objects in typing.py that are not used elswhere in the same file
# do not need the default value assignment.
Union: _SpecialForm = ...
Generic: _SpecialForm = ...
# Protocol is only present in 3.8 and later, but mypy needs it unconditionally
Protocol: _SpecialForm = ...
Type: _SpecialForm = ...
NoReturn: _SpecialForm = ...
Callable: _SpecialForm
Optional: _SpecialForm
Tuple: _SpecialForm
ClassVar: _SpecialForm
if sys.version_info >= (3, 8):
    Final: _SpecialForm
    def final(f: _T) -> _T: ...
    Literal: _SpecialForm
    # TypedDict is a (non-subscriptable) special form.
    TypedDict: object


if sys.version_info >= (3, 11):
    Self: _SpecialForm
    Never: _SpecialForm = ...

if sys.version_info < (3, 7):
    class GenericMeta(type): ...

if True:
    class ParamSpecArgs:
        __origin__: ParamSpec
        def __init__(self, origin: ParamSpec) -> None: ...

    class ParamSpecKwargs:
        __origin__: ParamSpec
        def __init__(self, origin: ParamSpec) -> None: ...

    class ParamSpec:
        __name__: str
        __bound__: Any | None
        __covariant__: bool
        __contravariant__: bool
        def __init__(
            self,
            name: str,
            *,
            bound: Any | None = ...,
            contravariant: bool = ...,
            covariant: bool = ...
        ) -> None: ...
        @property
        def args(self) -> ParamSpecArgs: ...
        @property
        def kwargs(self) -> ParamSpecKwargs: ...
        def __or__(self, other: Any) -> _SpecialForm: ...
        def __ror__(self, other: Any) -> _SpecialForm: ...
    Concatenate: _SpecialForm
    TypeAlias: _SpecialForm
    TypeGuard: _SpecialForm

    class NewType:
        def __init__(self, name: str, tp: type) -> None: ...
        def __call__(self, x: _T) -> _T: ...
        def __or__(self, other: Any) -> _SpecialForm: ...
        def __ror__(self, other: Any) -> _SpecialForm: ...
        __supertype__: type

else:
    def NewType(name: str, tp: Type[_T]) -> Type[_T]: ...

# These type variables are used by the container types.
_S = TypeVar("_S")
_KT = TypeVar("_KT")  # Key type.
_VT = TypeVar("_VT")  # Value type.
_T_co = TypeVar("_T_co", covariant=True)  # Any type covariant containers.
_V_co = TypeVar("_V_co", covariant=True)  # Any type covariant containers.
_KT_co = TypeVar("_KT_co", covariant=True)  # Key type covariant containers.
_VT_co = TypeVar("_VT_co", covariant=True)  # Value type covariant containers.
_T_contra = TypeVar("_T_contra", contravariant=True)  # Ditto contravariant.
_TC = TypeVar("_TC", bound=Type[object])

def no_type_check(arg: _F) -> _F: ...
def no_type_check_decorator(decorator: Callable[_P, _T]) -> Callable[_P, _T]: ...  # type: ignore[misc]

# Type aliases and type constructors

class _Alias:
    # Class for defining generic aliases for library types.
    def __getitem__(self, typeargs: Any) -> Any: ...

List = _Alias()
Dict = _Alias()
# DefaultDict = _Alias()
Set = _Alias()
# FrozenSet = _Alias()
# Counter = _Alias()
# Deque = _Alias()
# ChainMap = _Alias()

if sys.version_info >= (3, 9):
    Annotated: _SpecialForm

# Predefined type variables.
AnyStr = TypeVar("AnyStr", str, bytes)  # noqa: Y001

# Technically in 3.7 this inherited from GenericMeta. But let's not reflect that, since
# type checkers tend to assume that Protocols all have the ABCMeta metaclass.
class _ProtocolMeta(ABCMeta): ...

# Abstract base classes.

def runtime_checkable(cls: _TC) -> _TC: ...
# @runtime_checkable
# class SupportsInt(Protocol, metaclass=ABCMeta):
#     @abstractmethod
#     def __int__(self) -> int: ...

# @runtime_checkable
# class SupportsFloat(Protocol, metaclass=ABCMeta):
#     @abstractmethod
#     def __float__(self) -> float: ...

# # @runtime_checkable
# # class SupportsComplex(Protocol, metaclass=ABCMeta):
# #     @abstractmethod
# #     def __complex__(self) -> complex: ...

# @runtime_checkable
# class SupportsBytes(Protocol, metaclass=ABCMeta):
#     @abstractmethod
#     def __bytes__(self) -> bytes: ...

# if sys.version_info >= (3, 8):
#     @runtime_checkable
#     class SupportsIndex(Protocol, metaclass=ABCMeta):
#         @abstractmethod
#         def __index__(self) -> int: ...

# @runtime_checkable
class SupportsAbs(Protocol[_T_co]):
    @abstractmethod
    def __abs__(self) -> _T_co: ...


# @runtime_checkable
class SupportsHash(Protocol):
    __slots__ = ()

    @abstractmethod
    def __hash__(self) -> int:
        pass

# @runtime_checkable
class SupportsRound(Protocol[_T_co]):
    @overload
    @abstractmethod
    def __round__(self) -> int: ...
    @overload
    @abstractmethod
    def __round__(self, __ndigits: int) -> _T_co: ...

@runtime_checkable
class Sized(Protocol, metaclass=ABCMeta):
    @abstractmethod
    def __len__(self) -> int: ...

# @runtime_checkable
class Hashable(Protocol, metaclass=ABCMeta):
    # TODO: This is special, in that a subclass of a hashable class may not be hashable
    #   (for example, list vs. object). It's not obvious how to represent this. This class
    #   is currently mostly useless for static checking.
    @abstractmethod
    def __hash__(self) -> int: ...

@runtime_checkable
class Iterable(Protocol[_T_co]):
    @abstractmethod
    def __iter__(self) -> Iterator[_T_co]: ...

@runtime_checkable
class Iterator(Iterable[_T_co], Protocol[_T_co]):
    @abstractmethod
    def __next__(self) -> _T_co: ...
    def __iter__(self) -> Iterator[_T_co]: ...

@runtime_checkable
class Reversible(Iterable[_T_co], Protocol[_T_co]):
    @abstractmethod
    def __reversed__(self) -> Iterator[_T_co]: ...

@final
class Generator(Awaitable[_V_co], Iterator[_T_co], Generic[_T_co, _T_contra, _V_co]):
    def __next__(self, __refval: ref[Any]) -> TypeGuard[ref[_T_co]]: ...
    @property
    def is_completed(self) -> bool:
        """Returns True if the task has finished."""
        ...
    @property
    def result(self) -> _V_co | None:
        """Returns the task result, or return None if the task has not finished.
        """
        ...
    @overload
    def send(self, __value: _T_contra) -> bool: ...
    @overload
    def send(self, __value: _T_contra, __ref: ref[Any]) -> TypeGuard[_T_co]: ...
    def __iter__(self) -> Generator[_T_co, _T_contra, _V_co]: ...


@runtime_checkable
class Awaitable(Protocol[_T_co]):
    @abstractmethod
    def __await__(self) -> Generator[Any, None, _T_co]: ...

# TODO: implementation
@runtime_checkable
class Comparable(Protocol[_T_co]):
    @abstractmethod
    def __lt__(self: TypeshedSelf, other: TypeshedSelf) -> bool: ...
    def __le__(self: TypeshedSelf, other: TypeshedSelf) -> bool: ...
    def __gt__(self: TypeshedSelf, other: TypeshedSelf) -> bool: ...
    def __ge__(self: TypeshedSelf, other: TypeshedSelf) -> bool: ...

Coroutine = Generator

@runtime_checkable
class AsyncIterable(Protocol[_T_co]):
    @abstractmethod
    def __aiter__(self) -> AsyncIterator[_T_co]: ...

@runtime_checkable
class AsyncIterator(AsyncIterable[_T_co], Protocol[_T_co]):
    @abstractmethod
    async def __anext__(self) -> _T_co: ...
    def __aiter__(self) -> AsyncIterator[_T_co]: ...

AsyncGenerator = Coroutine

@runtime_checkable
class Container(Protocol[_T_co]):
    @abstractmethod
    def __contains__(self, __x: object) -> bool: ...

@runtime_checkable
class Collection(Iterable[_T_co], Container[_T_co], Protocol[_T_co]):
    # Implement Sized (but don't have it as a base class).
    @abstractmethod
    def __len__(self) -> int: ...

@runtime_checkable
class Sequence(Collection[_T_co], Reversible[_T_co], Generic[_T_co]):
    @overload
    @abstractmethod
    def __getitem__(self, i: int) -> _T_co: ...
    @overload
    @abstractmethod
    def __getitem__(self, s: slice) -> Sequence[_T_co]: ...
    # Mixin methods
    def index(self, value: Any, start: int = ..., stop: int = ...) -> int: ...
    def count(self, value: Any) -> int: ...
    def __contains__(self, x: object) -> bool: ...
    def __iter__(self) -> Iterator[_T_co]: ...
    def __reversed__(self) -> Iterator[_T_co]: ...

# class MutableSequence(Sequence[_T], Generic[_T]):
#     @abstractmethod
#     def insert(self, index: int, value: _T) -> None: ...
#     @overload
#     @abstractmethod
#     def __getitem__(self, i: int) -> _T: ...
#     @overload
#     @abstractmethod
#     def __getitem__(self, s: slice) -> MutableSequence[_T]: ...
#     @overload
#     @abstractmethod
#     def __setitem__(self, i: int, o: _T) -> None: ...
#     @overload
#     @abstractmethod
#     def __setitem__(self, s: slice, o: Iterable[_T]) -> None: ...
#     @overload
#     @abstractmethod
#     def __delitem__(self, i: int) -> None: ...
#     @overload
#     @abstractmethod
#     def __delitem__(self, i: slice) -> None: ...
#     # Mixin methods
#     def append(self, value: _T) -> None: ...
#     def clear(self) -> None: ...
#     def extend(self, values: Iterable[_T]) -> None: ...
#     def reverse(self) -> None: ...
#     def pop(self, index: int = ...) -> _T: ...
#     def remove(self, value: _T) -> None: ...
#     def __iadd__(self: TypeshedSelf, x: Iterable[_T]) -> TypeshedSelf: ...

# class AbstractSet(Collection[_T_co], Generic[_T_co]):
#     @abstractmethod
#     def __contains__(self, x: object) -> bool: ...
#     def _hash(self) -> int: ...
#     # Mixin methods
#     def __le__(self, s: AbstractSet[Any]) -> bool: ...
#     def __lt__(self, s: AbstractSet[Any]) -> bool: ...
#     def __gt__(self, s: AbstractSet[Any]) -> bool: ...
#     def __ge__(self, s: AbstractSet[Any]) -> bool: ...
#     def __and__(self, s: AbstractSet[Any]) -> AbstractSet[_T_co]: ...
#     def __or__(self, s: AbstractSet[_T]) -> AbstractSet[_T_co | _T]: ...
#     def __sub__(self, s: AbstractSet[Any]) -> AbstractSet[_T_co]: ...
#     def __xor__(self, s: AbstractSet[_T]) -> AbstractSet[_T_co | _T]: ...
#     def isdisjoint(self, other: Iterable[Any]) -> bool: ...

# class MutableSet(AbstractSet[_T], Generic[_T]):
#     @abstractmethod
#     def add(self, value: _T) -> None: ...
#     @abstractmethod
#     def discard(self, value: _T) -> None: ...
#     # Mixin methods
#     def clear(self) -> None: ...
#     def pop(self) -> _T: ...
#     def remove(self, value: _T) -> None: ...
#     def __ior__(self: TypeshedSelf, s: AbstractSet[_T]) -> TypeshedSelf: ...  # type: ignore[override,misc]
#     def __iand__(self: TypeshedSelf, s: AbstractSet[Any]) -> TypeshedSelf: ...
#     def __ixor__(self: TypeshedSelf, s: AbstractSet[_T]) -> TypeshedSelf: ...  # type: ignore[override,misc]
#     def __isub__(self: TypeshedSelf, s: AbstractSet[Any]) -> TypeshedSelf: ...

# class MappingView(Sized):
#     def __init__(self, mapping: Mapping[Any, Any]) -> None: ...  # undocumented
#     def __len__(self) -> int: ...

# class ItemsView(
#     MappingView, AbstractSet[tuple[_KT_co, _VT_co]], Generic[_KT_co, _VT_co]
# ):
#     def __init__(self, mapping: Mapping[_KT_co, _VT_co]) -> None: ...  # undocumented
#     def __and__(self, o: Iterable[Any]) -> set[tuple[_KT_co, _VT_co]]: ...
#     def __rand__(self, o: Iterable[_T]) -> set[_T]: ...
#     def __contains__(self, o: object) -> bool: ...
#     def __iter__(self) -> Iterator[tuple[_KT_co, _VT_co]]: ...
#     if sys.version_info >= (3, 8):
#         def __reversed__(self) -> Iterator[tuple[_KT_co, _VT_co]]: ...

#     def __or__(self, o: Iterable[_T]) -> set[tuple[_KT_co, _VT_co] | _T]: ...
#     def __ror__(self, o: Iterable[_T]) -> set[tuple[_KT_co, _VT_co] | _T]: ...
#     def __sub__(self, o: Iterable[Any]) -> set[tuple[_KT_co, _VT_co]]: ...
#     def __rsub__(self, o: Iterable[_T]) -> set[_T]: ...
#     def __xor__(self, o: Iterable[_T]) -> set[tuple[_KT_co, _VT_co] | _T]: ...
#     def __rxor__(self, o: Iterable[_T]) -> set[tuple[_KT_co, _VT_co] | _T]: ...


@runtime_checkable
class ContextManager(Protocol[_T_co]):
    def __enter__(self) -> _T_co: ...
    def __exit__(
        self,
        __exc_type: Type[BaseException] | None,
        __exc_value: BaseException | None,
        __traceback: None # Unity Python has no traceback type, so the 3rd arg is None
    ) -> bool | None: ...

# @runtime_checkable
# class AsyncContextManager(Protocol[_T_co]):
#     async def __aenter__(self) -> _T_co: ...
#     async def __aexit__(
#         self,
#         __exc_type: Type[BaseException] | None,
#         __exc_value: BaseException | None,
#         __traceback: TracebackType | None,
#     ) -> bool | None: ...

class Mapping(Collection[_KT], Generic[_KT, _VT_co]):
    # TODO: We wish the key type could also be covariant, but that doesn't work,
    # see discussion in https://github.com/python/typing/pull/273.
    @abstractmethod
    def __finditem__(self, __k: _KT, __v_ref: ref[Any]) -> TypeGuard[ref[_VT_co]]: ...
    # Mixin methods
    def __getitem__(self, __k: _KT) -> _VT_co: ...
    @overload
    def get(self, __key: _KT) -> _VT_co | None: ...
    @overload
    def get(self, __key: _KT, default: _VT_co | _T) -> _VT_co | _T: ...
    def find(self, __key: _KT, __v_ref: ref[Any]) -> TypeGuard[ref[_VT_co]]: ...
    def items(self) -> iter[tuple[_KT, _VT_co]]: ...
    def keys(self) -> iter[_KT]: ...
    def values(self) -> iter[_VT_co]: ...
    def __contains__(self, __o: object) -> bool: ...

# class MutableMapping(Mapping[_KT, _VT], Generic[_KT, _VT]):
#     @abstractmethod
#     def __setitem__(self, __k: _KT, __v: _VT) -> None: ...
#     @abstractmethod
#     def __delitem__(self, __v: _KT) -> None: ...
#     def clear(self) -> None: ...
#     @overload
#     def pop(self, __key: _KT) -> _VT: ...
#     @overload
#     def pop(self, __key: _KT, default: _VT | _T) -> _VT | _T: ...
#     def popitem(self) -> tuple[_KT, _VT]: ...
#     # This overload should be allowed only if the value type is compatible with None.
#     # Keep OrderedDict.setdefault in line with MutableMapping.setdefault, modulo positional-only differences.
#     @overload
#     def setdefault(self: MutableMapping[_KT, _T | None], __key: _KT) -> _T | None: ...
#     @overload
#     def setdefault(self, __key: _KT, __default: _VT) -> _VT: ...
    # 'update' used to take a Union, but using overloading is better.
    # The second overloaded type here is a bit too general, because
    # Mapping[tuple[_KT, _VT], W] is a subclass of Iterable[tuple[_KT, _VT]],
    # but will always have the behavior of the first overloaded type
    # at runtime, leading to keys of a mix of types _KT and tuple[_KT, _VT].
    # We don't currently have any way of forcing all Mappings to use
    # the first overload, but by using overloading rather than a Union,
    # mypy will commit to using the first overload when the argument is
    # known to be a Mapping with unknown type parameters, which is closer
    # to the behavior we want. See mypy issue  #1430.
    #
    # Various mapping classes have __ior__ methods that should be kept roughly in line with .update():
    # -- dict.__ior__
    # -- os._Environ.__ior__
    # -- collections.UserDict.__ior__
    # -- collections.ChainMap.__ior__
    # -- weakref.WeakValueDictionary.__ior__
    # -- weakref.WeakKeyDictionary.__ior__
    # @overload
    # def update(self, __m: SupportsKeysAndGetItem[_KT, _VT], **kwargs: _VT) -> None: ...
    # @overload
    # def update(self, __m: Iterable[tuple[_KT, _VT]], **kwargs: _VT) -> None: ...
    # @overload
    # def update(self, **kwargs: _VT) -> None: ...

Text = str

TYPE_CHECKING: bool

# In stubs, the arguments of the IO class are marked as positional-only.
# This differs from runtime, but better reflects the fact that in reality
# classes deriving from IO use different names for the arguments.
# Functions

if sys.version_info >= (3, 7):
    _get_type_hints_obj_allowed_types = Union[
        object,
        Callable[..., Any],
        FunctionType,
        BuiltinFunctionType,
        MethodType,
        ModuleType,
        WrapperDescriptorType,
        MethodWrapperType,
        MethodDescriptorType,
    ]
else:
    _get_type_hints_obj_allowed_types = Union[
        object,
        Callable[..., Any],
        FunctionType,
        BuiltinFunctionType,
        MethodType,
        ModuleType,
    ]

if sys.version_info >= (3, 9):
    def get_type_hints(
        obj: _get_type_hints_obj_allowed_types,
        globalns: dict[str, Any] | None = ...,
        localns: dict[str, Any] | None = ...,
        include_extras: bool = ...,
    ) -> dict[str, Any]: ...

else:
    def get_type_hints(
        obj: _get_type_hints_obj_allowed_types,
        globalns: dict[str, Any] | None = ...,
        localns: dict[str, Any] | None = ...,
    ) -> dict[str, Any]: ...

if sys.version_info >= (3, 8):
    def get_origin(tp: Any) -> Any | None: ...
    def get_args(tp: Any) -> tuple[Any, ...]: ...

@overload
def cast(typ: Type[_T], val: Any) -> _T: ...
@overload
def cast(typ: str, val: Any) -> Any: ...
@overload
def cast(typ: object, val: Any) -> Any: ...

if sys.version_info >= (3, 11):
    def reveal_type(__obj: _T) -> _T: ...
    def assert_never(__arg: Never) -> Never: ...

# Internal mypy fallback type for all typed dicts (does not exist at runtime)
class _TypedDict(dict[str, object]):
    def copy(self: TypeshedSelf) -> TypeshedSelf: ...
    # Using NoReturn so that only calls using mypy plugin hook that specialize the signature
    # can go through.
    def setdefault(self, k: NoReturn, default: object) -> object: ...
    # Mypy plugin hook for 'pop' expects that 'default' has a type variable type.
    def pop(self, k: NoReturn, default: _T = ...) -> object: ...  # type: ignore
    def update(self: _T, __m: _T) -> None: ...
    def __delitem__(self, k: NoReturn) -> None: ...
    def items(self) -> iter[tuple[str, object]]: ...
    def keys(self) -> iter[str]: ...
    def values(self) -> iter[object]: ...
    def __or__(self: TypeshedSelf, __value: TypeshedSelf) -> TypeshedSelf: ...
    # def __ior__(self: TypeshedSelf, __value: TypeshedSelf) -> TypeshedSelf: ...

# This itself is only available during type checking
def type_check_only(func_or_cls: _F) -> _F: ...

ForwardRef = str

class NamedTuple(tuple[Any, ...]): # type: ignore
    pass
