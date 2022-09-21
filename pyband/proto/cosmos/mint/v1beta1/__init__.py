# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: cosmos/mint/v1beta1/genesis.proto, cosmos/mint/v1beta1/mint.proto, cosmos/mint/v1beta1/query.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import (
    TYPE_CHECKING,
    Dict,
    Optional,
)

import betterproto
import grpclib
from betterproto.grpc.grpclib_server import ServiceBase


if TYPE_CHECKING:
    import grpclib.server
    from betterproto.grpc.grpclib_client import MetadataLike
    from grpclib.metadata import Deadline


@dataclass(eq=False, repr=False)
class Minter(betterproto.Message):
    """Minter represents the minting state."""

    inflation: str = betterproto.string_field(1)
    """current annual inflation rate"""

    annual_provisions: str = betterproto.string_field(2)
    """current annual expected provisions"""


@dataclass(eq=False, repr=False)
class Params(betterproto.Message):
    """Params holds parameters for the mint module."""

    mint_denom: str = betterproto.string_field(1)
    """type of coin to mint"""

    inflation_rate_change: str = betterproto.string_field(2)
    """maximum annual change in inflation rate"""

    inflation_max: str = betterproto.string_field(3)
    """maximum inflation rate"""

    inflation_min: str = betterproto.string_field(4)
    """minimum inflation rate"""

    goal_bonded: str = betterproto.string_field(5)
    """goal of percent bonded atoms"""

    blocks_per_year: int = betterproto.uint64_field(6)
    """expected blocks per year"""


@dataclass(eq=False, repr=False)
class QueryParamsRequest(betterproto.Message):
    """
    QueryParamsRequest is the request type for the Query/Params RPC method.
    """

    pass


@dataclass(eq=False, repr=False)
class QueryParamsResponse(betterproto.Message):
    """
    QueryParamsResponse is the response type for the Query/Params RPC method.
    """

    params: "Params" = betterproto.message_field(1)
    """params defines the parameters of the module."""


@dataclass(eq=False, repr=False)
class QueryInflationRequest(betterproto.Message):
    """
    QueryInflationRequest is the request type for the Query/Inflation RPC
    method.
    """

    pass


@dataclass(eq=False, repr=False)
class QueryInflationResponse(betterproto.Message):
    """
    QueryInflationResponse is the response type for the Query/Inflation RPC
    method.
    """

    inflation: bytes = betterproto.bytes_field(1)
    """inflation is the current minting inflation value."""


@dataclass(eq=False, repr=False)
class QueryAnnualProvisionsRequest(betterproto.Message):
    """
    QueryAnnualProvisionsRequest is the request type for the
    Query/AnnualProvisions RPC method.
    """

    pass


@dataclass(eq=False, repr=False)
class QueryAnnualProvisionsResponse(betterproto.Message):
    """
    QueryAnnualProvisionsResponse is the response type for the
    Query/AnnualProvisions RPC method.
    """

    annual_provisions: bytes = betterproto.bytes_field(1)
    """annual_provisions is the current minting annual provisions value."""


@dataclass(eq=False, repr=False)
class GenesisState(betterproto.Message):
    """GenesisState defines the mint module's genesis state."""

    minter: "Minter" = betterproto.message_field(1)
    """minter is a space for holding current inflation information."""

    params: "Params" = betterproto.message_field(2)
    """params defines all the paramaters of the module."""


class QueryStub(betterproto.ServiceStub):
    async def params(
        self,
        query_params_request: "QueryParamsRequest",
        *,
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["MetadataLike"] = None
    ) -> "QueryParamsResponse":
        return await self._unary_unary(
            "/cosmos.mint.v1beta1.Query/Params",
            query_params_request,
            QueryParamsResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )

    async def inflation(
        self,
        query_inflation_request: "QueryInflationRequest",
        *,
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["MetadataLike"] = None
    ) -> "QueryInflationResponse":
        return await self._unary_unary(
            "/cosmos.mint.v1beta1.Query/Inflation",
            query_inflation_request,
            QueryInflationResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )

    async def annual_provisions(
        self,
        query_annual_provisions_request: "QueryAnnualProvisionsRequest",
        *,
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["MetadataLike"] = None
    ) -> "QueryAnnualProvisionsResponse":
        return await self._unary_unary(
            "/cosmos.mint.v1beta1.Query/AnnualProvisions",
            query_annual_provisions_request,
            QueryAnnualProvisionsResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )


class QueryBase(ServiceBase):
    async def params(self, query_params_request: "QueryParamsRequest") -> "QueryParamsResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def inflation(self, query_inflation_request: "QueryInflationRequest") -> "QueryInflationResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def annual_provisions(
        self, query_annual_provisions_request: "QueryAnnualProvisionsRequest"
    ) -> "QueryAnnualProvisionsResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def __rpc_params(self, stream: "grpclib.server.Stream[QueryParamsRequest, QueryParamsResponse]") -> None:
        request = await stream.recv_message()
        response = await self.params(request)
        await stream.send_message(response)

    async def __rpc_inflation(
        self,
        stream: "grpclib.server.Stream[QueryInflationRequest, QueryInflationResponse]",
    ) -> None:
        request = await stream.recv_message()
        response = await self.inflation(request)
        await stream.send_message(response)

    async def __rpc_annual_provisions(
        self,
        stream: "grpclib.server.Stream[QueryAnnualProvisionsRequest, QueryAnnualProvisionsResponse]",
    ) -> None:
        request = await stream.recv_message()
        response = await self.annual_provisions(request)
        await stream.send_message(response)

    def __mapping__(self) -> Dict[str, grpclib.const.Handler]:
        return {
            "/cosmos.mint.v1beta1.Query/Params": grpclib.const.Handler(
                self.__rpc_params,
                grpclib.const.Cardinality.UNARY_UNARY,
                QueryParamsRequest,
                QueryParamsResponse,
            ),
            "/cosmos.mint.v1beta1.Query/Inflation": grpclib.const.Handler(
                self.__rpc_inflation,
                grpclib.const.Cardinality.UNARY_UNARY,
                QueryInflationRequest,
                QueryInflationResponse,
            ),
            "/cosmos.mint.v1beta1.Query/AnnualProvisions": grpclib.const.Handler(
                self.__rpc_annual_provisions,
                grpclib.const.Cardinality.UNARY_UNARY,
                QueryAnnualProvisionsRequest,
                QueryAnnualProvisionsResponse,
            ),
        }
