#!/usr/bin/env python
import bcrypt

password = b's$cret12'

salt = bcrypt.gensalt()
hashed = bcrypt.hashpw(password, salt)

print(salt)
print(hashed)

import http.client

conn = http.client.HTTPSConnection("")

payload = "grant_type=client_credentials&client_id=%24%7Baccount.clientId%7D&client_secret=YOUR_zaP1ZH50JprRiLExbwip-K7bbXt1tj1zydSwbxF85pnbbtxqgLxg0bsh2hDtkOwI&audience=messagesAPI"

headers = { 'content-type': "application/x-www-form-urlencoded" }

conn.request("POST", "/dev-f1z64pkl.us.auth0.com/oauth/token", payload, headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))