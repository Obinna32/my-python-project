"""LOGIC SIDE:
STEP 1: TAKE DATA INPUT
STEP 2: ENCODE TO QR FORMAT
STEP 3: ADD ERROR CORRECTION
STEP 4: SAVE AS IMAGE"""

import qrcode

def create_qr(data, filename="my_qr.png"):
    qr = qrcode.QRCode(
        version=1, #Size of QR code
        box_size=10, #Size of each box
        border=4 #Border thickness
    )

    #Add your data
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color = "black", back_color="white")

    img.save(filename)
    print(f"QR saved as {filename}")

create_qr("https://127.0.0.1/")