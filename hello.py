import qrcode

# Create a QRCode instance
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

# Add data to the QR code
data = "https://www.youtube.com/results?search_query=qr+code+generator+multiple+field++android+studio+java+"
qr.add_data(data)
qr.make(fit=True)

# Create an image from the QRCode instance
img = qr.make_image(fill_color="black", back_color="white")

# Save the image or display it
img.save("my_qr_code.png")