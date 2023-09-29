import cv2
import qrcode
from pyzbar.pyzbar import decode

# Function to generate a QR code
def generate_qr_code(data, filename):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(filename)

# Function to scan a QR code from an image
def scan_qr_code(image_path):
    # Read the image using OpenCV
    image = cv2.imread(image_path)

    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Use pyzbar to decode the QR code
    decoded_objects = decode(gray)

    if not decoded_objects:
        print("No QR code found in the image.")
        return

    # Print the decoded information from the QR code
    for obj in decoded_objects:
        print(f"Type: {obj.type}")
        print(f"Data: {obj.data.decode('utf-8')}")

if __name__ == "__main__":
    # Generate a sample QR code
    data_to_encode = "https://www.example.com"
    qr_code_filename = "example_qr_code.png"
    generate_qr_code(data_to_encode, qr_code_filename)
    print(f"QR code generated as {qr_code_filename}")

    # Scan the generated QR code
    scan_qr_code("my_qr_code.png")
    scan_qr_code(qr_code_filename)
    
