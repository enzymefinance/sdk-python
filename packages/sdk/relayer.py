from web3 import Web3
from web3.types import ChecksumAddress, TxParams, HexStr
from web3.constants import ADDRESS_ZERO
from .utils.clients import PublicClient, WalletClient
from eth_abi import encode


RELAY_HUB_ABI = [
    {
        "inputs": [
            {
                "internalType": "uint256",
                "name": "maxAcceptanceBudget",
                "type": "uint256",
            },
            {
                "components": [
                    {
                        "components": [
                            {
                                "internalType": "address",
                                "name": "from",
                                "type": "address",
                            },
                            {
                                "internalType": "address",
                                "name": "to",
                                "type": "address",
                            },
                            {
                                "internalType": "uint256",
                                "name": "value",
                                "type": "uint256",
                            },
                            {
                                "internalType": "uint256",
                                "name": "gas",
                                "type": "uint256",
                            },
                            {
                                "internalType": "uint256",
                                "name": "nonce",
                                "type": "uint256",
                            },
                            {"internalType": "bytes", "name": "data", "type": "bytes"},
                            {
                                "internalType": "uint256",
                                "name": "validUntil",
                                "type": "uint256",
                            },
                        ],
                        "internalType": "struct IForwarder.ForwardRequest",
                        "name": "request",
                        "type": "tuple",
                    },
                    {
                        "components": [
                            {
                                "internalType": "uint256",
                                "name": "gasPrice",
                                "type": "uint256",
                            },
                            {
                                "internalType": "uint256",
                                "name": "pctRelayFee",
                                "type": "uint256",
                            },
                            {
                                "internalType": "uint256",
                                "name": "baseRelayFee",
                                "type": "uint256",
                            },
                            {
                                "internalType": "address",
                                "name": "relayWorker",
                                "type": "address",
                            },
                            {
                                "internalType": "address",
                                "name": "paymaster",
                                "type": "address",
                            },
                            {
                                "internalType": "address",
                                "name": "forwarder",
                                "type": "address",
                            },
                            {
                                "internalType": "bytes",
                                "name": "paymasterData",
                                "type": "bytes",
                            },
                            {
                                "internalType": "uint256",
                                "name": "clientId",
                                "type": "uint256",
                            },
                        ],
                        "internalType": "struct GsnTypes.RelayData",
                        "name": "relayData",
                        "type": "tuple",
                    },
                ],
                "internalType": "struct GsnTypes.RelayRequest",
                "name": "relayRequest",
                "type": "tuple",
            },
            {"internalType": "bytes", "name": "signature", "type": "bytes"},
            {"internalType": "bytes", "name": "approvalData", "type": "bytes"},
            {"internalType": "uint256", "name": "externalGasLimit", "type": "uint256"},
        ],
        "name": "relayCall",
        "outputs": [
            {"internalType": "bool", "name": "paymasterAccepted", "type": "bool"},
            {"internalType": "bytes", "name": "returnValue", "type": "bytes"},
        ],
        "stateMutability": "nonpayable",
        "type": "function",
    },
]

RELAY_REQUEST_TYPES = {
    "RelayData": [
        {"name": "gasPrice", "type": "uint256"},
        {"name": "pctRelayFee", "type": "uint256"},
        {"name": "baseRelayFee", "type": "uint256"},
        {"name": "relayWorker", "type": "address"},
        {"name": "paymaster", "type": "address"},
        {"name": "forwarder", "type": "address"},
        {"name": "paymasterData", "type": "bytes"},
        {"name": "clientId", "type": "uint256"},
    ],
    "RelayRequest": [
        {"name": "from", "type": "address"},
        {"name": "to", "type": "address"},
        {"name": "value", "type": "uint256"},
        {"name": "gas", "type": "uint256"},
        {"name": "nonce", "type": "uint256"},
        {"name": "data", "type": "bytes"},
        {"name": "validUntil", "type": "uint256"},
        {"name": "relayData", "type": "RelayData"},
    ],
}


# --------------------------------------------------------------------------------------------
# TRANSACTIONS
# --------------------------------------------------------------------------------------------


async def deploy_gas_relay_paymaster(
    client: WalletClient,
    comptroller_proxy: ChecksumAddress,
) -> TxParams:
    contract = client.contract(comptroller_proxy, "IComptrollerLib")
    function = contract.functions.deployGasRelayPaymaster()
    return await client.populated_transaction(function)


async def deposit_to_gas_relay_paymaster(
    client: WalletClient,
    comptroller_proxy: ChecksumAddress,
) -> TxParams:
    contract = client.contract(comptroller_proxy, "IComptrollerLib")
    function = contract.functions.depositToGasRelayPaymaster()
    return await client.populated_transaction(function)


async def shutdown_gas_relay_paymaster(
    client: WalletClient,
    comptroller_proxy: ChecksumAddress,
) -> TxParams:
    contract = client.contract(comptroller_proxy, "IComptrollerLib")
    function = contract.functions.shutdownGasRelayPaymaster()
    return await client.populated_transaction(function)


# --------------------------------------------------------------------------------------------
# READ FUNCTIONS
# --------------------------------------------------------------------------------------------


async def is_relayer_enabled(
    client: PublicClient,
    comptroller_proxy: ChecksumAddress,
) -> bool:
    contract = client.contract(comptroller_proxy, "IComptrollerLib")
    gas_relay_paymaster_address = await contract.functions.getGasRelayPaymaster().call()
    return gas_relay_paymaster_address != ADDRESS_ZERO


async def get_gas_relay_paymaster(
    client: PublicClient,
    comptroller_proxy: ChecksumAddress,
) -> ChecksumAddress:
    contract = client.contract(comptroller_proxy, "IComptrollerLib")
    return await contract.functions.getGasRelayPaymaster().call()


async def get_relayer_balance(
    client: PublicClient,
    gas_relay_paymaster: ChecksumAddress,
) -> int:
    contract = client.contract(gas_relay_paymaster, "IGasRelayPaymasterLib")
    return await contract.functions.getRelayHubDeposit().call()


async def get_trusted_forwarder(
    client: PublicClient,
    gas_relay_paymaster: ChecksumAddress,
) -> ChecksumAddress:
    contract = client.contract(gas_relay_paymaster, "IGasRelayPaymasterLib")
    return await contract.functions.trustedForwarder().call()


async def get_nonce(
    client: PublicClient,
    trusted_forwarder: ChecksumAddress,
    sender: ChecksumAddress,
) -> int:
    contract = client.contract(trusted_forwarder, "IForwarder")
    return await contract.functions.getNonce(sender).call()


def encode_relay_call_data(
    max_acceptance_budget: int,
    relay_request: dict,
    signature: HexStr,
    approval_data: HexStr,
    gas_limit: int,
) -> HexStr:
    contract = Web3().eth.contract(abi=RELAY_HUB_ABI)
    return contract.encode_abi(
        "relayCall",
        [
            max_acceptance_budget,
            relay_request,
            signature,
            approval_data,
            gas_limit,
        ],
    )
