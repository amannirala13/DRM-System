import sys
import re
import os
from header import extract_id
from crypter import verify_uuid

def exec(path):
    id = extract_id(path).decode("latin-1")
    if verify_uuid(id):
        os.system(f"./{path}")
    else:
        print("not verified")


if __name__ == "__main__":
    path = sys.argv[1]
    
    pat = ".*\\.?(eilf|exe|a|out|bin)?$"
    
    if not re.match(pat, path):
        print("invalid executable file")
        sys.exit(-1)
    exec(path)
