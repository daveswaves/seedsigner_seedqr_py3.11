import tkinter as tk
from PIL import Image, ImageTk
from helpers.qr import QR


def run_encode_decode_test():
    data = '110301551596063900810786062915601161029816801682'

    width_height = 480

    qr = QR()
    image = qr.qrimage(
        data=data,
        width_height=width_height,
        border=2
    )

    image.save("qrcode.png")

    root = tk.Tk()
    root.title("Tkinter QR Code")

    canvas = tk.Canvas(root, width=width_height, height=width_height)
    canvas.pack()

    img = Image.open("qrcode.png")
    photo = ImageTk.PhotoImage(img)

    canvas.create_image(0, 0, anchor=tk.NW, image=photo)

    root.mainloop()


run_encode_decode_test()
