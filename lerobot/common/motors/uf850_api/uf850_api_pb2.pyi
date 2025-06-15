from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class JointState(_message.Message):
    __slots__ = ("name", "position", "velocity", "effort")
    NAME_FIELD_NUMBER: _ClassVar[int]
    POSITION_FIELD_NUMBER: _ClassVar[int]
    VELOCITY_FIELD_NUMBER: _ClassVar[int]
    EFFORT_FIELD_NUMBER: _ClassVar[int]
    name: _containers.RepeatedScalarFieldContainer[str]
    position: _containers.RepeatedScalarFieldContainer[float]
    velocity: _containers.RepeatedScalarFieldContainer[float]
    effort: _containers.RepeatedScalarFieldContainer[float]
    def __init__(self, name: _Optional[_Iterable[str]] = ..., position: _Optional[_Iterable[float]] = ..., velocity: _Optional[_Iterable[float]] = ..., effort: _Optional[_Iterable[float]] = ...) -> None: ...

class Pose(_message.Message):
    __slots__ = ("x", "y", "z", "qx", "qy", "qz")
    X_FIELD_NUMBER: _ClassVar[int]
    Y_FIELD_NUMBER: _ClassVar[int]
    Z_FIELD_NUMBER: _ClassVar[int]
    QX_FIELD_NUMBER: _ClassVar[int]
    QY_FIELD_NUMBER: _ClassVar[int]
    QZ_FIELD_NUMBER: _ClassVar[int]
    x: float
    y: float
    z: float
    qx: float
    qy: float
    qz: float
    def __init__(self, x: _Optional[float] = ..., y: _Optional[float] = ..., z: _Optional[float] = ..., qx: _Optional[float] = ..., qy: _Optional[float] = ..., qz: _Optional[float] = ...) -> None: ...

class Wrench(_message.Message):
    __slots__ = ("fx", "fy", "fz", "tx", "ty", "tz")
    FX_FIELD_NUMBER: _ClassVar[int]
    FY_FIELD_NUMBER: _ClassVar[int]
    FZ_FIELD_NUMBER: _ClassVar[int]
    TX_FIELD_NUMBER: _ClassVar[int]
    TY_FIELD_NUMBER: _ClassVar[int]
    TZ_FIELD_NUMBER: _ClassVar[int]
    fx: float
    fy: float
    fz: float
    tx: float
    ty: float
    tz: float
    def __init__(self, fx: _Optional[float] = ..., fy: _Optional[float] = ..., fz: _Optional[float] = ..., tx: _Optional[float] = ..., ty: _Optional[float] = ..., tz: _Optional[float] = ...) -> None: ...

class Empty(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class StatusResponse(_message.Message):
    __slots__ = ("success", "message")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    success: bool
    message: str
    def __init__(self, success: bool = ..., message: _Optional[str] = ...) -> None: ...
