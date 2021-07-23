"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

class CommitInfo(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    VERSION_FIELD_NUMBER: builtins.int
    STORE_INFOS_FIELD_NUMBER: builtins.int
    version: builtins.int = ...

    @property
    def store_infos(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___StoreInfo]: ...

    def __init__(self,
        *,
        version : builtins.int = ...,
        store_infos : typing.Optional[typing.Iterable[global___StoreInfo]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"store_infos",b"store_infos",u"version",b"version"]) -> None: ...
global___CommitInfo = CommitInfo

class StoreInfo(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    NAME_FIELD_NUMBER: builtins.int
    COMMIT_ID_FIELD_NUMBER: builtins.int
    name: typing.Text = ...

    @property
    def commit_id(self) -> global___CommitID: ...

    def __init__(self,
        *,
        name : typing.Text = ...,
        commit_id : typing.Optional[global___CommitID] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"commit_id",b"commit_id"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"commit_id",b"commit_id",u"name",b"name"]) -> None: ...
global___StoreInfo = StoreInfo

class CommitID(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    VERSION_FIELD_NUMBER: builtins.int
    HASH_FIELD_NUMBER: builtins.int
    version: builtins.int = ...
    hash: builtins.bytes = ...

    def __init__(self,
        *,
        version : builtins.int = ...,
        hash : builtins.bytes = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"hash",b"hash",u"version",b"version"]) -> None: ...
global___CommitID = CommitID
