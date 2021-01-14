import hashlib

def crack_sha1_hash(hash, use_salts=False):
    with open("top-10000-passwords.txt", 'r') as f:
        passwords = [x.strip() for x in f.readlines()]

    if use_salts:
        with open("known-salts.txt", 'r') as f:
            salts = [x.strip() for x in f.readlines()]
        for salt in salts:
            for password in passwords:
                salted = salt+password
                if str(hashlib.sha1(salted.encode()).hexdigest()) == hash:
                    return password

                salted = password+salt
                if str(hashlib.sha1(salted.encode()).hexdigest()) == hash:
                    return password
                
        return "PASSWORD NOT IN DATABASE"
        
    else:
        for password in passwords:
            if str(hashlib.sha1(password.encode()).hexdigest()) == hash:
                return password
        return "PASSWORD NOT IN DATABASE"
    