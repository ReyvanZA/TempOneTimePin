import pyotp
import time
import pyqrcode

base32secret = 'FE5ATLG3A5TAEOZA'

print('Secret:', base32secret)

totp_uri = pyotp.totp.TOTP(base32secret).provisioning_uri("devnullpy@gmail.com", issuer_name="ReyvanZA")

print(totp_uri)

totp = pyotp.TOTP(base32secret)
print('OTP code:', totp.now())

url = pyqrcode.create(totp_uri)
url.png('scan.png')


