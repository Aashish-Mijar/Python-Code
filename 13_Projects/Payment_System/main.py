import qrcode

# Taking Wallet ID As a input
wallet_id = input("Enter your Wallet ID / Mobile Number = ")

# custom payment message
amount = input("Enter Amount (optional, press Enter to skip): ")
remarks = input("Enter Remakrs / Message (optional, press Enter to skip): ")

# Defining the payment URL based on the Wallet ID / Mobile Number and the payment app
# Can be modified these URLs based on the payment apps 
esewa_url = f'https://esewa.com.np/qr?sc=esewa&pa={wallet_id}&am={amount}&tn={remarks}'
khalti_url = f'https://khalti.com/pay?pa={wallet_id}&am={amount}&tn={remarks}'
imepay_url = f'https://imepay.com/pay?pa={wallet_id}&am={amount}&tn={remarks}'

# Create QR Codes for each payment app
esewa_qr = qrcode.make(esewa_url)
khalti_qr = qrcode.make(khalti_url)
imepay_qr = qrcode.make(imepay_url)

# Save the QR code to image file
esewa_qr.save('esewa_qr.png')
khalti_qr.save('khalti_qr.png')
imepay_qr.save('imepay_qr.png')

# Display the  qr codes (you may need to install pIL/pillow library)
esewa_qr.show()
khalti_qr.show()
imepay_qr.show()