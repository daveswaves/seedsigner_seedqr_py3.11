'''
https://github.com/SeedSigner/seedsigner/blob/dev/src/seedsigner/models/settings_definition.py
'''

class SettingsConstants:
    # QR code constants
    DENSITY__LOW = "L"
    DENSITY__MEDIUM = "M"
    DENSITY__HIGH = "H"

    WORDLIST_LANGUAGE__ENGLISH = "en"
    
    # Seed-related constants
    MAINNET = "M"
    TESTNET = "T"
    REGTEST = "R"

    @classmethod
    def map_network_to_embit(cls, network) -> str:
        if network == SettingsConstants.MAINNET:
            return "main"
        elif network == SettingsConstants.TESTNET:
            return "test"
        if network == SettingsConstants.REGTEST:
            return "regtest"
    
    SINGLE_SIG = "ss"
    MULTISIG = "ms"

    LEGACY_P2PKH = "leg"  # Intentionally excluded from ALL_SCRIPT_TYPES
    NATIVE_SEGWIT = "nat"
    NESTED_SEGWIT = "nes"
    TAPROOT = "tr"
    CUSTOM_DERIVATION = "cus"
