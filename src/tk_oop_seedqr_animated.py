'''
python src/tk_oop_seedqr_animated.py
'''

import sys
import os
from pprint import pprint
# import time
from tkinter import Tk, Frame, Canvas, Entry, Label, Button
from PIL import Image, ImageDraw, ImageFont, ImageTk
from embit.networks import NETWORKS
from embit import bip32
from helpers.qr import QR
from helpers.ur2.ur_encoder import UREncoder
from helpers.ur2.ur import UR

from models.seed import Seed
from models.settings_definition import SettingsConstants

from urtypes.crypto import Account, HDKey, Output, Keypath, PathComponent, SCRIPT_EXPRESSION_TAG_MAP

PROGRAM_NAME = 'Export Xpub'
BG_COLOR = '#000'
FILL_COLOR = '#0f0'
TEXT_INPUT_BG_COLOR = '#fff'
TEXT_INPUT_FG_COLOR = '#000'

CONFIG = {
    "wrong": {
        "fingerprint": "56462df8",
        "SEED_PHRASE": "wrong kite shock primary together system assume sponsor faith virus year guide famous fit later stool awkward mom soon bleak apart render easy pair",
        "NETWORK": SettingsConstants.MAINNET,
        "DERIVATION": "m/84h/0h/0h"
    },
    
    "EXAMPLE_FROM": "",
    "obscure": {
        "fingerprint": "obscure",
        "SEED_PHRASE": "obscure bone gas open exotic abuse virus bunker shuffle nasty ship dash",
        "NETWORK": SettingsConstants.TESTNET,
        "DERIVATION": "m/48h/1h/0h/2h",

        "XPUB": "xpub6F5dY3kJHzryJ9jg31JBFUuWniawpxLKZNwiUDXohW7fjSVht9uhRimyF1kk6hZS6bqs4c3sPYuSckb6h53jSu2x3czyqxwwyhcw7mAwPey",
        "DATA_LIST": " \
            'UR:CRYPTO-ACCOUNT/1-4/LPADAACSKPCYMOMNLGRYHDCKOEADCYSSMECPONAOLYTAADMETAADDLOXAXHDCLAOKSRLNLKPUEGYATHPMNSNIYMUECBY', \
            'UR:CRYPTO-ACCOUNT/2-4/LPAOAACSKPCYMOMNLGRYHDCKKKGHZMLUZORPVDGUOTECSTTKTOLPCWPTNTLKZTTIZTBEAAHDCXVDTPMYRSTDMOPSCXFZ', \
            'UR:CRYPTO-ACCOUNT/3-4/LPAXAACSKPCYMOMNLGRYHDCKSPZSBZSPGERLGDATUYNLPYBTGYIYYKBTWTAOSWKSVTSGCHBYDKYAVDAMTAADMONDGDFD', \
            'UR:CRYPTO-ACCOUNT/4-4/LPAAAACSKPCYMOMNLGRYHDCKDYOTADLOCSDYYKADYKAEYKAOYKAOCYSSMECPONAXAAAYCYIOREKKJKAEAEAEWZWDMYON'  \
        ",
        "sparrow_xpub": "xpub"
    },

    "couple": {
        "fingerprint": "couple",
        "SEED_PHRASE": "couple mushroom amount shadow nuclear define like common call crew fortune slice",
        "NETWORK": SettingsConstants.MAINNET,
        "DERIVATION": "m/84h/0h/0h",

        "XPUB": "xpub6DBRY8RRnUYBPMTnuVvmiiC2jGMVmeKy4db8ztQL82GwCEMdYGbeJ2w9VH1pGQJVyci45DgkgtFX4Ro6t8JNrfbDprZMBKf4bJVueZNk2to",
        "DATA_LIST": " \
            'UR:CRYPTO-ACCOUNT/1-4/LPCFADJKAACSJKCYCHFXSWPFHDCAEMNSPSCEAYFSCNISNELYDLYNHPDLVTTTFTKPLUMKDPTKWEWDLFAXDMFMLEGTSEGOTL', \
            'UR:CRYPTO-ACCOUNT/2-4/LPCFADJYAACSJKCYCHFXSWPFHDCAWYLONBASLOAEIMFGVDIEGOVSFGHHPYNNHGSTPKTKFRJEZTGMKGFWRYVLTALYHYFMLK', \
            'UR:CRYPTO-ACCOUNT/3-4/LPCFADKPAACSJKCYCHFXSWPFHDCAGEGDRKEYAXECESHHEYFDGHLDNEPDLNCXHERLRSCFBSHEVTWKBADNSPVAOYJOPDWNRP', \
            'UR:CRYPTO-ACCOUNT/4-4/LPCFADKOAACSJKCYCHFXSWPFHDCAOEADCYBDDEEETLAOLYTAADMWTAADDLOXAXHDCLAXEMEMBBRFOYHSLSGMKSWMRYMWWN'  \
        ",
        "sparrow_xpub": "xpub6F4ZPuwSznDBF86FwVPY2qxNXVGSUNSR8XiYNkGznxdqd9JSaZ6z5iWkErHf1LhxvK9CiHeTwvTajuHQkV4fv5h9uWPGsexGR2qMhUdWKVQ"
    }
}

