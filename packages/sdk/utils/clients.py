import asyncio
from pathlib import Path
import json
from web3 import AsyncWeb3
from web3.types import TContractFn, HexBytes, TxParams
from web3.contract import AsyncContract
from web3.middleware import ExtraDataToPOAMiddleware, SignAndSendRawMiddlewareBuilder


# create PublicClient and WalletClient
# pass clients to the vault.py
# check if transaction methods should return a transaction or function


class PublicClient:
    def __init__(self, rpc_url: str):
        self.w3 = AsyncWeb3(AsyncWeb3.AsyncHTTPProvider(rpc_url))
        self.w3.middleware_onion.inject(ExtraDataToPOAMiddleware, layer=0)

        self._contracts = {}

    def contract(self, address: str, abi_name: str) -> AsyncContract:
        if address not in self._contracts:
            abi = self._load_abi(abi_name)
            self._contracts[address] = self.w3.eth.contract(address=address, abi=abi)
        return self._contracts[address]

    def _load_abi(self, abi_name: str) -> list[dict]:
        path = Path(__file__).parents[2] / "abis" / "abis" / f"{abi_name}.abi.json"
        print(path)
        with open(path, "r") as f:
            return json.load(f)


class WalletClient(PublicClient):
    def __init__(
        self,
        rpc_url: str,
        chain_id: int,
        private_key: str,
    ):
        super().__init__(rpc_url)
        self.chain_id = chain_id
        self.account = self.w3.eth.account.from_key(private_key)

    async def populated_transaction(self, function: TContractFn) -> TxParams:
        from_address = self.account.address
        nonce = await self.w3.eth.get_transaction_count(from_address)

        transaction_payload = {
            "nonce": nonce,
            "from": from_address,
            "chainId": self.chain_id,
        }

        return await function.build_transaction(transaction_payload)

    async def send_transaction(self, transaction: TxParams) -> HexBytes:
        gas = await self.w3.eth.estimate_gas(transaction)
        print(gas)
        signed_transaction = self.w3.eth.account.sign_transaction(
            transaction, self.account.key
        )
        print(signed_transaction)
        return await self.w3.eth.send_raw_transaction(
            signed_transaction.raw_transaction
        )
