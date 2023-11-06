import tkinter as tk
from PIL import Image, ImageTk
from helpers.qr import QR

data_index = 0

def animated_qr_code(ANIM_FREQ):
    global data_index

    # Get the next QR code image
    image = qr_images[data_index]

    # Update the canvas with the new QR code
    canvas.itemconfig(canvas_image, image=image)

    # Increment the data index, loop back to 0 if at the end of the list
    data_index = (data_index + 1) % len(data_list)

    # Schedule the next update after 1000 milliseconds (1 second)
    root.after(ANIM_FREQ, animated_qr_code, ANIM_FREQ)

# Create the Tkinter window
root = tk.Tk()
root.title("Animated QR-Code")

# Create the canvas
width_height = 480
canvas = tk.Canvas(root, width=width_height, height=width_height)
canvas.pack()

data_list = [
    '110301551596063900810786062915601161029816801682',
    '039311660064157412100460103703710259041007321627',
    '176801481597155801271723198905671360117209981400',
    '079109580935054206371240033117561800039706661127',
    '090415241574202915021138113318370973069307720970',
    '008817990829164913750416140216330820075911140576',
]

# Create and save all the QR code images
qr = QR()
qr_images = []
for data in data_list:
    image = qr.qrimage(data=data, width_height=width_height, border=2)
    qr_images.append(ImageTk.PhotoImage(image))

# Initially, create the canvas image and set it to the first QR code
canvas_image = canvas.create_image(0, 0, anchor=tk.NW, image=qr_images[0])

# Start the update loop to show QR codes one by one
ANIM_FREQ = 200
root.after(ANIM_FREQ, animated_qr_code, ANIM_FREQ)

root.mainloop()