CONF_KEY = 'couple'


# SEED_PHRASE = 'wrong kite shock primary together system assume sponsor faith virus year guide famous fit later stool awkward mom soon bleak apart render easy pair'
# SEED_PHRASE = 'couple mushroom amount shadow nuclear define like common call crew fortune slice' # correct
# SEED_PHRASE = 'couple mushroom amount shadow nuclear define like common call crew fortune ghif' # 'ghif' not in the dictionary
# SEED_PHRASE = 'couple mushroom amount shadow nuclear define like common call crew fortune zoo' # Checksum verification failed
# SEED_PHRASE = 'couple mushroom amount shadow nuclear define like common call crew fortune' # Invalid recovery phrase

class ExportXpub:
    def __init__(self, tk_root):
        self.tk_root = tk_root
        self.tk_root.title(PROGRAM_NAME)
        self.QR_WIDTH_HEIGHT = 480
        self.FREQ = int(1000 * 5 / 30.0)
        self.data_index = 0
        self.qr_images = []
        self.qr = QR()
        self.layout()

    def layout(self):
        self.frame = Frame(self.tk_root, bg=BG_COLOR)
        self.frame.pack(fill='both', expand=True)
        self.qr_panel_splash_screen()
        self.seed_phrase_panel()

    def qr_panel_splash_screen(self, error_message=None):
        script_dir = os.path.dirname(os.path.realpath(__file__))
        image_path = os.path.join(script_dir, 'qr_splash.png')
        image = Image.open(image_path)

        # Draw text on the image
        draw = ImageDraw.Draw(image)
        font_path = os.path.join(script_dir, 'rubik/Rubik-Regular.ttf') # https://www.fontsquirrel.com/
        font_heading = ImageFont.truetype(font_path, size=54)
        font = ImageFont.truetype(font_path, size=44)
        error_font = ImageFont.truetype(font_path, size=24)
        draw.text((60, 70), 'EXPORT XPUB', fill="black", font=font_heading)

        if error_message:
            err_txt = f'{error_message}'
            err_txt = err_txt.replace('ValueError(', '', 1)
            err_txt = err_txt.replace(')', '', 1)

            # Code to center text horizontally on PNG background image
            image_width, _ = image.size
            text_width, _ = draw.textsize(err_txt, error_font)
            x_pos = (image_width - text_width) // 2

            draw.text((x_pos, 210), err_txt, fill="red", font=error_font)
        else:
            draw.text((60, 140), 'Click submit to\ndisplay animated\nQR-code', fill="black", font=font)

        # Clear the existing canvas
        if hasattr(self, 'canvas'):
            self.canvas.destroy()

        self.canvas = Canvas(self.frame, width=self.QR_WIDTH_HEIGHT, height=self.QR_WIDTH_HEIGHT)
        self.canvas.pack(side='left', padx=10, pady=10)
        self.png_images = []
        png_image = ImageTk.PhotoImage(image)
        self.png_images.append(png_image)
        self.canvas_image = self.canvas.create_image(0, 0, anchor='nw', image=self.png_images[0])
        
    # Displays animated QR-code
    def update_qr_panel(self, data_list):
        self.data_list = data_list
        self.qr_images = []  # Clear existing images
        for data in data_list:
            image = self.qr.qrimage(data=data, width_height=self.QR_WIDTH_HEIGHT, border=2)
            self.qr_images.append(ImageTk.PhotoImage(image))
        self.canvas.itemconfig(self.canvas_image, image=self.qr_images[0])
        self.animated_qr_code()

    def animated_qr_code(self):
        image = self.qr_images[self.data_index]
        self.canvas.itemconfig(self.canvas_image, image=image)
        self.data_index = (self.data_index + 1) % len(self.data_list)
        self.tk_root.after(self.FREQ, self.animated_qr_code)

    def seed_phrase_panel(self):
        panel_frame = Frame(self.frame, bg=BG_COLOR)
        panel_frame.pack(side='right',anchor="n", padx=10, pady=10)

        # Seed phrase panel title
        text_label = Label(panel_frame, text="Enter Seed Phrase", font=("Arial", 18), bg=BG_COLOR, fg=FILL_COLOR)
        text_label.pack(side='top', anchor="n", padx=10, pady=10)

        # Seed phrase text input
        entry = Entry(panel_frame, font=("Arial", 12), bg=TEXT_INPUT_BG_COLOR, fg=TEXT_INPUT_FG_COLOR, width=100)
        entry.pack(side='top', anchor="w", padx=10, pady=2)
        try:
            # Prepopulate with seed phrase, if exists
            if '' != CONFIG[CONF_KEY]['SEED_PHRASE']:
                entry.insert(0, CONFIG[CONF_KEY]['SEED_PHRASE'])
        except NameError:
            pass
        
        # Button with callback function (process_seed)
        button = Button(panel_frame, text="Submit", command=lambda: self.process_seed(entry.get()))
        button.pack(side='top', anchor="w", padx=10, pady=10)

    def process_seed(self, seed_phrase_str):
        seed_phrase = seed_phrase_str.split()
        
        # Display error message on QR splash screen if 'try' fails
        try:
            XpubQrEncoder(seed_phrase)
        except SeedInitializationError as e:
            self.qr_panel_splash_screen(str(e))

        ur_xpub_qr_encoder = UrXpubQrEncoder(seed_phrase)
        self.update_qr_panel(ur_xpub_qr_encoder.data_list)

