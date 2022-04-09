from _typeshed import Self
from abc import abstractmethod
from typing import Annotated, Any, Callable, Concatenate, Generic, Iterable, Iterator, Literal, ParamSpec, Protocol, Type, TypeGuard, TypeVar, final, overload


def setProjectDirectory(__path: str) -> None: ...
def getPersistentDataPath() -> str: ...
def getProjectDir() -> str: ...


@final
class Color:
    def __eq__(self, __o: Color) -> bool: ...
    def __ne__(self, __o: Color) -> bool: ...
    def __hash__(self) -> int: ...

    r: float
    g: float
    b: float
    a: float

    def __new__(cls: Type[Self], r: float, g: float, b: float, a: float) -> Self: ...


@final
class Vector3:
    def __eq__(self, __o: Vector3) -> bool: ...
    def __ne__(self, __o: Vector3) -> bool: ...
    def __hash__(self) -> int: ...

    @overload
    def __add__(self, __o: Vector3) -> Vector3: ...
    @overload
    def __add__(self, __o: int) -> Vector3: ...
    @overload
    def __add__(self, __o: float) -> Vector3: ...
    @overload
    def __radd__(self, __o: int) -> Vector3: ...
    @overload
    def __radd__(self, __o: float) -> Vector3: ...

    @overload
    def __sub__(self, __o: Vector3) -> Vector3: ...
    @overload
    def __sub__(self, __o: int) -> Vector3: ...
    @overload
    def __sub__(self, __o: float) -> Vector3: ...
    @overload
    def __rsub__(self, __o: int) -> Vector3: ...
    @overload
    def __rsub__(self, __o: float) -> Vector3: ...

    @overload
    def __mul__(self, __o: Vector3) -> Vector3: ...
    @overload
    def __mul__(self, __o: int) -> Vector3: ...
    @overload
    def __mul__(self, __o: float) -> Vector3: ...
    @overload
    def __rmul__(self, __o: int) -> Vector3: ...
    @overload
    def __rmul__(self, __o: float) -> Vector3: ...

    def __matmul__(self, __o: Vector3) -> float: ...

    @overload
    def __truediv__(self, __o: Vector3) -> Vector3: ...
    @overload
    def __truediv__(self, __o: int) -> Vector3: ...
    @overload
    def __truediv__(self, __o: float) -> Vector3: ...
    @overload
    def __rtruediv__(self, __o: int) -> Vector3: ...
    @overload
    def __rtruediv__(self, __o: float) -> Vector3: ...


    @overload
    def __pow__(self, __o: Vector3) -> Vector3: ...
    @overload
    def __pow__(self, __o: int) -> Vector3: ...
    @overload
    def __pow__(self, __o: float) -> Vector3: ...
    @overload
    def __rpow__(self, __o: int) -> Vector3: ...
    @overload
    def __rpow__(self, __o: float) -> Vector3: ...


    @overload
    def __mod__(self, __o: Vector3) -> Vector3: ...
    @overload
    def __mod__(self, __o: int) -> Vector3: ...
    @overload
    def __mod__(self, __o: float) -> Vector3: ...
    @overload
    def __rmod__(self, __o: int) -> Vector3: ...
    @overload
    def __rmod__(self, __o: float) -> Vector3: ...

    def __neg__(self) -> Vector3: ...
    def __abs__(self) -> Vector3: ...

    x: float
    y: float
    z: float
    def __new__(cls: Type[Self], __x: float, __y: float, __z: float) -> Self: ...
    def tovec2(self) -> Vector2: ...


