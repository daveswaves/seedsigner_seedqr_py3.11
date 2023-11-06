'''
https://github.com/SeedSigner/seedsigner/blob/dev/src/seedsigner/models/encode_qr.py

'''

from dataclasses import dataclass
from typing import List

from helpers.qr import QR
from models.qr_type import QRType
from models.settings_definition import SettingsConstants
from models.seed import Seed


@dataclass
class EncodeQR:
    seed_phrase: List[str] = None
    qr_type: str = None
    qr_density: str = SettingsConstants.DENSITY__MEDIUM
    wordlist_language_code: str = SettingsConstants.WORDLIST_LANGUAGE__ENGLISH
    
    def __post_init__(self):
        self.qr = QR()

        if not self.qr_type:
            raise Exception('qr_type is required')
        
        if self.qr_density is None:
            self.qr_density = SettingsConstants.DENSITY__MEDIUM

        self.encoder: BaseQrEncoder = None

        # SeedQR formats
        if self.qr_type == QRType.SEED__SEEDQR:
            self.encoder = SeedQrEncoder(seed_phrase=self.seed_phrase,
                                         wordlist_language_code=self.wordlist_language_code)

    def next_part(self):
        return self.encoder.next_part()



class BaseQrEncoder:
    def seq_len(self):
        raise Exception("Not implemented in child class")

    def next_part(self) -> str:
        raise Exception("Not implemented in child class")

    @property
    def is_complete(self):
        raise Exception("Not implemented in child class")

    def _create_parts(self):
        raise Exception("Not implemented in child class")


class BaseStaticQrEncoder(BaseQrEncoder):
    def seq_len(self):
        return 1

    @property
    def is_complete(self):
        return True


class SeedQrEncoder(BaseStaticQrEncoder):
    def __init__(self, seed_phrase: List[str], wordlist_language_code: str):
        super().__init__()
        self.seed_phrase = seed_phrase
        self.wordlist = Seed.get_wordlist(wordlist_language_code)
        
        if self.wordlist == None:
            raise Exception('Wordlist Required')

    def next_part(self):
        data = ""
        # Output as Numeric data format
        for word in self.seed_phrase:
            index = self.wordlist.index(word)
            data += str("%04d" % index)
        return data
