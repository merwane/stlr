from mongoengine import *
import datetime

class RecipientAccount(Document):
    uid = StringField()
    public_key = StringField()
    private_key = StringField()
    phone = StringField()
    currency = StringField(default='XLM')
    sent_at = DateTimeField(default=datetime.datetime.utcnow)
    claimed_at = DateTimeField()
