# functions used for generations

from stellar_sdk import Keypair, Server, TransactionBuilder, Network, Asset, Account
from config import HORIZON_BASE_URL, TESTNET_NETWORK_PASSPHRASE
from resources.utils import assets 
import requests

server = Server(horizon_url=HORIZON_BASE_URL)

# generates a keypair
def gen_kp():
    keypair = Keypair.random()
    pubk = keypair.public_key
    prk = keypair.secret
    return {'public_key': pubk, 'private_key': prk}

# creates an account (testnet)
def create_acc(pubk):
    url = "https://friendbot.stellar.org"
    response = requests.get(url, params={'addr': pubk})
    response = response.json()
    return {"account": response['_links']['transaction']['href'], "status": "created"}

# creates a transaction
def create_tx(private_key, receiver, amount, asset_code, asset_code_dest):
    source_keypair = Keypair.from_secret(private_key)
    source_public_key = source_keypair.public_key
    source_account = server.load_account(source_public_key)
    
    # create account for recipient (testnet)
    try:
        create_acc(receiver)
    except KeyError:
        pass

    base_fee = server.fetch_base_fee()
    path = [Asset("XLM", None)]
    
    transaction = (
            TransactionBuilder(
                source_account=source_account,
                network_passphrase=Network.TESTNET_NETWORK_PASSPHRASE,
                base_fee=base_fee
                ).add_text_memo("Hello Testnet")
                .append_path_payment_op(receiver, dest_amount=str(amount), 
                    send_code=asset_code, send_issuer=assets[asset_code],
                    send_max="1000", dest_code=asset_code_dest,
                    dest_issuer=assets[asset_code_dest],
                    path=path
                    )
                .set_timeout(30)
                .build()
            )

    transaction.sign(source_keypair)
    response = server.submit_transaction(transaction)
    
    return response
