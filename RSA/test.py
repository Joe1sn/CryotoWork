from RSA import *

obj = RSA()

c = "c"*0x4f
print(c)
c = obj.ByteAlign(c)
m = obj.Encrypt(c)

print("m",hex(m))
print("c",obj.Decrypt(m))