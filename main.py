import pyqrcode
from svglib.svglib import svg2rlg
from reportlab.graphics import renderPM

#representing string which cases your url
print('Enter the URL address:')
string = input()
#creating the QR
url = pyqrcode.create(string)
#QRcode saving
url.svg('myQR.svg', scale = 8)
#converting SVG to PNG format and saving
drawing = svg2rlg('myQR.svg')
renderPM.drawToFile(drawing, 'MyQRcode.png', fmt = 'PNG')