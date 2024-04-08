'''

@author - Aman Nirala (@amannirala13)
@date - 8/4/2025

---

@description - This file contains critial cryptographic implementation

'''

import machineid
import rsa
import pickle
import os

'''
    This logic will go inside the embedded sub-system. This is to be secured.
    The key generation and system-id and related cryptographic operations shall
    not be exposed to the user.

'''

def generate_uuid():
    uuid = bytes(machineid.hashed_id(), "latin-1")
    return (uuid, len(uuid))

def verify_uuid(uuid):
    return uuid == machineid.hashed_id()


def generate_rsa_keys():
    file = open("key", "bw")
    (pub, prv) = rsa.newkeys(1024)
    pickle.dump({"pub": pub, "prv":prv}, file)
    file.close()
    return (pub, prv)

def load_rsa_keys():
    file = open("key", "br")
    data = pickle.load(file)
    file.close()
    return data

def encrypt(data):
    if not os.path.isfile("key"):
        pub, prv = generate_rsa_keys()
    else:
        keys = load_rsa_keys()
        pub = keys.get("pub")
        prv = keys.get("prv")

    return rsa.encrypt(data, pub)

def decrypt(cypher):
    if not os.path.isfile("key"):
        pub, prv = generate_rsa_keys()
    else:
        keys = load_rsa_keys()
        pub = keys.get("pub")
        prv = keys.get("prv")

    return rsa.decrypt(cypher, prv)

if __name__=="__main__":
    print(generate_rsa_keys())
    print("My-Keys: ",load_rsa_keys())
    data = encrypt(bytes("I am loved", "latin-1"))
    print(data.decode("latin-1"))
    print(decrypt(data).decode("latin-1"))

