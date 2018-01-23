#! /usr/bin/python3
# -*- coding : utf-8 -*-
def Crypter(m,k):#Fonction to Encrypt
    m = ord(str(m.upper())) - 65 
    if(m == -33):#if m is a space return the ASCII code for space i.e 32
        return 32
    else:#else if m was A with 65 for ASCII for exemple k = 3
        #we have : (65 + 3) %26 = 68
        #the Cesar ABCDEFGH... for k=3 decal. i.e A = A=3 ==> D
        #          DEFGHIJK...
        return (m+k)%26 #the Method Encrypt return 68.

def DeCrypter(m,k):#Fonction to Decrypt
    if(ord(str(m)) == 32): #if it's a space " " DeCrypt() return a space " "
        return 32
    else: #else if m is D for 68 in ASCII we have
        m = ord(str(m)) + 65 # 68 + 65
        return (m-k)%26 #(133-3)%26 = 0 ; 0 == A it's the first letter in the 26th ABCD...

def CesarCrypte(mot,k):
    motCrypter = []
    for l in mot:
        if(ord(l.upper()) >= 65 or ord(l.upper()) <=90):#if the letter is not a CESAR letter
            motCrypter.append(chr(ord(l.upper())+k))#add only a simple decalage to 3
        else:#else send it in Encrypt Fonction
            cr = Crypter(l, k) 
            if cr == 32:
                motCrypter.append(chr(cr))
            else:
                motCrypter.append(chr(cr+65))
        strCrp = "".join(motCrypter)
    return strCrp

def CesarDeCrypte(mot,k):#same inverse
    motCrypter = []
    for l in mot:
        if(ord(l.upper()) >= 65 or ord(l.upper()) <=90):#same inverse
            motCrypter.append(chr(ord(l.upper())-k))
        else:
            cr = DeCrypter(l, k)#same inverse
            if(cr == 32):
                motCrypter.append(chr(cr))
            else:
                motCrypter.append(chr(cr+65))
        strCrp = "".join(motCrypter)#add it in the chain
    return strCrp

# print('A Crypter : ',CesarCrypte('ALEA JACTA EST',3))
# print('A Decrypter : ',CesarDeCrypte("DOHD MDFWD HVW", 3))

msj = input('Entrer un msj a crypter : ')
print(CesarCrypte(msj, 3))
cph = input('Entrer un msj a Decrypter : ')
print(CesarDeCrypte(cph, 3))



