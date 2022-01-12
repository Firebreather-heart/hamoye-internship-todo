import hashlib,random,string,json,binascii,logging,datetime,collections
import numpy as np 
import pandas as pd 
import pylab as pl
import Crypto 
import Crypto.Random 
from Crypto.Hash import SHA
from Crypto.PublicKey import RSA 
from Crypto.Signature import PKCS1_v1_5

global last_block_hash
last_block_hash =''
global last_transaction_index 
last_transaction_index = 0

class Block: 
    def __init__(self): 
        self.verified_transactions = [] 
        self.previous_block_hash = "" 
        self.Nonce = ""
    
    
    
fbcoins = []    
def dump_blockchain (self): 
    print ("Number of blocks in the chain: " + str(len (self))) 
    for x in range (len(fbcoins)): 
        block_temp = fbcoins[x]         
        print ("block # " + str(x)) 
        for transaction in block_temp.verified_transactions: 
            display_transaction (transaction) 
            print ('--------------') 
        print ('=====================================')     
    
    

class Client:
    def __init__(self):
        random  = Crypto.Random.new().read
        self._private_key = RSA.generate(1024,random)
        self._public_key = self._private_key.publickey()
        self._signer = PKCS1_v1_5.new(self._private_key)

    @property 
    def identity(self):
        return binascii.hexlify(self._public_key.exportKey(format='DER')).decode('ascii')

class Transaction:
    def __init__(self,sender,recipient,value):
        self.sender = sender 
        self.recipient = recipient
        self.value = value
        self.time = datetime.datetime.now()
    
    def to_dict(self):
        if self.sender == 'Genesis':
            identity = 'Genesis'
        else:
            identity = self.sender.identity

        return collections.OrderedDict({
            'sender': identity,
            'recipient':self.recipient,
            'value': self.value,
            'time': self.time
        })

    def sign_transaction(self):
        private_key = self.sender._private_key
        signer  = PKCS1_v1_5.new(private_key)
        h = SHA.new(str(self.to_dict()).encode('utf-8'))
        return binascii.hexlify(signer.sign(h)).decode('ascii')
def display_transaction(transaction): 
    #for transaction in transactions: 
    dict = transaction.to_dict() 
    print ("sender: " + dict['sender']) 
    print ('-----') 
    print ("recipient: " + dict['recipient']) 
    print ('-----') 
    print ("value: " + str(dict['value'])) 
    print ('-----') 
    print ("time: " + str(dict['time'])) 
    print ('-----')
transactions = []
dinesh = Client()
lami = Client()
newton = Client()
favour = Client()

t0 = Transaction('Genesis',dinesh.identity,500)
block0 = Block()
block0.previous_block_hash = None
block0.Nonce = None

block0.verified_transactions.append(t0)

digest = hash(block0)
last_block_hash = digest

def sha256(message):
    return hashlib.sha256(message.encode('ascii')).hexdigest()

def mine(message, difficulty=1): 
    assert difficulty >= 1 
    prefix = '1' * difficulty 
    for i in range(1000): 
        digest = sha256(str(hash(message)) + str(i)) 
        if digest.startswith(prefix): 
            print ("after " + str(i) + " iterations found nonce: "  + digest) 
            return digest 









t = Transaction(dinesh,lami.identity,50)
t.sign_transaction()
t1 = Transaction(dinesh,newton.identity,100)
t1.sign_transaction()
t2 = Transaction(favour,lami.identity,10)
t2.sign_transaction()
t3 =Transaction(newton,dinesh.identity,23)
t3.sign_transaction()
t4 = Transaction(lami,favour.identity,13)
t4.sign_transaction()
btc = [t,t1,t2,t3,t4]
for t in btc:
    transactions.append(t)

for t in transactions:
    block0.verified_transactions.append(t)
fbcoins.append(block0)
dump_blockchain(fbcoins)


