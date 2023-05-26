import qrcode 


#Example 1
#img = qrcode.make("Hello World! This is Social Soft Tech")
#img.save("myqr.png")


#Example 2
#qr = qrcode.QRCode(version=1,
                   #error_correction=qrcode.constants.ERROR_CORRECT_L,
                   #box_size=50,
                   #border=1)

#qr.add_data("https://bannersbyroz.com/")
#qr.make(fit=True)

#img.save("BannersbyrozQR.png")


#Example 3

# Define the contact information to be encoded in the QR code
contact_info = {
    'FN': 'Earnie Mac',
    'ORG': 'EA Transport',
    'TITLE': 'CEO',
    'TEL': '+1 (832) 382-3786',
    'EMAIL': 'ernieg30@gmail.com',
}

# Define the filename and format of the generated QR code image
filename = 'Earnest_business_card.png'
image_format = 'PNG'

# Generate the QR code image using the qrcode library
qr = qrcode.QRCode(
    version=1,
    box_size=10,
    border=5,
    error_correction=qrcode.constants.ERROR_CORRECT_Q,
    #box_alignment=1,
)
qr.add_data('BEGIN:VCARD\n' + '\n'.join([f'{k}:{v}' for k, v in contact_info.items()]) + '\nEND:VCARD')
qr.make(fit=True)

# Save the QR code image to a file
img = qr.make_image(fill_color='black', back_color='white')
img.save(filename, format=image_format)

# Print a message to confirm that the QR code image was saved
print(f'QR code saved to file {filename}')
