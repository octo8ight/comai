from spl.token.constants import TOKEN_PROGRAM_ID
from spl.token.instructions import transfer_checked, TransferCheckedParams

from solana.rpc.commitment import Confirmed
from solana.rpc.api import Client
from solana.rpc.types import TxOpts
from solana.keypair import Keypair
from solana.publickey import PublicKey
from solana.transaction import Transaction
from solders.pubkey import Pubkey


from_token_account = PublicKey("Brnvzh...bGPED")
to_token_account = PublicKey("6Uij3...Ahmtp")
from_wallet_address = PublicKey("rjPKeL...wedQp")
mint_public_id = PublicKey("4qYnL....Pt4taGk")
SECRET_KEY = bytes([43,124,...,3,226,229,189]) #from the account you are sending from. AKA owner account. You will find this in id.json 

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