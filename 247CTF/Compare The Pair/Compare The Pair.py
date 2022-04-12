#!/usr/bin/env python3
import hashlib

pass_salt = 'f789bbc328a3d1a3'
password = 0

while True:
    current = pass_salt + str(password)
    
    h = hashlib.md5(bytes(current, 'ascii')).hexdigest()
    
    if h[:2] == "0e" and h[2:].isdigit():
        print(password)
        break
        
    password += 1