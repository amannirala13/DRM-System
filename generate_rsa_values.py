from random import seed
import random
import sys
from random import randint
import time
def is_prime(x): 
    count = 0
    for i in range(int(x/2)): 
        if x % (i+1) == 0:
            count = count+1 
    return count == 1

def gcd(a, b): 
    while b != 0:
        a, b = b, a % b 
    return a
def multiplicative_inverse(e, phi): 
    for x in range(1, phi):
        if (e * x) % phi == 1:
            return x
    return None
def generate_keypair():
    random.seed(time.time())
    p = random.randint(0,1000)
    q = random.randint(0,1000)
    while True:
        if is_prime(p) and is_prime(q) and p != q:
            break;
        p = random.randint(0,1000)
        q = random.randint(0,1000)
    n=p*q
    phi = (p-1) * (q-1)
    e = random.randrange(1, phi) 
    g = gcd(e, phi)
    while g != 1:
        e = random.randrange(1, phi)
        g = gcd(e, phi)
    d = multiplicative_inverse(e, phi)
    return ((e, n), (d, n))

def encrypt(pk, plaintext):
    key, n = pk
    cipher = [(ord(char) ** key) % n for char in plaintext]
    return cipher

def decrypt(pk, ciphertext):
    key, n = pk
    plain = [chr((char ** key) % n) for char in ciphertext]
    return ''.join(plain)

if __name__ == "__main__":
    public, private = generate_keypair()
    print(f"Public: {public}\nPrivate: {private}")
    cp = encrypt(public, "Hello world")
    print(cp)
    print(decrypt(private, cp))
