from binascii import hexlify
import os

hexstream = ''

with open('test2.mp3', 'rb') as f:
    data = f.read()
    hexstream = hexlify(data)

# print(hexstream)

with open('test.txt', 'w') as f:
    f.write(str(hexstream))

def validateBytes(input_bytes):
    byte_array = bytearray(input_bytes)
    for i in range(len(byte_array)):
        if byte_array[i] == bytes.fromhex('ff')[0]:
            byte_array[i] = bytes.fromhex('ee')[0]
    return bytes(byte_array)

def genRandomValidBytes(bytesNumber):
    return validateBytes(os.urandom(bytesNumber))

output_array = []
for i in range(0, 500):
    output_array.append(bytes.fromhex('fffbe444'))
    output_array.append(genRandomValidBytes(int(1910/2)))
    output_array.append(bytes.fromhex('11'))

output = b''.join(output_array)

with open('test2.mp3', 'wb') as f:
    f.write(output)

