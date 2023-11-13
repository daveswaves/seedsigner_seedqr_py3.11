'''
This script is from Stepan Snigirev's 'Basic usage' script on GitHub:
https://github.com/diybitcoinhardware/embit/tree/master/docs#basic-usage

Stepan is a quantum physicist, bitcoin hacker from Munich, Germany.

Generates bip39 seed, converts it to the root key, derives native segwit xpub,
prints first 5 receiving addresses, parses PSBT transaction and signs it.
'''

import sys
from pprint import pprint

from embit import bip32, bip39
from embit.psbt import PSBT
from embit.descriptor import Descriptor
from binascii import hexlify


mnemonic = bip39.mnemonic_from_bytes(b"128 bits is fine")
# >>> couple mushroom amount shadow nuclear define like common call crew fortune slice
# print(mnemonic)

# Generate root privkey, password can be omitted if you don't want it
seed = bip39.mnemonic_to_seed(mnemonic)
# >>> b'H\xb3\xcb*{\xe7\xd0%\xdc\xa6\x82\x1c6\x1c\x85\xd0>\xed\xb6b.*\x06\x8b"+X1\xea\xa3\xc29x\xa0?\xd5vz\xb3|\xf0v8\x17b&\xc2\x00VJ\t\x11 3*\xa2\x9d\xbc|O\xe5d@\xd3'
# print(seed)
root = bip32.HDKey.from_seed(seed)
# >>> xprv9s21ZrQH143K2fRspJMVsEnjap8ef4YqA8LafRnzPjiT8LN1YUvdWbXQYe1d3FLo2RFUt7Pzhi2qEQbeiDwcmYkqvo1nGqcV2qDFxD2QU1q
# print(root)

# Derive and convert to pubkey
xpub = root.derive("m/84h/0h/0h").to_public()
# >>> xpub6DBRY8RRnUYBPMTnuVvmiiC2jGMVmeKy4db8ztQL82GwCEMdYGbeJ2w9VH1pGQJVyci45DgkgtFX4Ro6t8JNrfbDprZMBKf4bJVueZNk2to
print(xpub)

sys.exit()

# Generate native segwit descriptors.
# You can use {0,1} for combined receive and change descriptors
desc = Descriptor.from_string("wpkh([%s/84h/0h/0h]%s/{0,1}/*)" % (hexlify(root.my_fingerprint).decode(), xpub))
# >>> wpkh([cd197461/84h/0h/0h]xpub6DBRY8RRnUYBPMTnuVvmiiC2jGMVmeKy4db8ztQL82GwCEMdYGbeJ2w9VH1pGQJVyci45DgkgtFX4Ro6t8JNrfbDprZMBKf4bJVueZNk2to/{0,1}/*)
# print(desc)

# Print first 5 addresses
for i in range(5):
    ''' >>>
    bc1q6vh3e5up842c08yg4cshdtwyjjq2fapk87ll56
    bc1qfavvltpjqyzaksy4a29mlajlshexzj9p0qyqg2
    bc1qya2kz0z6najtae7m48l0at8mhspftcshw0ukra
    bc1q08um0w3hq4a3zukegjx7fnq5eu3u73g7gxmnul
    bc1qayqd8zsad78slrkfyhnahd5974kdh9htwdzf64
    '''
    # print(desc.derive(i).address())

# parse base64-encoded PSBT transaction
psbt = PSBT.from_string("cHNidP8BAHECAAAAAaW9Cd1X07XEcA/D0XmE5dwI2AEQr4aTTTwBqopD1mxAAAAAAAD9////AvJJXQUAAAAAFgAUUa2Cs4u5XOmDFhwNxl/szK5L9beAlpgAAAAAABYAFCwSoUTerJLG437IpfbWF8DgWx6kAAAAAAABAHECAAAAATVenbXof59P6l5N+BxpXQytbyWp29JfJDyT+OwohRWKAAAAAAD+////AgDh9QUAAAAAFgAUgmkBPePxvl4jTWsuNNnypKngm824IKMwAAAAABYAFOiPQIZGLU3UZ8JugMpHcCwxmUK2zQEAAAEBHwDh9QUAAAAAFgAUgmkBPePxvl4jTWsuNNnypKngm80iBgPHS/KrcrFXnxQ0/kvZeBkmEsQGjBLEc5JRUjzP9yVXVhhnwyp0VAAAgAAAAIAAAACAAAAAAAAAAAAAIgIC9jzRiRyPDoZ5F2xMV/QfW6qma/6i0PtyELYn8YR5PjsYZ8MqdFQAAIAAAACAAAAAgAEAAAAAAAAAAAA=")

# only print outputs that are not change
for out in psbt.outputs:
    if not desc.owns(out):
        ''' >>>
        Send 89999858 to bc1q2xkc9vuth9wwnqckrsxuvhlvejhyhadhpqlduw
        Send 10000000 to bc1q9sf2z3x74jfvdcm7ezjld4shcrs9k84y3pgyxr
        '''
        print(f"Send {out.value} to {out.script_pubkey.address()}")

# >>> fee: 142
print(f"fee: {psbt.fee()}")

psbt.sign_with(root)
# >>> cHNidP8BAHECAAAAAaW9Cd1X07XEcA/D0XmE5dwI2AEQr4aTTTwBqopD1mxAAAAAAAD9////AvJJXQUAAAAAFgAUUa2Cs4u5XOmDFhwNxl/szK5L9beAlpgAAAAAABYAFCwSoUTerJLG437IpfbWF8DgWx6kAAAAAAABAHECAAAAATVenbXof59P6l5N+BxpXQytbyWp29JfJDyT+OwohRWKAAAAAAD+////AgDh9QUAAAAAFgAUgmkBPePxvl4jTWsuNNnypKngm824IKMwAAAAABYAFOiPQIZGLU3UZ8JugMpHcCwxmUK2zQEAAAEBHwDh9QUAAAAAFgAUgmkBPePxvl4jTWsuNNnypKngm80iBgPHS/KrcrFXnxQ0/kvZeBkmEsQGjBLEc5JRUjzP9yVXVhhnwyp0VAAAgAAAAIAAAACAAAAAAAAAAAAAIgIC9jzRiRyPDoZ5F2xMV/QfW6qma/6i0PtyELYn8YR5PjsYZ8MqdFQAAIAAAACAAAAAgAEAAAAAAAAAAAA=
print(psbt)
