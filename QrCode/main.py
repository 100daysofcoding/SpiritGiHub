import qrcode
from qrcode.constants import ERROR_CORRECT_L

qr_data = input("Entrez le lien ou le texte pour le QR code : ")


qr = qrcode.QRCode(
    version=1,
    error_correction=ERROR_CORRECT_L,
    box_size=10,
    border=4,
)


qr.add_data(qr_data)
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")


img.save('qrcode.png')

print("QR code généré et enregistré sous 'qrcode.png'")
