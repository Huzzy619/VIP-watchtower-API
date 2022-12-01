import string
import random
def create_api_key():
    length = 60
    key = ''.join(random.choices(string.ascii_letters + string.digits, k=60))
    return key