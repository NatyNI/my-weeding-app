import qrcode


url = "https://natyni.github.io/my-weeding-app/"

qr = qrcode.make(url)

qr.save("cod_qr.png")

print("The code QR has been created in 'cod_qr.png'.")