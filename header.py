import sys
from crypter import generate_uuid

def extract_id(path):
    file = open(path, 'br')
    file.seek(-64,2)
    id = file.read()
    return id

def embeed_secure_id(path=None, new_file_path=None):    
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
    secured.write(data)
    secured.write(id)
    
    print(f"Wrote {id}")

    return True

if __name__ == "__main__":
    embeed_secure_id(sys.argv[1], sys.argv[2])
