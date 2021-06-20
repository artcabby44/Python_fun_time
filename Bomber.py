import random
import string
import requests

s = requests.session()
while True:
    uname_size = random.randint(5,10)
    uname = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase + string.digits, k = uname_size))
    mail = uname + "@gmail.com"
    passwd_size = random.randint(8,20)
    passwd = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase + string.digits, k = passwd_size))
    print(mail)
    print(passwd)

    payload = {
        'email': mail,
        'pass' : passwd,
        }
    response = s.post("http://localhost/fakebook/login.php",data = payload)
    print(response.status_code)
