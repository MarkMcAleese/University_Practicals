from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import rsa

# Generate a private and public key pair
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
)

# Serialize the private key
private_pem = private_key.private_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PrivateFormat.TraditionalOpenSSL,
    encryption_algorithm=serialization.NoEncryption()
)

# Save the private key to a file
with open('private_key.pem', 'wb') as f:
    f.write(private_pem)

# Serialize the public key
public_key = private_key.public_key()
public_pem = public_key.public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo
)

# Save the public key to a file
with open('public_key.pem', 'wb') as f:
    f.write(public_pem)

# Text to be signed
text = b'This is the text to be signed.'

# Sign the text using the private key
signature = private_key.sign(
    text,
    padding.PKCS1v15(),
    hashes.SHA256()
)

# Save the signature to a file
with open('signature.bin', 'wb') as f:
    f.write(signature)

# Verify the signature
with open('public_key.pem', 'rb') as f:
    public_key = serialization.load_pem_public_key(f.read())

with open('signature.bin', 'rb') as f:
    signature = f.read()

try:
    public_key.verify(
        signature,
        text,
        padding.PKCS1v15(),
        hashes.SHA256()
    )
    print('Signature is valid.')
except Exception as e:
    print('Signature is not valid:', e)