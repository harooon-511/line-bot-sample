import jwt
from jwt.algorithms import RSAAlgorithm
import time

privateKey ={
  "alg": "RS256",
  "d": "DFMZRJg63EnH0Fuzaswg3p6XFGMoQReZyfw-Pm1Ag5tT0aXUkciZGUjpNY8O3uX-LI3LgWiVxtmDA22Bqby3IJX96KkRixiyepaxcXvOhVbBFezdcrnUBOJ_X1Agosuhj9FepNSWnwkRNTApA5LCZdNLfdIFKj8uf9672eLSI8BTxEoT-aZTT4yrAV-WNsn8Ge2xbJ6Gazw20D193l4UXcQgRidWUdq-nFpXdcDgtXpcvfDSuVVx4fG-yQzkay1dwHOuLURNPZr9RQKvQPm0ioZ3NmB6qvqzpdcBN9MCTEJFWGisuDkSotHJo-bgHY7IHp_vg_h28JXBtC66zkrh",
  "dp": "PFvdJYNTGzs-SSoo7NQuhLu7ISYl88Em6KuSeiMHRmv8gzjfoHTMEumbVTo7i7E2FNGGMc5ORV7bo02qp3xq2pKQMsj-TksPsKmt8BUK29sY83MZ1jyGJ9Br_zkUDLgIAXboKpHfLkEnPmwT7JrtotuW9D4iD0Et2qk3YsLUwAE",
  "dq": "uLHhDJX0sj1uvRZdXC0oKlTGjm5aBXq_i5Bm377DKzaJKrtPDDESVBskE0-E2Zd7WvdogfKrYrOmPpWqh5vHeLFUzZ4sUIbfJZ6WkQB6BcraCYpgkuKSxm_NQVt5Mt2WXLCcqJDP9SkwHIu1fQL1Ak7lwjK-q0eRgTzUx4_Kqr8",
  "e": "AQAB",
  "kty": "RSA",
  "n": "uZjMsBaOYifFTWIavDVkZZ2C_6k21pRnn2nlVWHR7tBv0nMwcqgrZ6XLNEBCtA0BF0rTt8Ug6G3Bs8uX9JxJQMWO-sNsevSQMXsPijDxAjFRr-EjvZq_7J5eOWHhHPT2Ug4G8_RwNpHli1_k7O2HF91BAbxpMTJll13drvsPcgi8zmWelAygtttmodOpiWA5t_bbUoyFRYNQ7eqGk4sF87XwlHAXg7pbdpFF1EsWYueNz2-nNhHeN0Frk6jp03Xi-b7Bl3bZU0dSXj4MXFKyfwkV4FqWpqly02WPSeQPriiEcKkgmXyNUvGrYn1VgVFvrCbtxHCluG4HgisScAR5dw",
  "p": "y1EtfeajxT3PN0TenkcYv7a8K2KeqBfuBiNN-Ehwi58yTi0XEfP0T909dVYdjThxw3fvM6Nekx7AB0fDOcb6aGMWzqWy1S0GrjqCBe8XYVdugdfA9wfz2LfW8VR20CixmT-0pqiMohwShU6Oo_wif0d_XcBLH58erp6NoZutgtE",
  "q": "6bArZ_zNvfNm27av5Eut5RGYIxhnGNbXDdLUMk05YDi4dJ9e4FCm9YjNAHy_Cbuw9DTSS3I4R9Zo4NaBIXTZEj8K2msIGqAfD28IAnJaDSQiAWVS-UyC2_VIjgcPeerXw_mKw0zU7VaciJEUGqvWIm2XrAWPPCefNmwPYfIfecc",
  "qi": "dATu5DuspKLtU7MEOTouywr3Bm_faO5Uln70NnHeEY2xavTHlUGQ2mSktFsmiRRiiNJGaYkbIh8Teb-98j06e7A31zdxIlZ-4OMdR8qeSTOEpuft8schn-qUTz1afIpFIjomTpWcFhTrNUWPPKx6XITiFs0AhlxK4bilNOMBH-o",
  "use": "sig"
}

headers = {
    "alg": "RS256",
    "typ": "JWT",
    "kid": "b24d8aaa-41a2-4c5e-b2c2-1ed4d234ff27"
}

payload = {
  "iss": "1657560388",
  "sub": "1657560388",
  "aud": "https://api.line.me/",
  "exp":int(time.time())+(60 * 30),
  "token_exp": 60 * 60 * 24 * 30
}

key = RSAAlgorithm.from_jwk(privateKey)

JWT = jwt.encode(payload, key, algorithm="RS256", headers=headers, json_encoder=None)
print(JWT)