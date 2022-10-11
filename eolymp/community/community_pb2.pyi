from eolymp.annotations import http_pb2 as _http_pb2
from eolymp.annotations import ratelimit_pb2 as _ratelimit_pb2
from eolymp.annotations import scope_pb2 as _scope_pb2
from eolymp.community import attribute_pb2 as _attribute_pb2
from eolymp.community import member_pb2 as _member_pb2
from eolymp.wellknown import expression_pb2 as _expression_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AddAttributeInput(_message.Message):
    __slots__ = ["attribute", "attribute_key"]
    ATTRIBUTE_FIELD_NUMBER: _ClassVar[int]
    ATTRIBUTE_KEY_FIELD_NUMBER: _ClassVar[int]
    attribute: _attribute_pb2.Attribute
    attribute_key: str
    def __init__(self, attribute_key: _Optional[str] = ..., attribute: _Optional[_Union[_attribute_pb2.Attribute, _Mapping]] = ...) -> None: ...

class AddAttributeOutput(_message.Message):
    __slots__ = ["ern"]
    ERN_FIELD_NUMBER: _ClassVar[int]
    ern: str
    def __init__(self, ern: _Optional[str] = ...) -> None: ...

class AddMemberInput(_message.Message):
    __slots__ = ["member"]
    MEMBER_FIELD_NUMBER: _ClassVar[int]
    member: _member_pb2.Member
    def __init__(self, member: _Optional[_Union[_member_pb2.Member, _Mapping]] = ...) -> None: ...

class AddMemberOutput(_message.Message):
    __slots__ = ["ern", "member_id"]
    ERN_FIELD_NUMBER: _ClassVar[int]
    MEMBER_ID_FIELD_NUMBER: _ClassVar[int]
    ern: str
    member_id: str
    def __init__(self, ern: _Optional[str] = ..., member_id: _Optional[str] = ...) -> None: ...

class DescribeAttributeInput(_message.Message):
    __slots__ = ["attribute_key"]
    ATTRIBUTE_KEY_FIELD_NUMBER: _ClassVar[int]
    attribute_key: str
    def __init__(self, attribute_key: _Optional[str] = ...) -> None: ...

class DescribeAttributeOutput(_message.Message):
    __slots__ = ["attribute"]
    ATTRIBUTE_FIELD_NUMBER: _ClassVar[int]
    attribute: _attribute_pb2.Attribute
    def __init__(self, attribute: _Optional[_Union[_attribute_pb2.Attribute, _Mapping]] = ...) -> None: ...

class DescribeMemberInput(_message.Message):
    __slots__ = ["member_id"]
    MEMBER_ID_FIELD_NUMBER: _ClassVar[int]
    member_id: str
    def __init__(self, member_id: _Optional[str] = ...) -> None: ...

class DescribeMemberOutput(_message.Message):
    __slots__ = ["member"]
    MEMBER_FIELD_NUMBER: _ClassVar[int]
    member: _member_pb2.Member
    def __init__(self, member: _Optional[_Union[_member_pb2.Member, _Mapping]] = ...) -> None: ...

class IntrospectMemberInput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class IntrospectMemberOutput(_message.Message):
    __slots__ = ["member"]
    MEMBER_FIELD_NUMBER: _ClassVar[int]
    member: _member_pb2.Member
    def __init__(self, member: _Optional[_Union[_member_pb2.Member, _Mapping]] = ...) -> None: ...

class JoinSpaceInput(_message.Message):
    __slots__ = ["name", "values"]
    NAME_FIELD_NUMBER: _ClassVar[int]
    VALUES_FIELD_NUMBER: _ClassVar[int]
    name: str
    values: _containers.RepeatedCompositeFieldContainer[_member_pb2.Member.Value]
    def __init__(self, name: _Optional[str] = ..., values: _Optional[_Iterable[_Union[_member_pb2.Member.Value, _Mapping]]] = ...) -> None: ...

class JoinSpaceOutput(_message.Message):
    __slots__ = ["ern", "member_id"]
    ERN_FIELD_NUMBER: _ClassVar[int]
    MEMBER_ID_FIELD_NUMBER: _ClassVar[int]
    ern: str
    member_id: str
    def __init__(self, ern: _Optional[str] = ..., member_id: _Optional[str] = ...) -> None: ...

