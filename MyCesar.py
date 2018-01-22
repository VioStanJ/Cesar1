#! /usr/bin/python3
# -*- coding : utf-8 -*-
def Crypter(m,k):
    m = ord(str(m.upper())) - 65
    if(m == -33):
        return 32
    else:
        return (m+k)%26

def DeCrypter(m,k):
    if(ord(str(m)) == 32):
        return 32
    else:
        m = ord(str(m)) + 65
        return (m-k)%26

def CesarCrypte(mot,k):
    mot.upper()
    motCrypter = []
    for l in mot:
        cr = Crypter(l, k)
        if(cr == 32):
            motCrypter.append(chr(cr))
        else:
            motCrypter.append(chr(cr+65))
        strCrp = "".join(motCrypter)
    return strCrp

def CesarDeCrypte(mot,k):
    motCrypter = []
    for l in mot:
        cr = DeCrypter(l, k)
        if(cr == 32):
            motCrypter.append(chr(cr))
        else:
            motCrypter.append(chr(cr+65))
        strCrp = "".join(motCrypter)
    return strCrp

# print('A Crypter : ',CesarCrypte('ALEA JACTA EST',3))
# print('A Decrypter : ',CesarDeCrypte("DOHD MDFWD HVW", 3))

print(CesarCrypte("Je m'appelle Guerrier ", 3))
print(CesarDeCrypte("MH PDDSSHOOH JXHUULHU ", 3))



