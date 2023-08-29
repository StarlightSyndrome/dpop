#!/lhome/hulandg/.cache/pypoetry/virtualenvs/dpop-3FM0kS-w-py3.10/bin/python
import authlib.jose
from authlib.jose.rfc7519 import jwt
from authlib.jose.rfc7518 import JWS_ALGORITHMS
import uuid
import datetime
import calendar
 


class DpopJsonWebToken(jwt.JsonWebToken):
    def encode(self, jwk, alg, htm, htu, key):
        """Encode a JWT with the given header, payload and key.

        :param jwk: A dict of JWK public key
        :param alg: the encryption algorithm
        :param htm: the HTML method
        :param htu: the API endpoint
        :param key: the private key
        :param check: check if sensitive data in payload
        :return: bytes
        """
        header = {
            "typ": "dpop+jwt",
            "alg": alg,
            "jwk": jwk
        }
        payload = {
            "jti": uuid.uuid4().hex,
            "iat": calendar.timegm(datetime.datetime.now().utctimetuple()),
            "htm": htm,
            "htu": htu,
        }


        key = jwt.find_encode_key(key, header)
        text = jwt.to_bytes(jwt.json_dumps(payload))
        return self._jws.serialize_compact(header, text, key)



key_data = open('pubkey.pem', 'r').read()
key = authlib.jose.JsonWebKey.import_key(key_data, {'kty': 'EC'})

jwk = key.as_dict()

dpop =  DpopJsonWebToken(list(authlib.jose.rfc7515.JsonWebSignature.ALGORITHMS_REGISTRY.keys()))

secret = open("privkey.pem", "r").read()

# Sign the JWT using the ERS256 algorithm
token = dpop.encode(jwk, "ES256", "POST", "https://some.server.example/api", secret)
print(token)

