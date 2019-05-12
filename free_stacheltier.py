import binascii
import struct
import array
from Crypto.Cipher import DES

def key_to_bytes(key):
    tk_sub=key.split('-',3)
    tk_bytes='{:04x}{:04x}{:04x}{:04x}'.format(int(tk_sub[0]),int(tk_sub[1]),int(tk_sub[2]),int(tk_sub[3]))
    ba = bytearray(tk_bytes.decode('hex'))
    ba[0],ba[1] = ba[1],ba[0]
    ba[2],ba[3] = ba[3],ba[2]
    ba[4],ba[5] = ba[5],ba[4]
    ba[6],ba[7] = ba[7],ba[6]
    return ba

def bytes_to_key(bytes):
    ba = bytearray(bytes)
    ba[0],ba[1] = ba[1],ba[0]
    ba[2],ba[3] = ba[3],ba[2]
    ba[4],ba[5] = ba[5],ba[4]
    ba[6],ba[7] = ba[7],ba[6]
    i1 = struct.unpack('>H', ba[0:2])
    i2 = struct.unpack('>H', ba[2:4])
    i3 = struct.unpack('>H', ba[4:6])
    i4 = struct.unpack('>H', ba[6:8])
    tk_sub='{}-{}-{}-{}'.format(i1[0],i2[0],i3[0],i4[0])
    return tk_sub

tk='#'

print("welcome to free_stacheltier.py")
print("enter your igel terminal key below.")
print("just press enter to exit")
print("")

while tk is not '':
    tk = str(raw_input('terminal key:'))
    if tk is '':
        break
    b = key_to_bytes(tk)
    key3 = b'\x34\x49\xd6\xa9\xc7\x55\x67\x28'
    key2 = b'\x56\x59\x12\x95\x89\xaa\x76\x33'
    key1 = b'\x72\x02\x53\xb6\x77\x79\xad\x96'

    iv3 = b'\xF4\x41\x71\x68\x37\x73\xB1\x02'
    iv2 = b'\xC1\x92\x88\x48\x49\x05\x11\x19'
    iv1 = b'\x3B\x52\x7F\x6E\x97\xF8\xAA\x16'

    d1 = DES.new(key1,DES.MODE_CBC,iv1)
    d2 = DES.new(key2,DES.MODE_CBC,iv2)
    d3 = DES.new(key3,DES.MODE_CBC,iv3)

    t1 = d1.encrypt(buffer(b,0,8))
    t2 = d2.decrypt(buffer(t1,0,8))
    t3 = d3.encrypt(buffer(t2,0,8))
    print("Congratulations!")
    print("your reset key:")
    print(bytes_to_key(bytearray(t3)))
    print("")
