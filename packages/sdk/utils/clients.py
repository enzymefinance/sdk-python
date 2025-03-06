from web3 import AsyncWeb3
from web3.types import TContractFn, HexStr, TxParams
from web3.contract import AsyncContract
from web3.middleware import ExtraDataToPOAMiddleware
from ...abis import abis


class PublicClient:
    def __init__(self, rpc_url: str):
        self.w3 = AsyncWeb3(AsyncWeb3.AsyncHTTPProvider(rpc_url))
        self.w3.middleware_onion.inject(ExtraDataToPOAMiddleware, layer=0)

        self._contracts = {}

    def contract(self, address: str, abi_name: str) -> AsyncContract:
        key = f"{address}_{abi_name}"
        if key not in self._contracts:
            abi = abis.get(abi_name)
            self._contracts[key] = self.w3.eth.contract(address=address, abi=abi)
        return self._contracts[key]


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

    async def send_transaction(self, transaction: TxParams) -> HexStr:
        signed_transaction = self.w3.eth.account.sign_transaction(
            transaction, self.account.key
        )
        tx_hash = await self.w3.eth.send_raw_transaction(
            signed_transaction.raw_transaction
        )
        return tx_hash.to_0x_hex()
