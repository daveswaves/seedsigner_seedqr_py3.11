'''
python src/tk_seedqr_animated.py
'''

import tkinter as tk
from PIL import Image, ImageTk
from helpers.qr import QR

def animated_qr_code(FREQ, data_index = 0):
    image = qr_images[data_index]
    canvas.itemconfig(canvas_image, image=image)
    data_index = (data_index + 1) % len(data_list)
    root.after(FREQ, animated_qr_code, FREQ, data_index)

BG_COLOR = "#000"
FILL_COLOR = "#0f0"

# Create the Tkinter window
root = tk.Tk()
root.title("Export Xpub")

frame = tk.Frame(root, bg=BG_COLOR)
frame.pack(fill=tk.BOTH, expand=True)

WIDTH_HEIGHT = 480
canvas = tk.Canvas(frame, width=WIDTH_HEIGHT, height=WIDTH_HEIGHT)
canvas.pack(side=tk.LEFT, padx=10, pady=10)

# Create a Label for displaying text on the right (position top, not default middle)
text_label = tk.Label(frame, text="To my dearest Catharine\n Happy Birthday", font=("Arial", 18), width=30, bg=BG_COLOR, fg=FILL_COLOR)
text_label.pack(side=tk.RIGHT, anchor="n", padx=10, pady=40)

data_list = [
    'UR:CRYPTO-ACCOUNT/1-4/LPCFADJKAACSJKCYCHFXSWPFHDCAEMNSPSCEAYFSCNISNELYDLYNHPDLVTTTFTKPLUMKDPTKWEWDLFAXDMFMLEGTSEGOTL',
    'UR:CRYPTO-ACCOUNT/2-4/LPCFADJYAACSJKCYCHFXSWPFHDCAWYLONBASLOAEIMFGVDIEGOVSFGHHPYNNHGSTPKTKFRJEZTGMKGFWRYVLTALYHYFMLK',
    'UR:CRYPTO-ACCOUNT/3-4/LPCFADKPAACSJKCYCHFXSWPFHDCAGEGDRKEYAXECESHHEYFDGHLDNEPDLNCXHERLRSCFBSHEVTWKBADNSPVAOYJOPDWNRP',
    'UR:CRYPTO-ACCOUNT/4-4/LPCFADKOAACSJKCYCHFXSWPFHDCAOEADCYBDDEEETLAOLYTAADMWTAADDLOXAXHDCLAXEMEMBBRFOYHSLSGMKSWMRYMWWN',
]


qr = QR()
qr_images = []
for data in data_list:
    image = qr.qrimage(data=data, width_height=WIDTH_HEIGHT, border=2)
    qr_images.append(ImageTk.PhotoImage(image))

canvas_image = canvas.create_image(0, 0, anchor=tk.NW, image=qr_images[0])

FREQ = int(1000 * 5 / 30.0)
animated_qr_code(FREQ)

root.mainloop()