@final
class Vector2:
    def __eq__(self, __o: Vector2) -> bool: ...
    def __ne__(self, __o: Vector2) -> bool: ...
    def __hash__(self) -> int: ...

    @overload
    def __add__(self, __o: Vector2) -> Vector2: ...
    @overload
    def __add__(self, __o: int) -> Vector2: ...
    @overload
    def __add__(self, __o: float) -> Vector2: ...
    @overload
    def __radd__(self, __o: int) -> Vector2: ...
    @overload
    def __radd__(self, __o: float) -> Vector2: ...

    @overload
    def __sub__(self, __o: Vector2) -> Vector2: ...
    @overload
    def __sub__(self, __o: int) -> Vector2: ...
    @overload
    def __sub__(self, __o: float) -> Vector2: ...
    @overload
    def __rsub__(self, __o: int) -> Vector2: ...
    @overload
    def __rsub__(self, __o: float) -> Vector2: ...

    @overload
    def __mul__(self, __o: Vector2) -> Vector2: ...
    @overload
    def __mul__(self, __o: int) -> Vector2: ...
    @overload
    def __mul__(self, __o: float) -> Vector2: ...
    @overload
    def __rmul__(self, __o: int) -> Vector2: ...
    @overload
    def __rmul__(self, __o: float) -> Vector2: ...

    def __matmul__(self, __o: Vector2) -> float: ...

    @overload
    def __truediv__(self, __o: Vector2) -> Vector2: ...
    @overload
    def __truediv__(self, __o: int) -> Vector2: ...
    @overload
    def __truediv__(self, __o: float) -> Vector2: ...
    @overload
    def __rtruediv__(self, __o: int) -> Vector2: ...
    @overload
    def __rtruediv__(self, __o: float) -> Vector2: ...


    @overload
    def __pow__(self, __o: Vector2) -> Vector2: ...
    @overload
    def __pow__(self, __o: int) -> Vector2: ...
    @overload
    def __pow__(self, __o: float) -> Vector2: ...
    @overload
    def __rpow__(self, __o: int) -> Vector2: ...
    @overload
    def __rpow__(self, __o: float) -> Vector2: ...


    @overload
    def __mod__(self, __o: Vector2) -> Vector2: ...
    @overload
    def __mod__(self, __o: int) -> Vector2: ...
    @overload
    def __mod__(self, __o: float) -> Vector2: ...
    @overload
    def __rmod__(self, __o: int) -> Vector2: ...
    @overload
    def __rmod__(self, __o: float) -> Vector2: ...

    def __neg__(self) -> Vector2: ...
    def __abs__(self) -> Vector2: ...

    x: float
    y: float

    def __new__(cls: Type[Self], __x: float, __y: float) -> Self: ...

    def tovec3(self) -> Vector3: ...


@final
class ImageResource:
    @staticmethod
    def load(__path: str) -> ImageResource: ...

    def destory(self) -> None: ...


@final
class EventTriggerType:
    PointerEnter: EventTriggerType
    PointerDown: EventTriggerType
    PointerExit: EventTriggerType
    PointerUp: EventTriggerType
    PointerClick: EventTriggerType
    Drag: EventTriggerType
    Drop: EventTriggerType
    Scroll: EventTriggerType
    UpdateSelected: EventTriggerType
    Select: EventTriggerType
    Deselect: EventTriggerType
    Move: EventTriggerType
    InitializePotentialDrag: EventTriggerType
    BeginDrag: EventTriggerType
    EndDrag: EventTriggerType
    Submit: EventTriggerType
    Cancel: EventTriggerType
    __new__ = None  # type: ignore[override]


_TComponent_co = TypeVar('_TComponent_co', covariant=True, bound=MonoBehaviour)
_TComponent = TypeVar('_TComponent', bound=MonoBehaviour)
_TGameST = TypeVar('_TGameST')
_TParams = TypeVar('_TParams')

@final
class EventData:
    __new__ = None # type: ignore[override]
    @property
    def screen_pos(self) -> Vector2:
        ...
    @property
    def delta(self) -> Vector2:
        ...
    @property
    def clickCount(self) -> int:
        ...
    @property
    def clickTime(self) -> float:
        ...
    @property
    def hovered(self) -> iter[GameObject]:
        ...
    @property
    def is_scrolling(self) -> bool:
        ...
    @property
    def is_dragging(self) -> bool:
        ...
    @property
    def scroll_delta_y(self) -> float:
        ...
    @property
    def is_pointer_moving(self) -> bool:
        ...



class MonoBehaviour(Generic[_TGameST, _TParams]):
    @abstractmethod
    def __init__(self, __gameState: _TGameST, __parameters: _TParams | None = ...) -> None: ...

    @property
    def gameObject(self) -> GameObject:
        """get the base GameObject to attach components to"""
        ...

    @property
    def x(self) -> float:
        """x (screen position)
        """
        ...
    @x.setter
    def x(self, __v: float) -> None: ...

    @property
    def y(self) -> float:
        """y (screen position)
        """
        ...

    @y.setter
    def y(self, __v: float) -> None: ...

    @property
    def z(self) -> float:
        """z (world position)
        """
        ...

    @z.setter
    def z(self, __v: float) -> None: ...
    def on(self, __ev: EventTriggerType) -> Callable[[Callable[[EventData], None]], Callable[[EventData], None]]: ...
    def requireComponents(self, *cs: Type[_TComponent]) -> None: ...

