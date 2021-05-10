#!/usr/bin/env python3
#ST2504 - ACG Practical - myMd5Stud_skel.py
# Template for myMd5Stud.py
import sys
import hashlib
# main program starts here
argc = len(sys.argv)
if argc != 2:
    print("Usage : {0} <file name>".format(sys.argv[0]))
    exit(-1)
try:
    with open(sys.argv[1],"r") as f:
        content = f.read()
        # instantiate your hash object here
        
        # update the hash object with the file content (in bytes!) here
        
        # Retrieve and print the hex string of the message digest. 
        
        print("A Simple Program on MD5")
        # insert your code here
        h = hashlib.new('md5')
        h.update(content.encode())
        hxs = h.hexdigest()
        print(hxs)
        print("End of Program")
    f.close()
except:
    print("Invalid file argument!")

