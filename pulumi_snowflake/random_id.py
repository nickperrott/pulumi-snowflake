import binascii
import os
from math import ceil


class RandomId:

    @staticmethod
    def generate(chars):
        bytes = ceil(chars / 2)
        string = binascii.b2a_hex(os.urandom(bytes)).decode("utf-8")
        return string[0:chars]
