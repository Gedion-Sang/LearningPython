import pyqrcode
from pyqrcode import Image
link = input(":nEnter the URL to generate a QR code: ")
qr_code = pyqrcode.create(link)
qr_code.png("QRCode.png", scale=10)
Image.open("QRCode.png").show()
