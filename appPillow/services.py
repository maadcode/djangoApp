from PIL import Image, ImageChops

def inverso(imagen):
    array = imagen.load()
    inv_array = ImageChops.invert(img)
    inv_array.show()

def umbral(imagen, u):
    array = imagen.load()
    for x in range(imagen.size[0]):
        for y in range(imagen.size[1]):
            if imagen.getpixel((x, y)) > u:
                array[x, y] = 255
            else:
                array[x, y] = 0
    return array

def invumbral(imagen, u):
    array = imagen.load()
    for x in range(imagen.size[0]):
        for y in range(imagen.size[1]):
            if imagen.getpixel((x, y)) > u:
                array[x, y] = 0
            else:
                array[x, y] = 255
    return array

def biumbral(imagen, u1, u2):
    array = imagen.load()
    for x in range(imagen.size[0]):
        for y in range(imagen.size[1]):
            if imagen.getpixel((x, y)) <= u1 or imagen.getpixel((x, y)) >= u2:
                array[x, y] = 255
            else:
                array[x, y] = 0
    return array

def invbiumbral(imagen, u1, u2):
    array = imagen.load()
    for x in range(imagen.size[0]):
        for y in range(imagen.size[1]):
            if imagen.getpixel((x, y)) <= u1 or imagen.getpixel((x, y)) >= u2:
                array[x, y] = 255
            else:
                array[x, y] = 0
    return array

def escala_gris(imagen):
    array = imagen.load()
    for x in range(imagen.size[0]):
        for y in range(imagen.size[1]):
            array[x,y] = imagen.getpixel((x,y))
            avg = sum(array[x,y]) // 3
            gris = (avg, avg, avg)
            array[x,y] = gris
    
def invescala_gris(imagen):
    array = imagen.load()
    for x in range(imagen.size[0]):
        for y in range(imagen.size[1]):
            array[x,y] = imagen.getpixel((x,y))
            avg = sum(array[x,y]) // 3
            gris = (255-avg, 255-avg, 255-avg)
            array[x,y] = gris

def extension(imagen, u1, u2):
    array = imagen.load()
    for x in range(imagen.size[0]):
        for y in range(imagen.size[1]):
            if imagen.getpixel((x, y)) <= u1 or imagen.getpixel((x, y)) >= u2:
                array[x, y] = 255
            else:
                array[x, y] = (imagen.getpixel((x,y))-u1)*(255 // (u2-u1))
    return array