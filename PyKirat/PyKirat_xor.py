#-*- coding: utf-8 -*-
mode=input("Choose Program mode:\n1.Encryption\n2. Decryption\n>")

if mode==1:
    plaintext=list(raw_input("Enter PlainText: "))
    key=list(raw_input("Enter key: "))
    
    binary=[]
    
    for i in plaintext:
        binary.append(list(bin(ord(i))[2:]))
    print binary
        
    full_key=[]
    
    for j in range(((len(binary)*8)/len(key))):
        full_key.extend(key)
    print full_key
    
    code=[]
    
    loc=0
    for k in binary:
        for z in k:
            if z==full_key[loc]:
                code.append('0')
            else:
                code.append('1')
            loc+=1
    #-----------------------------    
    mode=input("Choose Encryption mode:\n1.키랏-mode\n2.가루바나나-mode\n>")    
    if mode==1:
        one="키랏"
        zero="★"
    else:
        one="가루★"
        zero="바나나!"
    #-------------------------------
    
    print code
    
    for l in code:
        if l=='1':
            print one,
        else:
            print zero,

else:
    code=list(raw_input("Enter Encrypted Code: ").split())
    key=list(raw_input("Enter key: "))  
        
    #-------------------------------
    mode=input("Choose Encryption mode:\n1.키랏-mode\n2.가루바나나-mode\n>")    
    if mode==1:
        one="키랏"
        zero="★"
    else:
        one="가루★"
        zero="바나나!"    
    #-------------------------------
    binary=[]
    for i in code:
        if i==one:
            binary.append('1')
        else:
            binary.append('0')
    print binary
    
    full_key=[]
    for j in range((len(binary)/len(key))+1):
        full_key.extend(key)
    print full_key
        
    plainbin=[]
    loc=0
    for k in binary:
        if k==full_key[loc]:
            plainbin.append('0')
        else:
            plainbin.append('1')
        loc+=1
    print plainbin
    
    plaintext=[]
    
    """for l in range(len(plainbin)/7):
        ascii="0b"
        for m in range(7):
            ascii+=plainbin.pop(0)
        plaintext.append(chr(int(ascii,2)))
        
    while True:
        ascii="0b"
        for m in range(7):
            ascii+=plainbin.pop(0)
        plaintext.append(chr(int(ascii,2)))"""
    
    for l in plainbin:
        ascii="0b"
        for m in l:
            ascii+=m
        plaintext.append(chr(int(ascii,2)))
        
    
    text=""
    for n in plaintext:
        text+=n
    print text
