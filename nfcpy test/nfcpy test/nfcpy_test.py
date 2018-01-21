import nfc
from nfc.clf import RemoteTarget
import time

def on_connect(tag):
    print('connect')
    print(tag)

def on_release(tag):
    print('release')
    print(tag)



with nfc.ContactlessFrontend('usb') as clf:
    target = clf.sense(RemoteTarget('106A'), RemoteTarget('106B'), RemoteTarget('212F'))
    print(target)

    while (True):
        clf.connect(rdwr={
            'on-connect': on_connect, 
            'on-release': on_release, 
            'beep-on-connect': True,
            })
        time.sleep(1)
        print('retry.')

    clf.close()