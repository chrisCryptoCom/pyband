"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import abc
import grpc

from .tx_pb2 import *
class MsgStub:
    def __init__(self, channel: grpc.Channel) -> None: ...
    CreateValidator:grpc.UnaryUnaryMultiCallable[
        global___MsgCreateValidator,
        global___MsgCreateValidatorResponse] = ...

    EditValidator:grpc.UnaryUnaryMultiCallable[
        global___MsgEditValidator,
        global___MsgEditValidatorResponse] = ...

    Delegate:grpc.UnaryUnaryMultiCallable[
        global___MsgDelegate,
        global___MsgDelegateResponse] = ...

    BeginRedelegate:grpc.UnaryUnaryMultiCallable[
        global___MsgBeginRedelegate,
        global___MsgBeginRedelegateResponse] = ...

    Undelegate:grpc.UnaryUnaryMultiCallable[
        global___MsgUndelegate,
        global___MsgUndelegateResponse] = ...


class MsgServicer(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def CreateValidator(self,
        request: global___MsgCreateValidator,
        context: grpc.ServicerContext,
    ) -> global___MsgCreateValidatorResponse: ...

    @abc.abstractmethod
    def EditValidator(self,
        request: global___MsgEditValidator,
        context: grpc.ServicerContext,
    ) -> global___MsgEditValidatorResponse: ...

    @abc.abstractmethod
    def Delegate(self,
        request: global___MsgDelegate,
        context: grpc.ServicerContext,
    ) -> global___MsgDelegateResponse: ...

    @abc.abstractmethod
    def BeginRedelegate(self,
        request: global___MsgBeginRedelegate,
        context: grpc.ServicerContext,
    ) -> global___MsgBeginRedelegateResponse: ...

    @abc.abstractmethod
    def Undelegate(self,
        request: global___MsgUndelegate,
        context: grpc.ServicerContext,
    ) -> global___MsgUndelegateResponse: ...


def add_MsgServicer_to_server(servicer: MsgServicer, server: grpc.Server) -> None: ...
