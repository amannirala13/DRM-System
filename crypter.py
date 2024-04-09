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
import hmac
import hashlib

'''
    This logic will go inside the embedded sub-system. This is to be secured.
    The key generation and system-id and related cryptographic operations shall
    not be exposed to the user.

'''

'''
-------------- [DEVICE UUID] ----------------------
'''
# TODO: Implement this function in the sub-system and access through the device driver
'''
    Generates and return the device uuid
'''
def generate_uuid():
    uuid = bytes(machineid.hashed_id(), "latin-1")
    return (uuid, len(uuid))

'''
Very the id with the current device id
'''
def verify_uuid(uuid):
    return uuid == machineid.hashed_id()

'''
---------------- [HASHING] ---------------------
'''

# TODO: Implement this function in the sub-system and access through the device driver
'''
    Loads the signature key pairs from the key-store
'''
def load_signature_secret_key():
    try:
        file = open("secure.key", "br")
        secret_key = file.read()
    except:
        secret_key = b"Default key in case of secret.key file is missing"
    return secret_key

'''
    Generate a pub and prv key pair for digital signatures
'''
def generate_signature(data):
    signature = hmac.new(load_signature_secret_key(), data, hashlib.sha256).hexdigest()
    return signature

'''
    Verify the digital signature against the currrent executable
'''
def verify_signature(data, signature):
    actual_signature = signature = hmac.new(load_signature_secret_key(), data, hashlib.sha256).hexdigest()
    return signature == actual_signature



'''
--------------- [ENCRYPTION] ------------------
'''
# TODO: Implement this function in the sus-system and access through the device driver

'''
    Generate the RSA encryption kry pair and store it in the keystore

    This will be used in the manufacturing process of the sub-system
'''
def generate_rsa_keys():
    file = open("key", "bw")
    (pub, prv) = rsa.newkeys(1024)
    pickle.dump({"pub": pub, "prv":prv}, file)
    file.close()
    return (pub, prv)

'''
    Load the RSA keys from the key-store. 
    WARNING: This should not be done... This should be generated at the time of manufacturing
    and burned in the EEPROM of the sub-system
'''
def load_rsa_keys():
    file = open("key", "br")
    data = pickle.load(file)
    file.close()
    return data

'''
    Encrypts the bytes data using the pub key and returns the encrypted bytes
'''
def encrypt(data):
    if not os.path.isfile("key"):
        pub, prv = generate_rsa_keys()
    else:
        keys = load_rsa_keys()
        pub = keys.get("pub")
        prv = keys.get("prv")
    print(f"prv: {prv}")
    return rsa.encrypt(data, pub)

'''
    Decrypts the encrypted bytes using the prv ket and returns the actual bytes
'''
def decrypt(cypher):
    if not os.path.isfile("key"):
        print("generating keys")
        pub, prv = generate_rsa_keys()
    else:
        keys = load_rsa_keys()
        pub = keys.get("pub")
        prv = keys.get("prv")
    print(f"prv:{prv}")
    return rsa.decrypt(cypher, prv)

'''
-------------------------------------------------
'''
if __name__=="__main__":
    print(generate_rsa_keys())
    print("My-Keys: ",load_rsa_keys())
    data = encrypt(bytes("I am loved", "latin-1"))
    print(data.decode("latin-1"))
    print(decrypt(data).decode("latin-1"))

