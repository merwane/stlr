from flask_restful import Resource, abort
from flask import request, jsonify
from resources.gen import gen_kp, create_tx
from resources.phone import send_msg
from resources.utils import gen_uid, xlm_balance
from mongoengine import connect
from config import DB_CLIENT, DB_HOST
from models.account import RecipientAccount
import pymongo
import re

# init db
dbclient = pymongo.MongoClient(host=DB_HOST, retryWrites=False)
db = dbclient[DB_CLIENT]
connect(DB_CLIENT, host=DB_HOST, retryWrites=False)

class GenerateAccount(Resource):
    def get(self, phone):
        
        kp = gen_kp()
        uid = gen_uid()
        phone_number = str(phone)
        recipient_account = RecipientAccount(
                uid=uid,
                public_key=kp['public_key'],
                private_key=kp['private_key'],
                phone=phone_number
                )
        recipient_account.save()

        return jsonify(status='success', public_key=kp['public_key'], uid=uid, phone=phone_number)

class SendTx(Resource):
    def post(self, uid):
        txs = []
        for tx in db.recipient_account.find({"uid": uid}):
            txs.append({
                'uid': tx['uid'],
                'public_key': tx['public_key'],
                'phone': tx['phone'],
                'currency': tx['currency']
                })
        recipient = txs[0]
        balance = xlm_balance(recipient['public_key'])
        if balance <= 0:
            abort(400, message="Cannot be 0 XLM")

        msg_body = 'Someone just sent you '+str(balance)+' XLM via stlr - claim it on http://localhost:3000/claim/'+uid
        send_msg(msg_body, recipient['phone'])

        return jsonify(status='success', recipient=recipient['phone'])

class Claim(Resource):
    def get(self, uid):
        txs = []
        for tx in db.recipient_account.find({"uid": uid}):
            txs.append({
                    'uid': tx['uid'],
                    'public_key': tx['public_key'],
                    'private_key': tx['private_key'],
                    'phone': tx['phone'],
                    'currency': tx['currency']
                    })
        recipient = txs[0]
        return jsonify(balance=xlm_balance(recipient['public_key']), prkey=recipient['private_key'], currency=recipient['currency'], phone=recipient['phone'])

class SendClaim(Resource):
    def post(self, uid):
        recipient_pubk = request.json['pubk']
        prkey = request.json['prkey']
        balance = request.json['balance']
        preferred_currency = request.json['preferred_currency']
        phone = request.json['phone']
        
        balance = balance - 2

        create_tx(prkey, recipient_pubk, str(balance), 'XLM', preferred_currency, phone)
        return jsonify(status='success')
