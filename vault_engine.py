import os
from cryptography.hazmat.primitives.ciphers.aead import AESGCM

# CipherVault-DB: Advanced Data-at-Rest Encryption Engine
# Author: Mustafa-SeniorDev (15+ Years Experience)

class CipherVault:
    """Handles high-level encryption/decryption for sensitive database fields."""

    def __init__(self, master_key: bytes = None):
        # Generate a secure 256-bit key if not provided
        self.key = master_key if master_key else AESGCM.generate_key(bit_length=256)
        self.aesgcm = AESGCM(self.key)

    def encrypt_data(self, plaintext: str) -> bytes:
        """Encrypts data using AES-256 GCM with a unique nonce."""
        nonce = os.urandom(12)  # Recommended nonce length for GCM
        ciphertext = self.aesgcm.encrypt(nonce, plaintext.encode(), None)
        return nonce + ciphertext

    def decrypt_data(self, encrypted_blob: bytes) -> str:
        """Extracts nonce and decrypts the ciphertext."""
        nonce = encrypted_blob[:12]
        ciphertext = encrypted_blob[12:]
        decrypted_data = self.aesgcm.decrypt(nonce, ciphertext, None)
        return decrypted_data.decode()

if __name__ == "__main__":
    # Demonstration of the Security Layer
    vault = CipherVault()
    
    sensitive_info = "Customer-SSN-999-00-1234"
    print(f"[*] Original Data: {sensitive_info}")

    # Protecting the data
    secure_blob = vault.encrypt_data(sensitive_info)
    print(f"[+] Encrypted Blob (Stored in DB): {secure_blob.hex()[:32]}...")

    # Retrieving the data
    decrypted = vault.decrypt_data(secure_blob)
    print(f"[+] Decrypted Result: {decrypted}")
