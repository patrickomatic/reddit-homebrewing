""" 
I need a secret key that can be used to sign the token used in this form.  
Ideally I would use settings.SECRET_KEY, however this is available on github so 
anybody could use that to create a invalid signature and fake a confirmation of 
a user.  Instead I'll use a secret hash computed from /dev/urandom.
"""
import hashlib

fh = open('/dev/urandom', 'r')
secret_key = hashlib.sha256(fh.read(256)).hexdigest()
fh.close()

