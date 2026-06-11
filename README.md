# CipherVault-DB
An enterprise-grade data encryption layer for relational databases. Implements AES-256 GCM encryption to ensure Data-at-Rest security and PII protection."
# CipherVault-DB

Enterprise-grade encryption layer for protecting Personally Identifiable Information (PII) within relational databases.

## Features

- **AES-256-GCM** encryption for column-level data protection
- **Key management** with secure key rotation
- **PostgreSQL** and **MySQL** support
- **Zero-downtime encryption** for existing tables
- **Audit logging** for all encryption operations

## Quick Start

```bash
git clone https://github.com/Mustafa-SeniorDev/ciphervault-db.git
cd ciphervault-db
pip install -r requirements.txt
python src/main.py
Technical Architecture

· Encrypts data before writing to database
· Stores encryption keys in separate key store (environment variables / KMS)
· Implements authenticated encryption (GCM mode)
· Base64 encoding for safe storage in VARCHAR columns

Performance

· <5ms overhead per encryption operation
· Parallel processing for bulk operations
· Connection pooling support for high-throughput systems

Use Cases

· Protecting PII in compliance with GDPR, CCPA, PCI-DSS
· Securing healthcare records (HIPAA)
· Financial transaction data protection

License

MIT

Author

Mustafa Ramadhani – Senior Quantitative Systems & Data Engineer
