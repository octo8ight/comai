from solders.keypair import Keypair
from solders.pubkey import Pubkey
from solana.rpc.api import Client
from solders.system_program import TransferParams, transfer
from solana.transaction import Transaction
import base58


from_token_account = Pubkey(base58.b58decode("CUBroYE9CVHfALHmcD7dvyoLwiFEmN9M4s7AqkcczZag"))
to_token_account = Pubkey(base58.b58decode("BqpF7PTetpYvGhvoUmyB4nYDBCR25VPUK91EJS5oqhd5"))

leading_zeros = [0] * 31
print(leading_zeros + [1])
sender, receiver = Keypair.from_seed(leading_zeros + [1]), Keypair.from_seed(leading_zeros + [2])
print(sender.pubkey())
print(from_token_account)
print(from_token_account.default())
txn = Transaction().add(transfer(TransferParams(from_pubkey=from_token_account, to_pubkey=to_token_account, lamports=1)))
solana_client = Client("https://api.testnet.solana.com")
solana_client.send_transaction(txn, Keypair.from_base58_string(base58.b58decode("CUBroYE9CVHfALHmcD7dvyoLwiFEmN9M4s7AqkcczZag"))) # doctest: +SKIP
# solana_client.send_transaction(txn, sender) # doctest: +SKIP
# Signature(1111111111111111111111111111111111111111111111111111111111111111)