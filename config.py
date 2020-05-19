from dotenv import load_dotenv
from os.path import join, dirname
import os

HORIZON_BASE_URL = "https://horizon-testnet.stellar.org"
TESTNET_NETWORK_PASSPHRASE="Test SDF Network ; September 2015"

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

# DB
DB_CLIENT = os.getenv('DB_CLIENT')
DB_HOST = os.getenv('DB_HOST')

# Twilio API
PHONE_NUMBER = os.getenv('PHONE_NUMBER') 
ACCOUNT_SID = os.getenv('ACCOUNT_SID')
AUTH_TOKEN = os.getenv('AUTH_TOKEN')
