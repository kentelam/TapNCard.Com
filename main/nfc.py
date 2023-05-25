import nfc
import pyqrcode
import os

# Create a new user object
class User:
    def __init__(self, uid, first_name, last_name, job_title, phone_number, email, website):
        self.uid = uid
        self.first_name = first_name
        self.last_name = last_name
        self.job_title = job_title
        self.phone_number = phone_number
        self.email = email
        self.website = website

# Create a function to scan an NFC card and create a new user object
def scan_card():
    # Create an NFC reader object
    reader = nfc.Nfc()

    # Scan for an NFC card
    card = reader.scan()

    # Get the card's UID
    uid = card.uid

    # Get the card's contact information
    first_name = card.get('first_name')
    last_name = card.get('last_name')
    job_title = card.get('job_title')
    phone_number = card.get('phone_number')
    email = card.get('email')
    website = card.get('website')

    # Create a new user object
    user = User(uid, first_name, last_name, job_title, phone_number, email, website)

    return user

# Create a function to generate a vcard for a user
def generate_vcard(user):
    # Create a vcard object
    vcard = pyqrcode.create(user.to_vcard())

    # Save the vcard to a file
    vcard.save('vcard/{}.vcf'.format(user.uid))

# Create a function to generate a QR code for a user
def generate_qr_code(user):
    # Create a QR code object
    qr_code = pyqrcode.create(user.to_url())

    # Save the QR code to a file
    qr_code.save('qrcode/{}.png'.format(user.uid))

# Create a function to create a new user profile
def create_profile(user):
    # Create a new profile directory
    directory = 'profile/{}'.format(user.uid)
    os.mkdir(directory)

    # Generate a vcard for the user
    generate_vcard(user)

    # Generate a QR code for the user
    generate_qr_code(user)

# Create a main function to run the program
def main():
    # Scan an NFC card
    user = scan_card()

    # Create a new user profile
    create_profile(user)

# Run the main function
if __name__ == '__main__':
    main()
