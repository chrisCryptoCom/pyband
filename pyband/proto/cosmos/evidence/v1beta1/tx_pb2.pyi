"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.any_pb2
import google.protobuf.descriptor
import google.protobuf.message
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

class MsgSubmitEvidence(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    SUBMITTER_FIELD_NUMBER: builtins.int
    EVIDENCE_FIELD_NUMBER: builtins.int
    submitter: typing.Text = ...

    @property
    def evidence(self) -> google.protobuf.any_pb2.Any: ...

    def __init__(self,
        *,
        submitter : typing.Text = ...,
        evidence : typing.Optional[google.protobuf.any_pb2.Any] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"evidence",b"evidence"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"evidence",b"evidence",u"submitter",b"submitter"]) -> None: ...
global___MsgSubmitEvidence = MsgSubmitEvidence

class MsgSubmitEvidenceResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    HASH_FIELD_NUMBER: builtins.int
    hash: builtins.bytes = ...

    def __init__(self,
        *,
        hash : builtins.bytes = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"hash",b"hash"]) -> None: ...
global___MsgSubmitEvidenceResponse = MsgSubmitEvidenceResponse
