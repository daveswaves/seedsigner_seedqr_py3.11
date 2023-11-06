'''
https://github.com/SeedSigner/seedsigner/blob/dev/tests/test_seedqr.py#L24

INFO:
Creates a 12 or 24 word seed phrase.
Converts seed phrase words to their 4 digit zero-padded indices,
and concatenates


: eg. 110301551596063900810786062915601161029816801682

Eg:
['1103: measure',
 '0155: beach',
 '1596: shy',
 '0639: exit',
 '0081: any',
 '0786: girl',
 '0629: exchange',
 '1560: seek',
 '1161: muffin',
 '0298: census',
 '1680: spirit',
 '1682: spoil']

# The above can be output with the following code:
word_index = []
for word in seed_phrase:
    index = bip39.WORDLIST.index(word)
    word_index.append(f"{index:04d}: {word}")

pprint(word_index)
'''

import os
from pprint import pprint
from embit import bip39
# from PIL import Image

from helpers.qr import QR
from models.decode_qr import DecodeQR, DecodeQRStatus
from models.encode_qr import EncodeQR
from models.qr_type import QRType



def run_encode_decode_test(entropy: bytes, mnemonic_length, qr_type):
    # print(entropy) # b"\x89\xe2o\x1e'\xf0\xa2\xc4\x93\xae\x18\x91$\xabHi"
    seed_phrase = bip39.mnemonic_from_bytes(entropy).split()
    # print(seed_phrase) # ['measure', 'beach', 'shy', 'exit', 'any', 'girl', 'exchange', 'seek', 'muffin', 'census', 'spirit', 'spoil']

    # hardcode seed
    seed_phrase = [
        'win',
        'between',
        'crucial',
        'lemon',
        'tonight',
        'owner',
        'height',
        'shift',
        'planet',
        'devote',
        'will',
        'retreat',
        'duck',
        'cash',
        'civil',
        'elbow',
        'melody',
        'rare',
        'glide',
        'deliver',
        'labor',
        'refuse',
        'write',
        'front'
    ]

    e = EncodeQR(seed_phrase=seed_phrase, qr_type=qr_type)
    data = e.next_part()
    # print(data) # 110301551596063900810786062915601161029816801682

    # print(type(data))

    qr = QR()
    image = qr.qrimage(
        data=data,
        # Options: 480 / 720 (comment out to default to 240)
        width_height=480,
        border=2
    )

    # pprint(image)

    image.show() # Display QR-code
    """
    decoder = DecodeQR()
    status = decoder.add_image(image)
    # Check status correct
    pprint(status == DecodeQRStatus.COMPLETE) # True

    decoded_seed_phrase = decoder.get_seed_phrase()
    print(decoded_seed_phrase) # ['measure', 'beach', 'shy', 'exit', 'any', 'girl', 'exchange', 'seek', 'muffin', 'census', 'spirit', 'spoil']
    """



# 24-word seed
# run_encode_decode_test(os.urandom(32), mnemonic_length=24, qr_type=QRType.SEED__SEEDQR)

# 12-word seed
run_encode_decode_test(os.urandom(16), mnemonic_length=12, qr_type=QRType.SEED__SEEDQR)
