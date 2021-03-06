# stlr: An easy and fast way to send money via text messages

### Sending money across borders has never been an easy task. It takes a lot of time and relies on a slow and expensive banking infratructure. Stellar solves this problem by offering a reliable money transfer/storage system, and this project, **stlr**, offers another layer of simplification by enabling less-fortunate people with basic cell phones and casual access to the internet to receive money cheaply via a simple SMS, regardless of their currency or location.

**IMPORTANT**: stlr currently only works on the Stellar testnet as it's an experimental project.

The API uses Twilio for sending messages and MongoDB for storing pending operations consistently.

Workflow:
---------------
Here's the workflow for sending money to someone via an SMS:

**Sender:**
- The sender enters the recipient's phone number.
- The sender sends the desired amount (in XLM) to a generated address.

**Recipient:**
- The recipient receives a unique URL via sms.
- The recipient can use the url to claim the funds by entering a Stellar address and selecting a currency once he has an Internet access.

Instructions:
---------------

After cloning the repository, do:

```bash
# Using Pipenv

sudo pipenv install --skip-lock

# Using Pip

sudo pip install -r requirements.txt
```

Then, create a `.env` file:
```bash
ACCOUNT_SID="<twilio account sid>"
AUTH_TOKEN="<twilio auth token>"
PHONE_NUMBER="<twilio phone number>"
DB_HOST="<mongodb URI>"
DB_CLIENT="<database name>"
```

Launch the server using:

```bash
python main.py
```

Launch the client by cloning [this repository](https://github.com/merwane/stlr-client) and following the instructions on the README file.

Once the client and the server are running, you can start using the service by visiting [localhost:3000](http://localhost:3000/)

Ideas:
---------------
- This can be monetized by substracting a tiny fraction as a commission for each transfer.
- A built-in exchange would facilitate withdrawals for recipients.
- User accounts to keep track of withdrawals.