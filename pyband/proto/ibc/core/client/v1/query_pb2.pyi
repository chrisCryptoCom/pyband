"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import cosmos.base.query.v1beta1.pagination_pb2
import google.protobuf.any_pb2
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import ibc.core.client.v1.client_pb2
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

class QueryClientStateRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    CLIENT_ID_FIELD_NUMBER: builtins.int
    client_id: typing.Text = ...

    def __init__(self,
        *,
        client_id : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"client_id",b"client_id"]) -> None: ...
global___QueryClientStateRequest = QueryClientStateRequest

class QueryClientStateResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    CLIENT_STATE_FIELD_NUMBER: builtins.int
    PROOF_FIELD_NUMBER: builtins.int
    PROOF_HEIGHT_FIELD_NUMBER: builtins.int
    proof: builtins.bytes = ...

    @property
    def client_state(self) -> google.protobuf.any_pb2.Any: ...

    @property
    def proof_height(self) -> ibc.core.client.v1.client_pb2.Height: ...

    def __init__(self,
        *,
        client_state : typing.Optional[google.protobuf.any_pb2.Any] = ...,
        proof : builtins.bytes = ...,
        proof_height : typing.Optional[ibc.core.client.v1.client_pb2.Height] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"client_state",b"client_state",u"proof_height",b"proof_height"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"client_state",b"client_state",u"proof",b"proof",u"proof_height",b"proof_height"]) -> None: ...
global___QueryClientStateResponse = QueryClientStateResponse

class QueryClientStatesRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    PAGINATION_FIELD_NUMBER: builtins.int

    @property
    def pagination(self) -> cosmos.base.query.v1beta1.pagination_pb2.PageRequest: ...

    def __init__(self,
        *,
        pagination : typing.Optional[cosmos.base.query.v1beta1.pagination_pb2.PageRequest] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"pagination",b"pagination"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"pagination",b"pagination"]) -> None: ...
global___QueryClientStatesRequest = QueryClientStatesRequest

class QueryClientStatesResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    CLIENT_STATES_FIELD_NUMBER: builtins.int
    PAGINATION_FIELD_NUMBER: builtins.int

    @property
    def client_states(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[ibc.core.client.v1.client_pb2.IdentifiedClientState]: ...

    @property
    def pagination(self) -> cosmos.base.query.v1beta1.pagination_pb2.PageResponse: ...

    def __init__(self,
        *,
        client_states : typing.Optional[typing.Iterable[ibc.core.client.v1.client_pb2.IdentifiedClientState]] = ...,
        pagination : typing.Optional[cosmos.base.query.v1beta1.pagination_pb2.PageResponse] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"pagination",b"pagination"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"client_states",b"client_states",u"pagination",b"pagination"]) -> None: ...
global___QueryClientStatesResponse = QueryClientStatesResponse

class QueryConsensusStateRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    CLIENT_ID_FIELD_NUMBER: builtins.int
    REVISION_NUMBER_FIELD_NUMBER: builtins.int
    REVISION_HEIGHT_FIELD_NUMBER: builtins.int
    LATEST_HEIGHT_FIELD_NUMBER: builtins.int
    client_id: typing.Text = ...
    revision_number: builtins.int = ...
    revision_height: builtins.int = ...
    latest_height: builtins.bool = ...

    def __init__(self,
        *,
        client_id : typing.Text = ...,
        revision_number : builtins.int = ...,
        revision_height : builtins.int = ...,
        latest_height : builtins.bool = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"client_id",b"client_id",u"latest_height",b"latest_height",u"revision_height",b"revision_height",u"revision_number",b"revision_number"]) -> None: ...
global___QueryConsensusStateRequest = QueryConsensusStateRequest

class QueryConsensusStateResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    CONSENSUS_STATE_FIELD_NUMBER: builtins.int
    PROOF_FIELD_NUMBER: builtins.int
    PROOF_HEIGHT_FIELD_NUMBER: builtins.int
    proof: builtins.bytes = ...

    @property
    def consensus_state(self) -> google.protobuf.any_pb2.Any: ...

    @property
    def proof_height(self) -> ibc.core.client.v1.client_pb2.Height: ...

    def __init__(self,
        *,
        consensus_state : typing.Optional[google.protobuf.any_pb2.Any] = ...,
        proof : builtins.bytes = ...,
        proof_height : typing.Optional[ibc.core.client.v1.client_pb2.Height] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"consensus_state",b"consensus_state",u"proof_height",b"proof_height"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"consensus_state",b"consensus_state",u"proof",b"proof",u"proof_height",b"proof_height"]) -> None: ...
global___QueryConsensusStateResponse = QueryConsensusStateResponse

class QueryConsensusStatesRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    CLIENT_ID_FIELD_NUMBER: builtins.int
    PAGINATION_FIELD_NUMBER: builtins.int
    client_id: typing.Text = ...

    @property
    def pagination(self) -> cosmos.base.query.v1beta1.pagination_pb2.PageRequest: ...

    def __init__(self,
        *,
        client_id : typing.Text = ...,
        pagination : typing.Optional[cosmos.base.query.v1beta1.pagination_pb2.PageRequest] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"pagination",b"pagination"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"client_id",b"client_id",u"pagination",b"pagination"]) -> None: ...
global___QueryConsensusStatesRequest = QueryConsensusStatesRequest

class QueryConsensusStatesResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    CONSENSUS_STATES_FIELD_NUMBER: builtins.int
    PAGINATION_FIELD_NUMBER: builtins.int

    @property
    def consensus_states(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[ibc.core.client.v1.client_pb2.ConsensusStateWithHeight]: ...

    @property
    def pagination(self) -> cosmos.base.query.v1beta1.pagination_pb2.PageResponse: ...

    def __init__(self,
        *,
        consensus_states : typing.Optional[typing.Iterable[ibc.core.client.v1.client_pb2.ConsensusStateWithHeight]] = ...,
        pagination : typing.Optional[cosmos.base.query.v1beta1.pagination_pb2.PageResponse] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"pagination",b"pagination"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"consensus_states",b"consensus_states",u"pagination",b"pagination"]) -> None: ...
global___QueryConsensusStatesResponse = QueryConsensusStatesResponse

class QueryClientParamsRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...

    def __init__(self,
        ) -> None: ...
global___QueryClientParamsRequest = QueryClientParamsRequest

class QueryClientParamsResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    PARAMS_FIELD_NUMBER: builtins.int

    @property
    def params(self) -> ibc.core.client.v1.client_pb2.Params: ...

    def __init__(self,
        *,
        params : typing.Optional[ibc.core.client.v1.client_pb2.Params] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"params",b"params"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"params",b"params"]) -> None: ...
global___QueryClientParamsResponse = QueryClientParamsResponse
