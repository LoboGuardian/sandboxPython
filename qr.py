import qrcode
from PIL import Image

def generate_qr_code(data, filename, size=300, fill_color="black", back_color="white"):
    """
    Generates a QR code image.

    Args:
        data: The data to be encoded in the QR code.
        filename: The filename for the saved QR code image.
        size: The size of the QR code image in pixels.
        fill_color: The color for the QR code modules.
        back_color: The color for the background of the QR code.
    """

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=size // 20,  # Adjust box size based on image size
        border=4
    )

    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color=fill_color, back_color=back_color)

    # Resize image to specified size using PIL
    img = img.resize((size, size), Image.ANTIALIAS)

    img.save(filename)

if __name__ == "__main__":
    data = "https://www.example.com"
    filename = "example_qr.png"
    size = 500

    generate_qr_code(data, filename, size)
    print("QR code generated successfully!")