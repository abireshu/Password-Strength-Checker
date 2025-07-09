import hashlib
import requests

def check_pwned(password):
    
    sha1_password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    prefix = sha1_password[:5]
    suffix = sha1_password[5:]
    
    
    url = f"https://api.pwnedpasswords.com/range/{prefix}"
    response = requests.get(url)
    if response.status_code != 200:
        return False, "Error checking password breach status."
    
    
    hashes = (line.split(':') for line in response.text.splitlines())
    for hash_suffix, count in hashes:
        if hash_suffix == suffix:
            return True, f"⚠️This password has appeared in data breaches {count} times!"
    return False, "🟢This password has not been found in known breaches."
