import unittest
import io
import sys
from hexdump import format_binary_file

class TestHexdump(unittest.TestCase):

    def test_single_line(self):
        data = b'\x00' * 16
        expected = "00000000  00 00 00 00 00 00 00 00   00 00 00 00 00 00 00 00    |................|\n00000010"
        self.assertEqual(format_binary_file(io.BytesIO(data)), expected)

    def test_two_different_lines(self):
        data = b'\x00' * 16 + b'\x01' * 16
        expected = ("00000000  00 00 00 00 00 00 00 00   00 00 00 00 00 00 00 00    |................|\n"
                    "00000010  01 01 01 01 01 01 01 01   01 01 01 01 01 01 01 01    |................|\n"
                    "00000020")
        self.assertEqual(format_binary_file(io.BytesIO(data)), expected)

    def test_repeated_lines(self):
        data = b'\x00' * 48
        expected = ("00000000  00 00 00 00 00 00 00 00   00 00 00 00 00 00 00 00    |................|\n"
                    "* 2 lines repeated\n"
                    "00000030")
        self.assertEqual(format_binary_file(io.BytesIO(data)), expected)

    def test_mixed_content(self):
        data = b'\x00' * 16 + b'\x01' * 32 + b'\x02' * 16
        expected = ("00000000  00 00 00 00 00 00 00 00   00 00 00 00 00 00 00 00    |................|\n"
                    "00000010  01 01 01 01 01 01 01 01   01 01 01 01 01 01 01 01    |................|\n"
                    "* 1 lines repeated\n"
                    "00000030  02 02 02 02 02 02 02 02   02 02 02 02 02 02 02 02    |................|\n"
                    "00000040")
        self.assertEqual(format_binary_file(io.BytesIO(data)), expected)

    def test_empty_file(self):
        data = b''
        expected = "00000000"
        self.assertEqual(format_binary_file(io.BytesIO(data)), expected)

if __name__ == '__main__':
    unittest.main()