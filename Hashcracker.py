import hashlib, os
print"""
_  _ ____ ____ _  _    ____ ____ ____ ____ _  _ ____ ____    ___  _   _ 
|__| |__| [__  |__|    |    |__/ |__| |    |_/  |___ |__/    |__]  \_/  
|  | |  | ___] |  |    |___ |  \ |  | |___ | \_ |___ |  \    |__]   |   
                                                                        
_ _  _ ____ _  _ ____ ____ ____ _  _ ___ 
| |\ | [__  |  | |__/ | __ |___ |\ |  |  
| | \| ___] |__| |  \ |__] |___ | \|  |
"""
print "\n(1) MD5 Cracker\n"
print "(2) SHA1 Cracker\n"
print "(3) SHA224 Cracker\n"
print "(4) SHA256 Cracker\n"
yolla = raw_input("Girdi : ")
if yolla == "1":
    sam = raw_input("Kirilacak Hash : ")
    girdi = sam
    liste = open("wordlist.txt", "r").readlines() 
    for hashs in liste:
        hashs = hashs.strip()
        insz = hashlib.md5(hashs).hexdigest()
        if insz == girdi:
                print "MD5 Kirildi: " + hashs
                break
if yolla == "2":
    bam = raw_input("Kirilacak Hash : ")
    girdi = bam
    liste = open("wordlist.txt", "r").readlines() 
    for hashs in liste:
        hashs = hashs.strip()
        insz = hashlib.sha1(hashs).hexdigest()
        if insz == girdi:
                print "SHA1 Kirildi: " + hashs
                break    
if yolla == "3":
    bam = raw_input("Kirilacak Hash : ")
    girdi = bam
    liste = open("wordlist.txt", "r").readlines() 
    for hashs in liste:
        hashs = hashs.strip()
        insz = hashlib.sha224(hashs).hexdigest()
        if insz == girdi:
                print "SHA224 Kirildi: " + hashs
                break
if yolla == "4":
    bam = raw_input("Hash : ")
    girdi = bam
    liste = open("wordlist.txt", "r").readlines() 
    for hashs in liste:
        hashs = hashs.strip()
        insz = hashlib.sha256(hashs).hexdigest()
        if insz == girdi:
                print "SHA256 Kirildi: " + hashs
                break
