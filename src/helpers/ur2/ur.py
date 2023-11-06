'''
https://github.com/SeedSigner/seedsigner/blob/dev/src/seedsigner/helpers/ur2/ur.py
'''

from .utils import is_ur_type

class InvalidType(Exception):
    pass

class UR:

    def __init__(self, type, cbor):
        if not is_ur_type(type):
            raise InvalidType()

        self.type = type
        self.cbor = cbor

    def __eq__(self, obj):
        if obj == None:
            return False
        return self.type == obj.type and self.cbor == obj.cbor
    