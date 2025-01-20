
import struct
data = struct.pack(">HB",266,17)
for d in data:
    print(f"{d:02x}", end = " ")


