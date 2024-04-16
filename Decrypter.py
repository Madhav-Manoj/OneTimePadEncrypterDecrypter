import random
def otpkeygen(ml):
    return [random.randint(0, 25) for _ in range(ml)]
def encrypter(m, otp):
    em = ""
    for i in range(len(m)):
        char = m[i]
        if char.isalpha():
            offset = ord('a') if char.islower() else ord('A')
            echar = chr((ord(char) - offset + otp[i]) % 26 + offset)
            em += echar
        else:
            em += char
    return em
def decrypter(m, otp):
    dm = ""
    for i in range(len(m)):
        char = m[i]
        if char.isalpha():
            offset = ord('a') if char.islower() else ord('A')
            dchar = chr((ord(char) - offset - otp[i]) % 26 + offset)
            dm += dchar
        else:
            dm += char
    return dm
f=open("messagefile.txt","r")
m = str(f.readlines())
ml = len(m)
otp = otpkeygen(ml)
em = encrypter(m, otp)
print(f"Original message from file: {m}")
print(f"One-time Pad Key: {otp}")
print(f"If the message needs to be encrypted: {em}")
dm = decrypter(m, otp)
print(f"If the message needs to be decrypted: {dm}")
