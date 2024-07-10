from eolymp.annotations import http_pb2 as _http_pb2
from eolymp.annotations import ratelimit_pb2 as _ratelimit_pb2
from eolymp.annotations import scope_pb2 as _scope_pb2
from eolymp.community import rating_point_pb2 as _rating_point_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DeleteRatingInput(_message.Message):
    __slots__ = ["point", "rating_id"]
    POINT_FIELD_NUMBER: _ClassVar[int]
    RATING_ID_FIELD_NUMBER: _ClassVar[int]
    point: _rating_point_pb2.RatingPoint
    rating_id: str
    def __init__(self, rating_id: _Optional[str] = ..., point: _Optional[_Union[_rating_point_pb2.RatingPoint, _Mapping]] = ...) -> None: ...

class DeleteRatingOutput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class SetRatingInput(_message.Message):
    __slots__ = ["rating", "rating_id"]
    RATING_FIELD_NUMBER: _ClassVar[int]
    RATING_ID_FIELD_NUMBER: _ClassVar[int]
    rating: _rating_point_pb2.RatingPoint
    rating_id: str
    def __init__(self, rating_id: _Optional[str] = ..., rating: _Optional[_Union[_rating_point_pb2.RatingPoint, _Mapping]] = ...) -> None: ...

class SetRatingOutput(_message.Message):
    __slots__ = ["rating_id"]
    RATING_ID_FIELD_NUMBER: _ClassVar[int]
    rating_id: str
    def __init__(self, rating_id: _Optional[str] = ...) -> None: ...
