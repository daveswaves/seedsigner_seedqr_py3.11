"""
$ python src/encode_xpub.py

https://github.com/SeedSigner/seedsigner/blob/dev/src/seedsigner/models/encode_qr.py#L358
"""

from pprint import pprint
from binascii import b2a_base64, hexlify
from embit import bip32
from embit.networks import NETWORKS
from models.seed import Seed
from models.settings_definition import SettingsConstants


def XpubQrEncoder():
    network: str = SettingsConstants.MAINNET
    wordlist_language_code: str = SettingsConstants.WORDLIST_LANGUAGE__ENGLISH
    wordlist = Seed.get_wordlist(wordlist_language_code)
    seed_phrase = ['couple','mushroom','amount','shadow','nuclear','define','like','common','call','crew','fortune','slice']


    # pprint(wordlist)
    # wordlist = 'en'

    # derivation = 'm/84/0/0'
    derivation = 'm/84h/0h/0h'

    if wordlist is None:
        raise Exception('Wordlist Required')

    # version = bip32.detect_version(derivation, default="xpub", network=NETWORKS['main'])
    version = bip32.detect_version(derivation, default="xpub", network=NETWORKS[SettingsConstants.map_network_to_embit(network)])
    seed = Seed(mnemonic=seed_phrase, wordlist_language_code=wordlist_language_code)
    root = bip32.HDKey.from_seed(seed.seed_bytes, version=NETWORKS[SettingsConstants.map_network_to_embit(network)]["xprv"])
    fingerprint = root.child(0).fingerprint
    xprv = root.derive(derivation)
    xpub = xprv.to_public()
    # Convert xpub to zpub
    xpub_base58 = xpub.to_string(version=version)

    xpubstring = "[{}{}]{}".format(
        hexlify(fingerprint).decode('utf-8'),
        derivation[1:],
        xpub_base58
    )


    pprint(xpubstring)
    '''
    '''


XpubQrEncoder()
