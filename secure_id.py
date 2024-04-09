import sys
from crypter import generate_uuid, generate_signature, verify_signature, encrypt, decrypt

def partition_file(path):
    file = open(path, 'br')
    data = file.read()
    exe = data[:-128]
    id = data[-128:]
    return exe, id

def embed_secure_id(path=None, new_file_path=None):    
    id, size = generate_uuid()
    if path == None:
        path = sys.argv[1]

    if not len(path) >= 0:
        return False

    if new_file_path == None:
        new_file_path = f"{path}.secure"

    original = open(path, "br")
    secured = open(new_file_path, "ba")
    
    data = original.read()

    original_sig = generate_signature(data+id)
    secure_id = encrypt(bytes(original_sig, "latin-1"))
    secure_id_size = len(secure_id)
    print(f"Size of secure_id : {secure_id_size}")
    secured.write(data)
    secured.write(secure_id)
    
    print(f"File secured with secure_id: {secure_id} at location: {new_file_path}")

    print("---- Debug -----")
    
    decrypted_secure_id = decrypt(secure_id)

    print(f"Decrypted msg: {decrypted_secure_id}")
    print(f"Verify Signature: {verify_signature(data+id, decrypted_secure_id)}")

    return True

if __name__ == "__main__":
    embed_secure_id(sys.argv[1], sys.argv[2])
