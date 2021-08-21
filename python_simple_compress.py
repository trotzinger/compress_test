# exploration file! just to try out a few diffrent inputs quickly
from ctypes import CDLL, POINTER, c_int, byref, c_ubyte
so_file = "/home/trotzinger/compress_test/simple_compress.so"

simple_compress = CDLL(so_file)
simple_compress.argtypes = [POINTER(c_ubyte), c_int]
# test simple pos path no compression
data_ptr1 = (c_ubyte * 4)(c_ubyte(0x22),c_ubyte(0x33),c_ubyte(0x44),c_ubyte(0x55))
# test simple pos path with compression
data_ptr2 = (c_ubyte * 4)(c_ubyte(0x22),c_ubyte(0x22),c_ubyte(0x22),c_ubyte(0x22))
# test overload max chunk size with compression (127)
data_ptr3 = (c_ubyte * 128)(*[c_ubyte(0x22) for i in range(128)])
# test empty 
data_ptr4 = (c_ubyte * 0)()
# test gap compressions
data_ptr5 = (c_ubyte * 9)(c_ubyte(0x22),c_ubyte(0x22),c_ubyte(0x22),c_ubyte(0x22),
                          c_ubyte(0x66),
                          c_ubyte(0x22),c_ubyte(0x22),c_ubyte(0x22),c_ubyte(0x22))
# test numbers too large no compression
data_ptr6 = (c_ubyte * 4)(c_ubyte(0xAA),c_ubyte(0xBB),c_ubyte(0xCC),c_ubyte(0xDD))
# test numbers too large no compression
data_ptr7 = (c_ubyte * 4)(c_ubyte(0xAA),c_ubyte(0xAA),c_ubyte(0xAA),c_ubyte(0xAA))

def results(data_ptr):
    print(simple_compress.simple_compress(byref(data_ptr), data_ptr._length_))
    for d in data_ptr:
        print(hex(d))

results(data_ptr1)
print('-'*10)
results(data_ptr2)
print('-'*10)
results(data_ptr3)
print('-'*10)
results(data_ptr4)
print('-'*10)
results(data_ptr5)
print('-'*10)
results(data_ptr6)
print('-'*10)
results(data_ptr7)
