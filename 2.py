from spl.token.constants import TOKEN_PROGRAM_ID
from spl.token.instructions import transfer_checked, TransferCheckedParams
# from spl.token import Pubkey
from pubkey import PyCompileError

from solana.rpc.commitment import Confirmed
from solana.rpc.api import Client
from solana.rpc.types import TxOpts
from solathon import Keypair, PublicKey
# from solana.Pubkey import Pubkey
# from solana.keypair import Keypair
# from solana.Pubkey import Pubkey
from solana.transaction import Transaction


from_token_account = pubkey("BqpF7PTetpYvGhvoUmyB4nYDBCR25VPUK91EJS5oqhd5")
to_token_account = pubkey("BqpF7PTetpYvGhvoUmyB4nYDBCR25VPUK91EJS5oqhd5")
from_wallet_address = pubkey("BqpF7PTetpYvGhvoUmyB4nYDBCR25VPUK91EJS5oqhd5")
mint_public_id = pubkey("BqpF7PTetpYvGhvoUmyB4nYDBCR25VPUK91EJS5oqhd5")
SECRET_KEY = bytes([182,252,200,158,248,52,69,246,145,119,120,235,143,228,54,194,20,253,59,46,122,162,194,56,15,217,157,227,32,196,132,247,217,49,219,19,3,44,155,153,194,215,29,1,88,41,92,181,68,44,63,100,202,233,125,68,79,197,84,129,64,195,129,121]) #from the account you are sending from. AKA owner account. You will find this in id.json 

transaction = Transaction()
transaction.add(
    transfer_checked(
        TransferCheckedParams(
            TOKEN_PROGRAM_ID, #DON'T WORRY ABOUT THIS! DON'T TOUCH IT!
            from_token_account, #Its not your wallet address! Its the token account address!
            mint_public_id, # token address 
            to_token_account, # to the receiving token account.
            from_wallet_address, # wallet address connected to the from_token_account. needs to have SOL
            1, #amount of tokens to send.
            9, #default decimal places. Don't touch in it most cases
            [] #default. Don't touch it in most cases

        )
    )
)
client = Client(endpoint="https://api.devnet.solana.com", commitment=Confirmed) #devnet you can change it to the main net if you want
owner = Keypair.from_secret_key(SECRET_KEY) # <-- need the keypair for the token owner here! [20,103,349, ... 230,239,239]
client.send_transaction(
    transaction, owner, opts=TxOpts(skip_confirmation=False, preflight_commitment=Confirmed)) #don't touch it in most cases.