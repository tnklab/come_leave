import binascii
import nfc
import time
from threading import Thread,Timer


class MyCardReader(object):
    def on_connect(self,tag):
        print("touched")
        self.idm = binascii.hexlify(tag.idm)
        return True
    def read_id(self):
        clf = nfc.ContactlessFrontend('usb')
        try:
            clf.connect(rdwr={'on-connect': self.on_connect})
        finally:
            clf.close()
if __name__ == '__main__':
    cr = MyCardReader()
    print("Touch card:")
    cr.read_id()
    print("released")
    print(cr.idm)