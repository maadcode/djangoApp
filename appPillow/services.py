from PIL import Image
import base64
import numpy as np

def identidad(url):
    imagen=Image.open(url)
    return tobase64(imagen)

def negativo(url):
    imagen=Image.open(url)
    array = imagen.load()
    for x in range(imagen.size[0]):
        for y in range(imagen.size[1]):
            r,g,b = imagen.getpixel((x,y))
            array[x,y] = (255-r, 255-g, 255-b)
    return tobase64(imagen)

def umbral(url):
    imagen=Image.open(url).convert("L")
    u=100
    array = imagen.load()
    for x in range(imagen.size[0]):
        for y in range(imagen.size[1]):
            if imagen.getpixel((x, y)) > u:
                array[x, y] = 255
            else:
                array[x, y] = 0
    return tobase64(imagen)


def invumbral(url):
    imagen=Image.open(url).convert("L")
    image=escala_gris(imagen)
    u=100
    array = imagen.load()
    for x in range(imagen.size[0]):
        for y in range(imagen.size[1]):
            if imagen.getpixel((x, y)) > u:
                array[x, y] = 0
            else:
                array[x, y] = 255
    return tobase64(imagen)


def biumbral(url):
    imagen=Image.open(url).convert("L")
    u1=40
    u2=190
    array = imagen.load()
    for x in range(imagen.size[0]):
        for y in range(imagen.size[1]):
            if imagen.getpixel((x, y)) <= u1 or imagen.getpixel((x, y)) >= u2:
                array[x, y] = 255
            else:
                array[x, y] = 0
    return tobase64(imagen)


def invbiumbral(url):
    imagen=Image.open(url).convert("L")
    u1=40
    u2=190
    array = imagen.load()
    for x in range(imagen.size[0]):
        for y in range(imagen.size[1]):
            if imagen.getpixel((x, y)) <= u1 or imagen.getpixel((x, y)) >= u2:
                array[x, y] = 255
            else:
                array[x, y] = 0
    return tobase64(imagen)

def escala_gris(url):
    imagen=Image.open(url)
    array = imagen.load()
    for x in range(imagen.size[0]):
        for y in range(imagen.size[1]):
            array[x,y] = imagen.getpixel((x,y))
            avg = sum(array[x,y]) // 3
            gris = (avg, avg, avg)
            array[x,y] = gris
    return tobase64(imagen)
    
def invescala_gris(url):
    imagen=Image.open(url)
    array = imagen.load()
    for x in range(imagen.size[0]):
        for y in range(imagen.size[1]):
            array[x,y] = imagen.getpixel((x,y))
            avg = sum(array[x,y]) // 3
            gris = (255-avg, 255-avg, 255-avg)
            array[x,y] = gris
    return tobase64(imagen)

def extension(url):
    imagen=Image.open(url).convert("L")
    u1=40
    u2=190
    array = imagen.load()
    for x in range(imagen.size[0]):
        for y in range(imagen.size[1]):
            if imagen.getpixel((x, y)) <= u1 or imagen.getpixel((x, y)) >= u2:
                array[x, y] = 255
            else:
                array[x, y] = (imagen.getpixel((x,y))-u1)*(255 // (u2-u1))
    return tobase64(imagen)

def nivelgrises(url):
    imagen=Image.open(url).convert("L")
    u1=15
    u2=50
    u3=75
    u4=92
    u5=130
    u6=170
    u7=195
    u8=225
    array = imagen.load()
    for x in range(imagen.size[0]):
        for y in range(imagen.size[1]):
            if imagen.getpixel((x, y)) <= u1:
                array[x, y] = 0
            elif imagen.getpixel((x, y)) > u1 and imagen.getpixel((x, y)) <= u2:
                array[x, y] = 30
            elif imagen.getpixel((x, y)) > u2 and imagen.getpixel((x, y)) <= u3:
                array[x, y] = 63
            elif imagen.getpixel((x, y)) > u3 and imagen.getpixel((x, y)) <= u4:
                array[x, y] = 85
            elif imagen.getpixel((x, y)) > u4 and imagen.getpixel((x, y)) <= u5:
                array[x, y] = 115
            elif imagen.getpixel((x, y)) > u5 and imagen.getpixel((x, y)) <= u6:
                array[x, y] = 150
            elif imagen.getpixel((x, y)) > u6 and imagen.getpixel((x, y)) <= u7:
                array[x, y] = 180
            elif imagen.getpixel((x, y)) > u7 and imagen.getpixel((x, y)) <= u8:
                array[x, y] = 210
            else:
                array[x, y] = 240
    return tobase64(imagen)

def tobase64(imagen):
    imagen.save("temp.jpg")
    with open("temp.jpg", "rb") as img_file:
        b64 = base64.b64encode(img_file.read())
    result=b64.decode('utf-8')
    print(result)
    return result
