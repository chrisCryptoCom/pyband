# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: cosmos/auth/v1beta1/auth.proto, cosmos/auth/v1beta1/genesis.proto, cosmos/auth/v1beta1/query.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import (
    TYPE_CHECKING,
    Dict,
    List,
    Optional,
)

import betterproto
import betterproto.lib.google.protobuf as betterproto_lib_google_protobuf
import grpclib
from betterproto.grpc.grpclib_server import ServiceBase

from ...base.query import v1beta1 as __base_query_v1_beta1__


if TYPE_CHECKING:
    import grpclib.server
    from betterproto.grpc.grpclib_client import MetadataLike
    from grpclib.metadata import Deadline


@dataclass(eq=False, repr=False)
class BaseAccount(betterproto.Message):
    """
    BaseAccount defines a base account type. It contains all the necessary
    fields for basic account functionality. Any custom account type should
    extend this type for additional functionality (e.g. vesting).
    """

    address: str = betterproto.string_field(1)
    pub_key: "betterproto_lib_google_protobuf.Any" = betterproto.message_field(2)
    account_number: int = betterproto.uint64_field(3)
    sequence: int = betterproto.uint64_field(4)


@dataclass(eq=False, repr=False)
class ModuleAccount(betterproto.Message):
    """
    ModuleAccount defines an account for modules that holds coins on a pool.
    """

    base_account: "BaseAccount" = betterproto.message_field(1)
    name: str = betterproto.string_field(2)
    permissions: List[str] = betterproto.string_field(3)


@dataclass(eq=False, repr=False)
class Params(betterproto.Message):
    """Params defines the parameters for the auth module."""

    max_memo_characters: int = betterproto.uint64_field(1)
    tx_sig_limit: int = betterproto.uint64_field(2)
    tx_size_cost_per_byte: int = betterproto.uint64_field(3)
    sig_verify_cost_ed25519: int = betterproto.uint64_field(4)
    sig_verify_cost_secp256_k1: int = betterproto.uint64_field(5)


@dataclass(eq=False, repr=False)
class QueryAccountsRequest(betterproto.Message):
    """
    QueryAccountsRequest is the request type for the Query/Accounts RPC method.
    Since: cosmos-sdk 0.43
    """

    pagination: "__base_query_v1_beta1__.PageRequest" = betterproto.message_field(1)
    """pagination defines an optional pagination for the request."""


@dataclass(eq=False, repr=False)
class QueryAccountsResponse(betterproto.Message):
    """
    QueryAccountsResponse is the response type for the Query/Accounts RPC
    method. Since: cosmos-sdk 0.43
    """

    accounts: List["betterproto_lib_google_protobuf.Any"] = betterproto.message_field(1)
    """accounts are the existing accounts"""

    pagination: "__base_query_v1_beta1__.PageResponse" = betterproto.message_field(2)
    """pagination defines the pagination in the response."""


@dataclass(eq=False, repr=False)
class QueryAccountRequest(betterproto.Message):
    """
    QueryAccountRequest is the request type for the Query/Account RPC method.
    """

    address: str = betterproto.string_field(1)
    """address defines the address to query for."""


@dataclass(eq=False, repr=False)
class QueryAccountResponse(betterproto.Message):
    """
    QueryAccountResponse is the response type for the Query/Account RPC method.
    """

    account: "betterproto_lib_google_protobuf.Any" = betterproto.message_field(1)
    """account defines the account of the corresponding address."""


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
class GenesisState(betterproto.Message):
    """GenesisState defines the auth module's genesis state."""

    params: "Params" = betterproto.message_field(1)
    """params defines all the paramaters of the module."""

    accounts: List["betterproto_lib_google_protobuf.Any"] = betterproto.message_field(2)
    """accounts are the accounts present at genesis."""


class QueryStub(betterproto.ServiceStub):
    async def accounts(
        self,
        query_accounts_request: "QueryAccountsRequest",
        *,
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["MetadataLike"] = None
    ) -> "QueryAccountsResponse":
        return await self._unary_unary(
            "/cosmos.auth.v1beta1.Query/Accounts",
            query_accounts_request,
            QueryAccountsResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )

    async def account(
        self,
        query_account_request: "QueryAccountRequest",
        *,
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["MetadataLike"] = None
    ) -> "QueryAccountResponse":
        return await self._unary_unary(
            "/cosmos.auth.v1beta1.Query/Account",
            query_account_request,
            QueryAccountResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )

    async def params(
        self,
        query_params_request: "QueryParamsRequest",
        *,
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["MetadataLike"] = None
    ) -> "QueryParamsResponse":
        return await self._unary_unary(
            "/cosmos.auth.v1beta1.Query/Params",
            query_params_request,
            QueryParamsResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )


class QueryBase(ServiceBase):
    async def accounts(self, query_accounts_request: "QueryAccountsRequest") -> "QueryAccountsResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def account(self, query_account_request: "QueryAccountRequest") -> "QueryAccountResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def params(self, query_params_request: "QueryParamsRequest") -> "QueryParamsResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def __rpc_accounts(
        self,
        stream: "grpclib.server.Stream[QueryAccountsRequest, QueryAccountsResponse]",
    ) -> None:
        request = await stream.recv_message()
        response = await self.accounts(request)
        await stream.send_message(response)

    async def __rpc_account(self, stream: "grpclib.server.Stream[QueryAccountRequest, QueryAccountResponse]") -> None:
        request = await stream.recv_message()
        response = await self.account(request)
        await stream.send_message(response)

    async def __rpc_params(self, stream: "grpclib.server.Stream[QueryParamsRequest, QueryParamsResponse]") -> None:
        request = await stream.recv_message()
        response = await self.params(request)
        await stream.send_message(response)

    def __mapping__(self) -> Dict[str, grpclib.const.Handler]:
        return {
            "/cosmos.auth.v1beta1.Query/Accounts": grpclib.const.Handler(
                self.__rpc_accounts,
                grpclib.const.Cardinality.UNARY_UNARY,
                QueryAccountsRequest,
                QueryAccountsResponse,
            ),
            "/cosmos.auth.v1beta1.Query/Account": grpclib.const.Handler(
                self.__rpc_account,
                grpclib.const.Cardinality.UNARY_UNARY,
                QueryAccountRequest,
                QueryAccountResponse,
            ),
            "/cosmos.auth.v1beta1.Query/Params": grpclib.const.Handler(
                self.__rpc_params,
                grpclib.const.Cardinality.UNARY_UNARY,
                QueryParamsRequest,
                QueryParamsResponse,
            ),
        }
