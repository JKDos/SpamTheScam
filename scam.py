import requests
import os
import random
import string
import json
import time
#import pyperclip
import urllib3

# There are more imports then really needed. I've been experimenting with data retention.
###########

_HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:55.0) Gecko/20100101 Firefox/55.0',
}

_YOUR_COMPANY = "acme.com" # Enter your company's email domain here. This will should help the scammers think their attack on your employees was successful.

_URL = '' # This may be the url with the form or the url the form submit if calling. Check the headers to comfirm.


chars = string.ascii_letters + string.digits + '!@#$%^&*'
random.seed = (os.urandom(1024))

decision = 0
passwd = 'qwerty123'
usern = 'admin'
xname = '01'

total = 0

urllib3.disable_warnings()

# Despite the JSON name, these are just arrays.
names = json.loads(open('someNames.json').read()) # About 30,000 names here
passwds = json.loads(open('passwd.json').read()) # A small collection of the most used passwords I've found for dictionary attacks
theE = json.loads(open('emails.json').read()) # A hand-made collection of domains.


def buildName(daName,daNum):
    pass

def buildExtra(daExtras,daNum):
    if (daNum < 5):
        daExtras = str(random.randint(0,9999))
    elif (daNum < 15):
        daExtras = str(random.randint(-100,0))
    elif (daNum < 40):
        daExtras = '_' + random.choice(names)
    elif (daNum < 60):
        daExtras = ''.join(random.choice(string.ascii_letters).lower() for i in range(random.randint(1,5)))
    else:
        daExtras = str(random.randint(10,999))

    return daExtras

def buildPass(daPass,daNum):
    if (daNum < 10):
        daPass = random.choice(passwds) + random.choice(names)
    elif (daNum < 20):
        daPass = random.choice(passwds) + ''.join(random.choice(chars) for i in range(3))
    else:
        daPass = random.choice(passwds) + ''.join(random.choice(string.digits) for i in range(2))

    return daPass


# Main loop. This is where we send the fake email credentials.
for name in names:

    # build a name
    decision = random.randint(0,100)
    #usern = buildName(name,decision).lower

    # build extras
    decision = random.randint(0,100)
    xname = buildExtra(xname,decision)

    # build a Password
    decision = random.randint(0,100)
    passwd = buildPass(passwd,decision)

    decision = random.randint(0,100)
    if (decision > 70):
        random_provider = _YOUR_COMPANY
    else:
        random_provider = random.choice(theE)

    username = name.lower() + xname + '@' + random_provider
    password = passwd

#    pyperclip.copy(passwd);

    # Collect the form data from the headers and reconstruct the _POST object to match.
    post={
        'user_name': username,
        'pass_word': password
    }

    response = requests.post(_URL, allow_redirects=False, verify=True, data=post, headers=_HEADERS)


    # Beautiful, Clean output
    fakeoutput = '{0:25} @ {1:25} > {2:10}'.format(name.lower() + xname,random_provider, password)

    total = total + 1
    #print(response.content)
    print(fakeoutput)
