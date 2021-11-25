import hashlib
import base64


def hash_base64(password):
    return base64.b64encode(hashlib.sha256(password.encode('utf-8')).digest())


print(hash_base64("myVerySecurePassword"))
