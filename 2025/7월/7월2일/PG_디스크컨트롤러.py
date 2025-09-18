from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5
from base64 import b64encode

# PEM 형식으로 변환한 공개키
public_key_pem = """
-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEApm7RFqlurGGqgoze4OJy
Zawg03Jj9kk/mhhiBYPP7w7g3oPUxQ4/Xdu4o0PE/N39nqULxTf89DCRAoCtWApn
Ec45MoIOKgGreZjHoDgPNxbQw335Ivb3Fuw9F/B3sdG8P+36Qf/aTLBWdVBAsDsp
WV5V68e8uA0Hi+gg+7lhVIkF1JGfLi0r/9Jm0EN/Rj/8ik+zi+UejpHI9zdyKRI0
E9MxhoI6e7HM3YJ93rMGqAVDim+gzVgZAUbsUnW4cGGXX5QiFAChqq/07E3WJDjU
1hmyC5z7RE6zrZKFVcOS0Jx1sMjy146eS3k2xUrlBsNekCcx0uy6S/oY1XJWh1s3
sQIDAQAB
-----END PUBLIC KEY-----
"""

# 암호화할 비밀번호
password_plain = "!Adlehddnr98"

# RSA 암호화
key = RSA.importKey(public_key_pem)
cipher = PKCS1_v1_5.new(key)
encrypted_bytes = cipher.encrypt(password_plain.encode('utf-8'))
encrypted_password = b64encode(encrypted_bytes).decode('utf-8')

print(encrypted_password)
