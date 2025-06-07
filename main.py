# Importing The Libraries
import pyqrcode
import png
import random

# Give The Website Name Or Whatever You Wan't To Make The QR code
qr_code_link = "https://www.youtube.com"

# Generate The qr_code
generating_qr_code = pyqrcode.create(qr_code_link)

# Using The Random Function To Use In The File
generate_the_numbers_of_file = random.randint(1, 10000)

# Asking The File Name
file_name = input("Enter The File Name (Don't Use Number Only Text) : ")

# Saving The QR_Code In SVG File
generating_qr_code.png(f"{file_name}_{generate_the_numbers_of_file}.png", scale=6)
