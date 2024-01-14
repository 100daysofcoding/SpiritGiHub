import cv2


qrfile = input("Entrez le lien vers le QR code : ")
d = cv2.QRCodeDetector()

val, points, qrcode = d.detectAndDecode(cv2.imread(qrfile))

if val:
    print("Données du QR Code:", val)
else:
    print("Aucun QR code détecté dans l'image.")
