import uuid
import requests

# available currencies/assets
assets = {
        "USD": 'GB2O5PBQJDAFCNM2U2DIMVAEI7ISOYL4UJDTLN42JYYXAENKBWY6OBKZ',
        "EURT": 'GAP5LETOV6YIE62YAM56STDANPRDO7ZFDBGSNHJQIYGGKSMOZAHOOS2S',
        'CNY': 'GAREELUB43IRHWEASCFBLKHURCGMHE5IF6XSE7EXDLACYHGRHM43RFOX',
        'XLM': None
        }

# generate uuid
def gen_uid():
    uid = uuid.uuid4().hex
    return uid

# query xlm balance
def xlm_balance(public_key):
    r = requests.get('https://horizon-testnet.stellar.org/accounts/'+public_key)
    r = r.json()
    return float(r['balances'][0]['balance'])
