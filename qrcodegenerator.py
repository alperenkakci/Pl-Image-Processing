import qrcode
import pyqrcode
import png
from pyqrcode import QRCode

girdi = input("Text=")
dosyadi = input("Dosya-adı=")

cikti = pyqrcode.create(girdi)
cikti.png((dosyadi+".png"),scale=6)
