from web3 import AsyncWeb3
from web3.types import TContractFn, HexStr, TxParams, ChecksumAddress
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

    async def populated_transaction(
        self,
        function: TContractFn,
        account: ChecksumAddress,
        value: int | None = None,
    ) -> TxParams:
        nonce = await self.w3.eth.get_transaction_count(account)

        transaction_payload = {
            "nonce": nonce,
            "from": account,
            # "chainId": self.chain_id,
        }

        if value is not None:
            transaction_payload["value"] = value

        return await function.build_transaction(transaction_payload)


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

    async def populated_transaction(
        self,
        function: TContractFn,
        account: ChecksumAddress | None = None,
        value: int | None = None,
    ) -> TxParams:
        return await super().populated_transaction(
            function, account or self.account.address, value
        )

    async def send_transaction(self, transaction: TxParams) -> HexStr:
        signed_transaction = self.w3.eth.account.sign_transaction(
            transaction, self.account.key
        )
        tx_hash = await self.w3.eth.send_raw_transaction(
            signed_transaction.raw_transaction
        )
        return tx_hash.to_0x_hex()
