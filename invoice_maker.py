import pandas as pd
import os
from PIL import Image, ImageDraw, ImageFont
import textwrap
from tabulate import tabulate
import time
from tabulate import tabulate
import datetime

now = "billed on : " + str(datetime.datetime.now())
name = input("enter the name : ")    


im = Image.open(r'invoice.png')
name = str(name.upper())
d = ImageDraw.Draw(im)
location = (180, 371)
text_color = (23, 23, 23)
font = ImageFont.truetype("font/Lato-Regular.TTF", 60)
d.text(location, name, fill = text_color, font = font)


d = ImageDraw.Draw(im)
location = (70, 1581)
text_color = (23, 23, 23)
font = ImageFont.truetype("font/A.TTF", 50)
d.text(location, now, fill = text_color, font = font)



d = ImageDraw.Draw(im)
location = (180, 571)
text_color = (23, 23, 23)
font = ImageFont.truetype("font/m.TTF", 50)
d.text(location, "Service", fill = text_color, font = font)


d = ImageDraw.Draw(im)
location = (1200, 571)
text_color = (23, 23, 23)
font = ImageFont.truetype("font/m.TTF", 50)
d.text(location, "Number", fill = text_color, font = font)

d = ImageDraw.Draw(im)
location = (1500, 571)
text_color = (23, 23, 23)
font = ImageFont.truetype("font/m.TTF", 50)
d.text(location, "Price", fill = text_color, font = font)

locate = 671
total = 0
service = ""

while service != "bill":
    
    
    service = input("enter the service : ")
    if service == "bill":
        break
    number = input("enter the numbers : ")
    price = input("enter the price : ")
    
    d = ImageDraw.Draw(im)
    location = (1200, locate)
    text_color = (23, 23, 23)
    font = ImageFont.truetype("font/A.TTF", 50)
    d.text(location, number, fill = text_color, font = font)
    
    d = ImageDraw.Draw(im)
    location = (180, locate)
    text_color = (23, 23, 23)
    font = ImageFont.truetype("font/A.TTF", 50)
    d.text(location, service, fill = text_color, font = font)
    
    
    d = ImageDraw.Draw(im)
    location = (1500, locate)
    text_color = (23, 23, 23)
    font = ImageFont.truetype("font/A.TTF", 50)
    d.text(location, price, fill = text_color, font = font)
    total = total + int(price)
    locate += 70

d = ImageDraw.Draw(im)
location = (180, 1400)
text_color = (23, 23, 23)
font = ImageFont.truetype("font/m.TTF", 50)
d.text(location, "TOTAL", fill = text_color, font = font)

d = ImageDraw.Draw(im)
location = (1500, 1400)
text_color = (23, 23, 23)
font = ImageFont.truetype("font/m.TTF", 60)
d.text(location, ("₹ " + str(total)), fill = text_color, font = font)

save_location = "invoices/"+  str(name) + "invoice_" + ".png"
im.save(save_location, "PNG")
os.startfile(os.getcwd() + "/" + "invoices")
os.startfile(os.getcwd() + save_location)