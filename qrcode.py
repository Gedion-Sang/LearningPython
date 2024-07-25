import pyqrcode
from PIL import Image
link = input(":/nEnter the URL to generate a QR code:")
qr_code = pyqrcode.create(link)
qr_code.png("QRCode.png", scale=5)
Image.open("QRCode.png").show()

# Ensure you install pyqrcode and pillow libraries before running this script