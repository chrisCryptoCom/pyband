"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import abc
import grpc

from .tx_pb2 import *
class MsgStub:
    def __init__(self, channel: grpc.Channel) -> None: ...
    ChannelOpenInit:grpc.UnaryUnaryMultiCallable[
        global___MsgChannelOpenInit,
        global___MsgChannelOpenInitResponse] = ...

    ChannelOpenTry:grpc.UnaryUnaryMultiCallable[
        global___MsgChannelOpenTry,
        global___MsgChannelOpenTryResponse] = ...

    ChannelOpenAck:grpc.UnaryUnaryMultiCallable[
        global___MsgChannelOpenAck,
        global___MsgChannelOpenAckResponse] = ...

    ChannelOpenConfirm:grpc.UnaryUnaryMultiCallable[
        global___MsgChannelOpenConfirm,
        global___MsgChannelOpenConfirmResponse] = ...

    ChannelCloseInit:grpc.UnaryUnaryMultiCallable[
        global___MsgChannelCloseInit,
        global___MsgChannelCloseInitResponse] = ...

    ChannelCloseConfirm:grpc.UnaryUnaryMultiCallable[
        global___MsgChannelCloseConfirm,
        global___MsgChannelCloseConfirmResponse] = ...

    RecvPacket:grpc.UnaryUnaryMultiCallable[
        global___MsgRecvPacket,
        global___MsgRecvPacketResponse] = ...

    Timeout:grpc.UnaryUnaryMultiCallable[
        global___MsgTimeout,
        global___MsgTimeoutResponse] = ...

    TimeoutOnClose:grpc.UnaryUnaryMultiCallable[
        global___MsgTimeoutOnClose,
        global___MsgTimeoutOnCloseResponse] = ...

    Acknowledgement:grpc.UnaryUnaryMultiCallable[
        global___MsgAcknowledgement,
        global___MsgAcknowledgementResponse] = ...


class MsgServicer(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def ChannelOpenInit(self,
        request: global___MsgChannelOpenInit,
        context: grpc.ServicerContext,
    ) -> global___MsgChannelOpenInitResponse: ...

    @abc.abstractmethod
    def ChannelOpenTry(self,
        request: global___MsgChannelOpenTry,
        context: grpc.ServicerContext,
    ) -> global___MsgChannelOpenTryResponse: ...

    @abc.abstractmethod
    def ChannelOpenAck(self,
        request: global___MsgChannelOpenAck,
        context: grpc.ServicerContext,
    ) -> global___MsgChannelOpenAckResponse: ...

    @abc.abstractmethod
    def ChannelOpenConfirm(self,
        request: global___MsgChannelOpenConfirm,
        context: grpc.ServicerContext,
    ) -> global___MsgChannelOpenConfirmResponse: ...

    @abc.abstractmethod
    def ChannelCloseInit(self,
        request: global___MsgChannelCloseInit,
        context: grpc.ServicerContext,
    ) -> global___MsgChannelCloseInitResponse: ...

    @abc.abstractmethod
    def ChannelCloseConfirm(self,
        request: global___MsgChannelCloseConfirm,
        context: grpc.ServicerContext,
    ) -> global___MsgChannelCloseConfirmResponse: ...

    @abc.abstractmethod
    def RecvPacket(self,
        request: global___MsgRecvPacket,
        context: grpc.ServicerContext,
    ) -> global___MsgRecvPacketResponse: ...

    @abc.abstractmethod
    def Timeout(self,
        request: global___MsgTimeout,
        context: grpc.ServicerContext,
    ) -> global___MsgTimeoutResponse: ...

    @abc.abstractmethod
    def TimeoutOnClose(self,
        request: global___MsgTimeoutOnClose,
        context: grpc.ServicerContext,
    ) -> global___MsgTimeoutOnCloseResponse: ...

    @abc.abstractmethod
    def Acknowledgement(self,
        request: global___MsgAcknowledgement,
        context: grpc.ServicerContext,
    ) -> global___MsgAcknowledgementResponse: ...


def add_MsgServicer_to_server(servicer: MsgServicer, server: grpc.Server) -> None: ...
