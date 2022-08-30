import pyqrcode
from svglib.svglib import svg2rlg
from reportlab.graphics import renderPM

#representing string which cases your url
string = 'https://www.instagram.com/mylnitsa.shop/'
#creating te QR
url = pyqrcode.create(string)
#QRcode saveng
url.svg('myQR.svg', scale = 8)
#converting SVG to PNG format and saving
drawing = svg2rlg('myQR.svg')
renderPM.drawToFile(drawing, 'MyQRcode.png', fmt = 'PNG')