class LeaveSpaceInput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class LeaveSpaceOutput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ListAttributesInput(_message.Message):
    __slots__ = ["filters", "offset", "size"]
    class Filter(_message.Message):
        __slots__ = ["hidden", "id", "key", "required", "type"]
        HIDDEN_FIELD_NUMBER: _ClassVar[int]
        ID_FIELD_NUMBER: _ClassVar[int]
        KEY_FIELD_NUMBER: _ClassVar[int]
        REQUIRED_FIELD_NUMBER: _ClassVar[int]
        TYPE_FIELD_NUMBER: _ClassVar[int]
        hidden: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionBool]
        id: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionID]
        key: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionEnum]
        required: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionBool]
        type: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionEnum]
        def __init__(self, id: _Optional[_Iterable[_Union[_expression_pb2.ExpressionID, _Mapping]]] = ..., key: _Optional[_Iterable[_Union[_expression_pb2.ExpressionEnum, _Mapping]]] = ..., hidden: _Optional[_Iterable[_Union[_expression_pb2.ExpressionBool, _Mapping]]] = ..., required: _Optional[_Iterable[_Union[_expression_pb2.ExpressionBool, _Mapping]]] = ..., type: _Optional[_Iterable[_Union[_expression_pb2.ExpressionEnum, _Mapping]]] = ...) -> None: ...
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    filters: ListAttributesInput.Filter
    offset: int
    size: int
    def __init__(self, offset: _Optional[int] = ..., size: _Optional[int] = ..., filters: _Optional[_Union[ListAttributesInput.Filter, _Mapping]] = ...) -> None: ...

class ListAttributesOutput(_message.Message):
    __slots__ = ["items", "total"]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[_attribute_pb2.Attribute]
    total: int
    def __init__(self, total: _Optional[int] = ..., items: _Optional[_Iterable[_Union[_attribute_pb2.Attribute, _Mapping]]] = ...) -> None: ...

class ListMembersInput(_message.Message):
    __slots__ = ["filters", "offset", "size"]
    class Filter(_message.Message):
        __slots__ = ["disabled", "id", "name", "user_id"]
        DISABLED_FIELD_NUMBER: _ClassVar[int]
        ID_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        USER_ID_FIELD_NUMBER: _ClassVar[int]
        disabled: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionBool]
        id: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionID]
        name: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionString]
        user_id: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionID]
        def __init__(self, id: _Optional[_Iterable[_Union[_expression_pb2.ExpressionID, _Mapping]]] = ..., user_id: _Optional[_Iterable[_Union[_expression_pb2.ExpressionID, _Mapping]]] = ..., disabled: _Optional[_Iterable[_Union[_expression_pb2.ExpressionBool, _Mapping]]] = ..., name: _Optional[_Iterable[_Union[_expression_pb2.ExpressionString, _Mapping]]] = ...) -> None: ...
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    filters: ListMembersInput.Filter
    offset: int
    size: int
    def __init__(self, offset: _Optional[int] = ..., size: _Optional[int] = ..., filters: _Optional[_Union[ListMembersInput.Filter, _Mapping]] = ...) -> None: ...

class ListMembersOutput(_message.Message):
    __slots__ = ["items", "total"]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[_member_pb2.Member]
    total: int
    def __init__(self, total: _Optional[int] = ..., items: _Optional[_Iterable[_Union[_member_pb2.Member, _Mapping]]] = ...) -> None: ...

class RegisterMemberInput(_message.Message):
    __slots__ = ["values"]
    VALUES_FIELD_NUMBER: _ClassVar[int]
    values: _containers.RepeatedCompositeFieldContainer[_member_pb2.Member.Value]
    def __init__(self, values: _Optional[_Iterable[_Union[_member_pb2.Member.Value, _Mapping]]] = ...) -> None: ...

class RegisterMemberOutput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class RemoveAttributeInput(_message.Message):
    __slots__ = ["attribute_key"]
    ATTRIBUTE_KEY_FIELD_NUMBER: _ClassVar[int]
    attribute_key: str
    def __init__(self, attribute_key: _Optional[str] = ...) -> None: ...

class RemoveAttributeOutput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class RemoveMemberInput(_message.Message):
    __slots__ = ["member_id"]
    MEMBER_ID_FIELD_NUMBER: _ClassVar[int]
    member_id: str
    def __init__(self, member_id: _Optional[str] = ...) -> None: ...

class RemoveMemberOutput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class UpdateAttributeInput(_message.Message):
    __slots__ = ["attribute", "attribute_key"]
    ATTRIBUTE_FIELD_NUMBER: _ClassVar[int]
    ATTRIBUTE_KEY_FIELD_NUMBER: _ClassVar[int]
    attribute: _attribute_pb2.Attribute
    attribute_key: str
    def __init__(self, attribute_key: _Optional[str] = ..., attribute: _Optional[_Union[_attribute_pb2.Attribute, _Mapping]] = ...) -> None: ...

class UpdateAttributeOutput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class UpdateMemberInput(_message.Message):
    __slots__ = ["member", "member_id"]
    MEMBER_FIELD_NUMBER: _ClassVar[int]
    MEMBER_ID_FIELD_NUMBER: _ClassVar[int]
    member: _member_pb2.Member
    member_id: str
    def __init__(self, member_id: _Optional[str] = ..., member: _Optional[_Union[_member_pb2.Member, _Mapping]] = ...) -> None: ...

class UpdateMemberOutput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...
