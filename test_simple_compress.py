from ctypes import CDLL, POINTER, c_int, byref, c_ubyte 


class TestSimpleCompress:
    def setup(self):
        so_file = "/home/trotzinger/compress_test/simple_compress.so"
        self.simple_compress = CDLL(so_file)
        self.simple_compress.argtypes = [POINTER(c_ubyte), c_int]

    def test_gapCompressSize(self):
        # Positive path A test.
        # tests size when a compression gap array is passed to simple_compress
        data_ptr = (c_ubyte * 10)(c_ubyte(0x22),c_ubyte(0x22),c_ubyte(0x22),c_ubyte(0x22),
                    c_ubyte(0x66),
                    c_ubyte(0x22),c_ubyte(0x22),c_ubyte(0x22),c_ubyte(0x22),c_ubyte(0x22))
        assert(self.simple_compress.simple_compress(byref(data_ptr), data_ptr._length_) == 5)
        
    def test_gapCompressContents(self):
        # Positive path A test. 
        # tests contents when a compression gap array is passed to simple_compress
        data_ptr = (c_ubyte * 10)(c_ubyte(0x22),c_ubyte(0x22),c_ubyte(0x22),c_ubyte(0x22),
                    c_ubyte(0x66),
                    c_ubyte(0x22),c_ubyte(0x22),c_ubyte(0x22),c_ubyte(0x22),c_ubyte(0x22))
        length = self.simple_compress.simple_compress(byref(data_ptr), data_ptr._length_) 
        expected_out = ["0x84","0x22","0x66","0x85","0x22"]
        actual_out = [hex(d) for d in data_ptr[:length]]
        assert(expected_out == actual_out) 

    def test_noCompressSize(self):
        # Positive path B test.
        # tests size when a no compression array is passed to simple_compress
        data_ptr = (c_ubyte * 4)(c_ubyte(0x22),c_ubyte(0x33),c_ubyte(0x44),c_ubyte(0x55))
        assert(self.simple_compress.simple_compress(byref(data_ptr), data_ptr._length_) == 4)
        
    def test_noCompressContents(self):
        # Positive path B test.
        # tests contents when a no compression array is passed to simple_compress
        data_ptr = (c_ubyte * 4)(c_ubyte(0x22),c_ubyte(0x33),c_ubyte(0x44),c_ubyte(0x55))
        length = self.simple_compress.simple_compress(byref(data_ptr), data_ptr._length_) 
        expected_out = ["0x22","0x33","0x44","0x55"]
        actual_out = [hex(d) for d in data_ptr[:length]]
        assert(expected_out == actual_out)

    def test_emptyCompressSize(self):
        # Extra test 1. 
        # tests size when length 0 array is passed to simple_compress
        data_ptr = (c_ubyte * 0)()
        assert(self.simple_compress.simple_compress(byref(data_ptr), data_ptr._length_) == 0)
        
    def test_emptyCompressContents(self):
        # Extra test 1.
        # tests contents when length 0 array is passed to simple_compress
        data_ptr = (c_ubyte * 0)()
        length = self.simple_compress.simple_compress(byref(data_ptr), data_ptr._length_) 
        expected_out = []
        actual_out = [hex(d) for d in data_ptr[:length]]
        assert(expected_out == actual_out)
    
    def test_at127CompressSize(self):
        # Extra test 2. size test 
        # tests size when 127 length array is passed to simple_compress
        data_ptr = (c_ubyte * 127)(*[c_ubyte(0x36) for i in range(127)])
        assert(self.simple_compress.simple_compress(byref(data_ptr), data_ptr._length_) == 2)
        
    def test_at127CompressContents(self):
        # Extra test 2. contents test.
        # tests contents when 127 length array is passed to simple_compress
        data_ptr = (c_ubyte * 127)(*[c_ubyte(0x36) for i in range(127)])
        length = self.simple_compress.simple_compress(byref(data_ptr), data_ptr._length_) 
        expected_out = ["0xff","0x36"]
        actual_out = [hex(d) for d in data_ptr[:length]]
        assert(expected_out == actual_out) 

