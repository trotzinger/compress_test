from ctypes import CDLL, POINTER, c_int, byref, c_ubyte
so_file = "/home/trotzinger/garmin_question/simple_compress.so"

simple_compress = CDLL(so_file)
simple_compress.argtypes = [POINTER(c_ubyte), c_int]
data_size = c_int(4)
data_ptr = (c_ubyte * 4)(c_ubyte(0x22),c_ubyte(0x22),c_ubyte(0x22),c_ubyte(0x55))

print(simple_compress.simple_compress(byref(data_ptr), data_ptr._length_))
for d in data_ptr:
    print(hex(d))
