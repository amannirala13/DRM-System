from crypter import encrypt as enc
def encrypt(data):
    cypher = enc(data)
    size = len(cypher)
    print(f"Cypher: {cypher}\n\nSize: {size}")

if __name__=="__main__":
    encrypt(bytes(input(), "latin-1"))