class SeedInitializationError(Exception):
    pass

class XpubQrEncoder(): # https://github.com/SeedSigner/seedsigner/blob/dev/src/seedsigner/models/encode_qr.py#L358
    def __init__(self, seed_phrase):
        network: str = CONFIG[CONF_KEY]['NETWORK']
        derivation = CONFIG[CONF_KEY]['DERIVATION']

        wordlist_language_code: str = SettingsConstants.WORDLIST_LANGUAGE__ENGLISH
        wordlist = Seed.get_wordlist(wordlist_language_code)

        if wordlist is None:
            raise Exception('Wordlist Required')

        # print(self.derivation)
        # sys.exit(1)

        version = bip32.detect_version(derivation, default="xpub", network=NETWORKS[SettingsConstants.map_network_to_embit(network)])
        
        """
        If Seed() method return an error, raise exception.
        This stops the code proceeding any further here and results in
        the process_seed() method (ExportXpub class) passing the error message
        to the qr_panel_splash_screen() method (ExportXpub class).
        This results in the error message being displayed on the splash screen.
        """
        try:
            self.seed = Seed(mnemonic=seed_phrase, wordlist_language_code=wordlist_language_code)
        except Exception as e:
            raise SeedInitializationError(f"{e}") from e
            # sys.exit(1)

        self.root = bip32.HDKey.from_seed(self.seed.seed_bytes, version=NETWORKS[SettingsConstants.map_network_to_embit(network)]["xprv"])
        self.fingerprint = self.root.child(0).fingerprint
        self.xprv = self.root.derive(derivation)
        self.xpub = self.xprv.to_public()

        # Convert xpub to zpub
        self.xpub_base58 = self.xpub.to_string(version=version)
        self.qr_max_fragment_size = 30


class UrXpubQrEncoder(XpubQrEncoder): # https://github.com/SeedSigner/seedsigner/blob/dev/src/seedsigner/models/encode_qr.py#L466
    def __init__(self, seed_phrase):
        super().__init__(seed_phrase)

        # derivation = "m/84h/0h/0h"
        derivation = CONFIG[CONF_KEY]['DERIVATION']

        # print(seed_phrase)
        print(self.xpub)

        def derivation_to_keypath(path: str) -> list:
            arr = path.split("/")

            if arr[0] == "m":
                arr = arr[1:]
            if len(arr) == 0:
                return Keypath([],self.root.my_fingerprint, None)
            if arr[-1] == "":
                arr = arr[:-1]

            for i, e in enumerate(arr):
                if e[-1] == "h" or e[-1] == "'":
                    arr[i] = PathComponent(int(e[:-1]), True)
                else:
                    arr[i] = PathComponent(int(e), False)

            return Keypath(arr, self.root.my_fingerprint, len(arr))

        origin = derivation_to_keypath(derivation)

        self.ur_hdkey = HDKey({ 'key': self.xpub.key.serialize(),
            'chain_code': self.xpub.chain_code,
            'origin': origin,
            'parent_fingerprint': self.xpub.fingerprint})
        
        ur_outputs = []
        if len(origin.components) > 0:
            if origin.components[0].index == 84: # Native Single Sig
                ur_outputs.append(Output([SCRIPT_EXPRESSION_TAG_MAP[404]], self.ur_hdkey))

        ur_account = Account(self.root.my_fingerprint, ur_outputs)
        qr_ur_bytes = UR("crypto-account", ur_account.to_cbor())
        ur2_encode = UREncoder(ur=qr_ur_bytes, max_fragment_len=self.qr_max_fragment_size)

        self.data_list = []
        loop_total = ur2_encode.fountain_encoder.seq_len()
        for _ in range(loop_total):
            data = ur2_encode.next_part().upper()
            self.data_list.append(data)
        
        pprint(self.data_list)

        '''
        qr = QR()
        loop_total = ur2_encode.fountain_encoder.seq_len()
        for _ in range(loop_total):
            # print(ur2_encode.next_part().upper())
            image = qr.qrimage(
                data=ur2_encode.next_part().upper(),
                width_height=480,
                border=2
            )
            # image.show() # Display QR-code
            time.sleep(5 / 30.0)
        '''


if __name__ == '__main__':
    tk_root = Tk()
    ExportXpub(tk_root)
    tk_root.mainloop()
