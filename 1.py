from solana.publickey import PublicKey
from solana.keypair import Keypair
from solana.system_program import TransferParams, transfer
from solana.transaction import Transaction
from solana.rpc.api import Client
from solders.pubkey import Pubkey


import base58

http_client = Client("https://api.devnet.solana.com")
sender_pri = ''
receiver_pub = ''

def load_wallet():
    byte_array = base58.b58decode(sender_pri)
    account = Keypair.from_secret_key(byte_array)
    return account

def send_sol(receiver, amount):
    try:
        sender = load_wallet()

        txn = Transaction().add(transfer(TransferParams(
            from_pubkey=sender.public_key, to_pubkey=PublicKey(receiver), lamports=amount)))
        resp = http_client.send_transaction(txn, sender)

        transaction_id = resp['result']
        if transaction_id != None:
            return transaction_id
        else:
            return None

    except Exception as e:
        print('error:', e)
        return None

if __name__ == '__main__':
    send_sol(receiver_pub, 1)