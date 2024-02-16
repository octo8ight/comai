import base58
from solana.rpc.api import Client
from spl.token.constants import TOKEN_PROGRAM_ID
from spl.token.instructions import mint_to, MintToParams, transfer, TransferParams
from solders.system_program import transfer, TransferParams
from solders.pubkey import Pubkey
from solders.keypair import Keypair
from solana.transaction import Transaction
from solathon import PublicKey

dest = Pubkey(base58.b58decode("CUBroYE9CVHfALHmcD7dvyoLwiFEmN9M4s7AqkcczZag"))
amount = 1
mint_authority=Keypair()
program_id=Pubkey(base58.b58decode("BqpF7PTetpYvGhvoUmyB4nYDBCR25VPUK91EJS5oqhd5"))
mint = Pubkey().create_with_seed(mint_authority.pubkey(), "mint", TOKEN_PROGRAM_ID)

print(dest)
print(mint)
print(mint_authority)
print(program_id)
print(TOKEN_PROGRAM_ID)

instruction = Transaction().add(
    mint_to(MintToParams(
        program_id=program_id,
        mint=mint,
        dest=dest,
        amount=amount,
        mint_authority=mint_authority.pubkey()
    ))
).add_signature(mint_authority)

client = Client("https://api.testnet.solana.com")