@final
class GameObject:

    x: float
    """x (screen position)"""
    y: float
    """y (screen position)"""

    z: float
    """z (world position)"""
    ...

    parent: GameObject | None

    def on(self, __ev: EventTriggerType) -> Callable[[Callable[[EventData], None]], Callable[[EventData], None]]: ...
    def requireComponents(self, *cs: Type[_TComponent]) -> None: ...
    def __getitem__(self, x: Type[_TComponent]) -> ComponentGroup[_TComponent]: ...


@final
class ComponentGroup(Protocol[_TComponent_co]):
    @overload
    def add(self: ComponentGroup[MonoBehaviour[_TGameST, _TParams | None]], __gameState: _TGameST, __parameters: _TParams | None = None) -> _TComponent_co: ...
    @overload
    def add(self: ComponentGroup[MonoBehaviour[_TGameST, _TParams]], __gameState: _TGameST, __parameters: _TParams) -> _TComponent_co: ...
    def peek(self) -> _TComponent_co | None: ...

    def __iter__(self) -> Iterator[_TComponent_co]: ...


class _UIProto:
    ui: UI
    width: float
    height: float

@final
class UI(MonoBehaviour[Any, Any]):
    width: float
    height: float


RectTransform = UI


@final
class Text(MonoBehaviour[Any, Any], _UIProto):
    AlignMiddle: int
    AlignLeft: int
    AlignRight: int
    AlignTop: int
    AlignBottom: int
    AlignCenter: int

    autoSize: bool
    """autoSizeTextContainer
    Determines if the size of the text container will be adjusted to fit the text object when it is first created.
    """
    color: Color

    overflowMode: Literal["..."] | Literal["Page"] | Literal["Scroll"]
    """Controls the Text Overflow Mode.
    '...' means the Ellipsis mode.
    """

    pageCount: int
    """textInfo.pageCount
    """

    characterCount: int
    """textInfo.characterCount
    """
    displayingPage: int
    """textInfo.pageToDisplay. Must be between **1** and textInfo.pageCount
    """
    maxVisibleCharacters: int
    """Allows to control how many characters are visible from the input.
    """

    contents: str
    """text contents
    """

    alignment: int
    """Check Text.Align* for possible values; values are int flags"""

    def forceMeshUpdate(self, ignoreActiveState: bool = False, forceTextReparsing: bool = False) -> None: ...

    def playText(self, text: str, speed: float = 0.5) -> iter[None]:
        """Play text with a given speed. Note that 'displayingPage' needs to be updated separately,
        otherwise this will not stop.
        """
        ...




@final
class SpriteImage(MonoBehaviour[Any, Any], _UIProto):
    alpha: float
    """alpha in (0, 1)
    """
    image: ImageResource

@final
class RawImage(MonoBehaviour[Any, Any], _UIProto):
    alpha: float
    """alpha in (0, 1)
    """
    image: ImageResource

@final
class Sprite(MonoBehaviour[Any, Any]):
    width: float
    height: float
    alpha: float
    """alpha in (0, 1)
    """
    image: ImageResource


@final
class ScrollRect(MonoBehaviour[Any, Any], _UIProto):
    elasticity: float
    """The amount of elasticity to use when the content moves beyond the scroll rect."""
    decelerationRate: float
    """The rate at which movement slows down."""
    content: UI
    """The content that can be scrolled. It should be a child of the GameObject with ScrollRect on it."""
    inertia: bool
    """Should movement inertia be enabled?"""
    movementType: Literal["Unrestricted"] | Literal["Elastic"] | Literal["Clamped"]

    horizontalScrollbarSpacing: float
    """The space between the scrollbar and the viewport."""
    verticalScrollbarSpacing: float
    """The space between the scrollbar and the viewport."""

    def onValueChanged(self, callback: Callable[[Vector2, None], Any]) -> None:
        """Callback executed when the position of the child changes."""


@final
class PolygonCollider2D(MonoBehaviour[Any, Any]):
    def resetShape(self, sprite: Sprite, tolerance: float = 0.5): ...

@final
class CanvasGroup(MonoBehaviour[Any, Any]):
    blocksRaycasts: bool
    """Does this group block raycasting (allow collision)."""
    alpha: float
    """Set the alpha of the group."""
    ignoreParentGroups: bool
    """Should the group ignore parent groups?"""
    interactable: bool
    """Is the group interactable (are the elements beneath the group enabled)."""

@final
class Canvas(MonoBehaviour[Any, Any]):
    rootCanvas: Canvas
    """Returns the Canvas closest to root, by checking through each parent and returning the last canvas found. If no other canvas is found then the canvas will return itself."""
    sortingOrder: int
    """Canvas' order within a sorting layer."""

del _UIProto
