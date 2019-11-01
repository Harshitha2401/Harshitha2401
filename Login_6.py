import re

def email_validation(email):
    pattern='\w+@[a-z]+\.com$'
    match=re.search(pattern,email)
    if match:
        return True
    else:
        return False
