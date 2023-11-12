"""
python src/encode_xpub.py

https://github.com/SeedSigner/seedsigner/blob/dev/tests/test_encodepsbtqr.py#L95

https://github.com/SeedSigner/seedsigner/blob/dev/src/seedsigner/models/encode_qr.py#L358
"""

import sys
import time
from pprint import pprint
from binascii import hexlify
from embit import bip32
from embit.networks import NETWORKS
from helpers.qr import QR
from helpers.ur2.ur_encoder import UREncoder
from helpers.ur2.ur import UR
from models.seed import Seed
from models.encode_qr import EncodeQR
from models.settings_definition import SettingsConstants

from urtypes.crypto import Account, HDKey, Output, Keypath, PathComponent, SCRIPT_EXPRESSION_TAG_MAP


def XpubQrEncoder():
    network: str = SettingsConstants.MAINNET
    wordlist_language_code: str = SettingsConstants.WORDLIST_LANGUAGE__ENGLISH
    wordlist = Seed.get_wordlist(wordlist_language_code)
    seed_phrase = ['couple','mushroom','amount','shadow','nuclear','define','like','common','call','crew','fortune','slice']

    print(seed_phrase)

    # pprint(wordlist)
    # wordlist = 'en'

    # derivation = 'm/84/0/0'
    derivation = 'm/84h/0h/0h'
    # derivation = 'm/84h/0h/0h/0h'

    if wordlist is None:
        raise Exception('Wordlist Required')

    # version = bip32.detect_version(derivation, default="xpub", network=NETWORKS['main'])
    version = bip32.detect_version(derivation, default="xpub", network=NETWORKS[SettingsConstants.map_network_to_embit(network)])
    seed = Seed(mnemonic=seed_phrase, wordlist_language_code=wordlist_language_code)
    root = bip32.HDKey.from_seed(seed.seed_bytes, version=NETWORKS[SettingsConstants.map_network_to_embit(network)]["xprv"])
    fingerprint = root.child(0).fingerprint
    xprv = root.derive(derivation)
    xpub = xprv.to_public()
    print(xpub)
    # Convert xpub to zpub
    xpub_base58 = xpub.to_string(version=version)
    # print(xpub_base58)

    # sys.exit()

    # https://github.com/SeedSigner/seedsigner/blob/dev/src/seedsigner/models/encode_qr.py#L382
    xpubstring = "[{}{}]{}".format(
        hexlify(fingerprint).decode('utf-8'),
        derivation[1:],
        xpub_base58
    )

    qr_density = 'M'
    qr_max_fragment_size = 30

    # derivation="m/48h/1h/0h/2h"
    derivation="m/84h/0h/0h/0h"
    # print(derivation)

    # Code from class UrXpubQrEncoder(XpubQrEncoder)
    # https://github.com/SeedSigner/seedsigner/blob/dev/src/seedsigner/models/encode_qr.py#L466
    def derivation_to_keypath(path: str) -> list:
        arr = path.split("/")

        if arr[0] == "m":
            arr = arr[1:]
        if len(arr) == 0:
            return Keypath([],root.my_fingerprint, None)
        if arr[-1] == "":
            # trailing slash
            arr = arr[:-1]

        for i, e in enumerate(arr):
            if e[-1] == "h" or e[-1] == "'":
                arr[i] = PathComponent(int(e[:-1]), True)
            else:
                arr[i] = PathComponent(int(e), False)
        
        return Keypath(arr, root.my_fingerprint, len(arr))


    # Code from class UrXpubQrEncoder(XpubQrEncoder)
    origin = derivation_to_keypath(derivation)
    # print(origin)

    ur_hdkey = HDKey({ 'key': xpub.key.serialize(),
        'chain_code': xpub.chain_code,
        'origin': origin,
        'parent_fingerprint': xpub.fingerprint})
    
    # print(ur_hdkey)
    # sys.exit()

    ur_outputs = []
    if len(origin.components) > 0:
        if origin.components[0].index == 84: # Native Single Sig
            ur_outputs.append(Output([SCRIPT_EXPRESSION_TAG_MAP[404]],ur_hdkey))

    ur_account = Account(root.my_fingerprint, ur_outputs)
    qr_ur_bytes = UR("crypto-account", ur_account.to_cbor())
    ur2_encode = UREncoder(ur=qr_ur_bytes, max_fragment_len=qr_max_fragment_size)

    # sys.exit()

    qr = QR()
    loop_total = ur2_encode.fountain_encoder.seq_len()
    for _ in range(loop_total):
        print(ur2_encode.next_part().upper())
        # image = qr.qrimage(
        #     data=ur2_encode.next_part().upper(),
        #     width_height=480,
        #     border=2
        # )
        # image.show() # Display QR-code
        time.sleep(5 / 30.0)
        # time.sleep(1)


    mnemonic = "obscure bone gas open exotic abuse virus bunker shuffle nasty ship dash"
    qr_type = 'xpub__ur'

    '''
    e = EncodeQR(
        seed_phrase=mnemonic.split(),
        passphrase="pass",
        qr_type=qr_type,
        network=SettingsConstants.TESTNET,
        derivation=derivation,
        qr_density=qr_density
    )
    '''



XpubQrEncoder()
