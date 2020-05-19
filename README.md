# stlr: An easy and fast way to send money via text messages

### Sending money across borders has never been an easy task. It takes a lot of time and relies on a slow and expensive banking infratructure. Stellar solves this problem by offering a reliable money transfer/storage system, and this project, **stlr**, offers another layer of simplification by enabling less-fortunate people with basic cell phones and casual access to the internet to receive money cheaply via a simple SMS, regardless of their currency or location.

**IMPORTANT**: stlr currently only works on the Stellar testnet as it's an experimental project.

The API uses Twilio for sending messages and MongoDB for storing pending operations consistently.

Usage:
---------------
Here's a video I made explaining how the service works.

[![IMAGE ALT TEXT HERE](https://img.youtube.com/vi/08FiCiACoGM/0.jpg)](https://www.youtube.com/watch?v=08FiCiACoGM)

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
