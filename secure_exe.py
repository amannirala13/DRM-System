'''
@author - Aman Nirala (@amannirala13)

@date - 9/4/2024

@description - This file contains functions extended from the UNIX exec syscall
'''

# TODO: Shift the logic to the kernel space

import sys
import re
import os
from secure_id import partition_file
from crypter import verify_uuid, verify_signature, decrypt, generate_uuid

'''
    Executes the exec file with secureity check
'''
def exec(path):
    device_id, _ = generate_uuid() 
    
    exe, id = partition_file(path)
    print(f"id: {id} \n\n\nsize: {len(id)}")
    
    decrypted_id = decrypt(id)

    try:
        if verify_signature(exe+device_id, decrypted_id):
            os.system(f"./{path}")
    except:
        print("not verified")
        sys.exit(-1)
    else:
        print("not verified")
        sys.exit(-1)


if __name__ == "__main__":
    path = sys.argv[1]
    
    pat = ".*\\.?(eilf|exe|a|out|bin)?$"
    
    if not re.match(pat, path):
        print("invalid executable file")
        sys.exit(-1)
    exec(path)
