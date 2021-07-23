"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import abc
import grpc

from .tx_pb2 import *
class MsgStub:
    def __init__(self, channel: grpc.Channel) -> None: ...
    Send:grpc.UnaryUnaryMultiCallable[
        global___MsgSend,
        global___MsgSendResponse] = ...

    MultiSend:grpc.UnaryUnaryMultiCallable[
        global___MsgMultiSend,
        global___MsgMultiSendResponse] = ...


class MsgServicer(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def Send(self,
        request: global___MsgSend,
        context: grpc.ServicerContext,
    ) -> global___MsgSendResponse: ...

    @abc.abstractmethod
    def MultiSend(self,
        request: global___MsgMultiSend,
        context: grpc.ServicerContext,
    ) -> global___MsgMultiSendResponse: ...


def add_MsgServicer_to_server(servicer: MsgServicer, server: grpc.Server) -> None: ...
