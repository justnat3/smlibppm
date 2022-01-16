from __future__ import print_function
from smlibppm.core.error import eprint
import struct
import zlib
import sys

fd = sys.argv[1]
fd = open(fd, "rb")
fd.seek(8)  # skip header

HEADER_BUFF_SIZE = 8
CHECKSUM_BUFF_SIZE = 4


def read_chunk(fd):
    # First 4 bytes is the size of the chunk
    # next 4 bytes is the chunk type
    # http://www.libpng.org/pub/png/spec/1.2/PNG-Structure.html
    length, _type = struct.unpack(">I4s", fd.read(HEADER_BUFF_SIZE))
    chunk_data = fd.read(length)

    checksum = zlib.crc32(
        chunk_data,
        zlib.crc32(struct.pack(">4s", _type)))

    (chunk_crc,) = struct.unpack(">I", fd.read(CHECKSUM_BUFF_SIZE))

    if chunk_crc != checksum:
        eprint(f"Checksum Failed {chunk_crc} != {checksum}")
        exit(1)

    return (_type, chunk_data)


def test() -> int:
    print("\nCT", "      DATA\n")
    while True:
        typ, data = read_chunk(fd)

        if typ == b"IEND":
            print("IEND")
            break

            break

        if len(data) < 100:
            print(typ.decode(), "   ", data)
        else:
            print(typ.decode())

    fd.close()

    return 0
