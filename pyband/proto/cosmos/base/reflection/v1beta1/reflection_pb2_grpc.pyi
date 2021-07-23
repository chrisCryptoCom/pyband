"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import abc
import grpc

from .reflection_pb2 import *
class ReflectionServiceStub:
    def __init__(self, channel: grpc.Channel) -> None: ...
    ListAllInterfaces:grpc.UnaryUnaryMultiCallable[
        global___ListAllInterfacesRequest,
        global___ListAllInterfacesResponse] = ...

    ListImplementations:grpc.UnaryUnaryMultiCallable[
        global___ListImplementationsRequest,
        global___ListImplementationsResponse] = ...


class ReflectionServiceServicer(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def ListAllInterfaces(self,
        request: global___ListAllInterfacesRequest,
        context: grpc.ServicerContext,
    ) -> global___ListAllInterfacesResponse: ...

    @abc.abstractmethod
    def ListImplementations(self,
        request: global___ListImplementationsRequest,
        context: grpc.ServicerContext,
    ) -> global___ListImplementationsResponse: ...


def add_ReflectionServiceServicer_to_server(servicer: ReflectionServiceServicer, server: grpc.Server) -> None: ...
