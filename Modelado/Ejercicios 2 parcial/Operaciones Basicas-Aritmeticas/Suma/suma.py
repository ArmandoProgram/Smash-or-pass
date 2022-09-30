from PIL import Image
import time
def suma(im, alpha):
    tiempoIn = time.time()
    ruta = ("C:/Users/uziel/Documents/QuintoSemestre/" + im)
    im = Image.open(ruta)
    im.show()
    im12 = im
    i = 0
    while i < im12.size[0]:
        j = 0
        while j < im12.size[1]:
            valor = im12.getpixel((i, j))            
            valor = valor + alpha
            if valor >= 255:
                valor = 255
            else:
                valor = valor
            im12.putpixel((i, j),(valor))
            j+=1
        i+=1
    im12.show()
    tiempoFin = time.time()
    print('El Proceso Tardo: ', tiempoFin - tiempoIn, 'Segundos') 

suma("mapachegris.jpg",80)