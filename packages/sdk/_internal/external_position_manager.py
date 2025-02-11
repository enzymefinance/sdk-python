from typing import TypedDict
from web3.types import ChecksumAddress, HexStr, TxParams
from eth_abi import encode, decode
from web3 import Web3
from ..utils.clients import WalletClient
from .extensions import call_extension


ACTION = {
    "create_external_position": 0,
    "call_on_external_position": 1,
    "remove_external_position": 2,
    "reactivate_external_position": 3,
}


# TODO: finish make_use() and make_create_and_use()

# class UseParams(TypedDict):
#     comptroller_proxy: ChecksumAddress
#     external_position_manager: ChecksumAddress
#     external_position_proxy: ChecksumAddress
#     call_args: HexStr

# async def make_use(action: int, encode: Callable) -> Callable:
#     return lambda args: call(args, action, encode(args))


# async def make_create_and_use(action: int, encode: Callable) -> Callable:
#     return lambda args: create_and_use(args, action, encode(args))


# --------------------------------------------------------------------------------------------
# CALL ON EXTERNAL POSITION
# --------------------------------------------------------------------------------------------

CALL_ENCODING = [
    {
        "name": "externalPositionProxy",
        "type": "address",
    },
    {
        "name": "actionId",
        "type": "uint256",
    },
    {
        "name": "actionArgs",
        "type": "bytes",
    },
]


class CallArgs(TypedDict):
    external_position_proxy: ChecksumAddress
    action_id: int
    action_args: HexStr = "0x"


def call_encode(args: CallArgs) -> HexStr:
    types = [e["type"] for e in CALL_ENCODING]
    values = [
        args["external_position_proxy"],
        args["action_id"],
        Web3.to_bytes(hexstr=args["action_args"]),
    ]
    return encode(types, values)


def call_decode(encoded: HexStr) -> CallArgs:
    [external_position_proxy, action_id, action_args] = decode(CALL_ENCODING, encoded)
    return CallArgs(
        external_position_proxy=external_position_proxy,
        action_id=action_id,
        action_args=action_args,
    )


async def call(
    client: WalletClient,
    comptroller_proxy: ChecksumAddress,
    external_position_manager: ChecksumAddress,
    external_position_proxy: ChecksumAddress,
    action_id: int,
    action_args: HexStr = "0x",
) -> TxParams:
    call_args = CallArgs(
        external_position_proxy=external_position_proxy,
        action_id=action_id,
        action_args=action_args,
    )
    return await call_extension(
        client,
        comptroller_proxy,
        external_position_manager,
        ACTION["call_on_external_position"],
        call_encode(call_args),
    )


# --------------------------------------------------------------------------------------------
# CREATE EXTERNAL POSITION
# --------------------------------------------------------------------------------------------

CREATE_ENCODING = [
    {
        "name": "typeId",
        "type": "uint256",
    },
    {
        "name": "initializationData",
        "type": "bytes",
    },
    {
        "name": "callOnExternalPositionCallArgs",
        "type": "bytes",
    },
]


class CreateArgs(TypedDict):
    type_id: int
    initialization_data: HexStr = "0x"
    call_on_external_position_call_args: HexStr = "0x"


def create_encode(args: CreateArgs) -> HexStr:
    types = [e["type"] for e in CREATE_ENCODING]
    values = [
        args["type_id"],
        Web3.to_bytes(hexstr=args["initialization_data"]),
        Web3.to_bytes(hexstr=args["call_on_external_position_call_args"]),
    ]
    return encode(types, values)


def create_decode(encoded: HexStr) -> CreateArgs:
    decoded = decode(CREATE_ENCODING, Web3.to_bytes(hexstr=encoded))
    return CreateArgs(
        type_id=decoded[0],
        initialization_data=Web3.to_hex(decoded[1]),
        call_on_external_position_call_args=Web3.to_hex(decoded[2]),
    )


async def create(
    client: WalletClient,
    type_id: int,
    comptroller_proxy: ChecksumAddress,
    external_position_manager: ChecksumAddress,
    initialization_data: HexStr = "0x",
    call_args: HexStr = "0x",
) -> TxParams:
    create_args = CreateArgs(
        type_id=type_id,
        initialization_data=initialization_data,
        call_on_external_position_call_args=call_args,
    )
    return await call_extension(
        client,
        comptroller_proxy,
        external_position_manager,
        ACTION["create_external_position"],
        create_encode(create_args),
    )


async def create_only(
    client: WalletClient,
    type_id: int,
    comptroller_proxy: ChecksumAddress,
    external_position_manager: ChecksumAddress,
    initialization_data: HexStr = "0x",
) -> TxParams:
    return await create(
        client,
        type_id,
        comptroller_proxy,
        external_position_manager,
        initialization_data,
        "0x",
    )


# --------------------------------------------------------------------------------------------
# REACTIVATE EXTERNAL POSITION
# --------------------------------------------------------------------------------------------

REACTIVATE_ENCODING = [
    {
        "name": "externalPosition",
        "type": "address",
    },
]


class ReactivateArgs(TypedDict):
    external_position: ChecksumAddress


def reactivate_encode(args: ReactivateArgs) -> HexStr:
    types = [e["type"] for e in REACTIVATE_ENCODING]
    values = [args["external_position"]]
    return encode(types, values)


def reactivate_decode(encoded: HexStr) -> ReactivateArgs:
    decoded = decode(REACTIVATE_ENCODING, Web3.to_bytes(hexstr=encoded))
    return ReactivateArgs(external_position=decoded[0])


async def reactivate(
    client: WalletClient,
    comptroller_proxy: ChecksumAddress,
    external_position_manager: ChecksumAddress,
    external_position_proxy: ChecksumAddress,
) -> TxParams:
    reactivate_args = ReactivateArgs(external_position=external_position_proxy)
    return await call_extension(
        client,
        comptroller_proxy,
        external_position_manager,
        ACTION["reactivate_external_position"],
        reactivate_encode(reactivate_args),
    )


# --------------------------------------------------------------------------------------------
# REMOVE EXTERNAL POSITION
# --------------------------------------------------------------------------------------------

REMOVE_ENCODING = [
    {
        "name": "externalPositionProxy",
        "type": "address",
    },
]


class RemoveArgs(TypedDict):
    external_position_proxy: ChecksumAddress


def remove_encode(args: RemoveArgs) -> HexStr:
    types = [e["type"] for e in REMOVE_ENCODING]
    values = [args["external_position_proxy"]]
    return encode(types, values)


def remove_decode(encoded: HexStr) -> RemoveArgs:
    decoded = decode(REMOVE_ENCODING, Web3.to_bytes(hexstr=encoded))
    return RemoveArgs(external_position_proxy=decoded[0])


async def remove(
    client: WalletClient,
    comptroller_proxy: ChecksumAddress,
    external_position_manager: ChecksumAddress,
    external_position_proxy: ChecksumAddress,
) -> TxParams:
    remove_args = RemoveArgs(external_position_proxy=external_position_proxy)
    return await call_extension(
        client,
        comptroller_proxy,
        external_position_manager,
        ACTION["remove_external_position"],
        remove_encode(remove_args),
    )
