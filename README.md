# Demonstrating Proof of Ownership RFC7800 Demonstrator

This is a quick dpop implementation using authlib overloading the JsonWebToken.encode method.
Create EC key with openssl:
```
openssl ecparam -genkey -name prime256v1 -noout -out privkey.pem
openssl ec -in privkey.pem -pubout -out pubkey.pem
```
Then run dpop.py
`

