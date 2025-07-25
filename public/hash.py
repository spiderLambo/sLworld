import hashlib

class Hashit:
    def hashing(self,texte,hash_type):
        texte=texte.encode('utf-8')
        hash_1=hashlib.new(hash_type)
        hash_1.update(texte)
        return hash_1.hexdigest()

Hash=Hashit()

def hash(text, username):
    return Hash.hashing(text + username, 'md5')
