#Equipo:
#Nuñez Castellanos Amanda
#Lopez Ruiz Uziel Esau
#Armando Ayala Lujan
from PIL import Image

foto=Image.open('mapache.jpg')

#si la imagen no es a escala de grises se hace la conversion
if foto.mode != 'L':
    foto=foto.convert('L')

#el umbral esta forzosamente comprendido entre 1 y 254 para las
#imagenes de 8 bits a escala de grises
umbral=65

datos=foto.getdata()
datos_binarios=[]

for x in datos:
    if x<umbral:
        datos_binarios.append(0)
        continue
    datos_binarios.append(1)

nueva_imagen=Image.new('1', foto.size)
nueva_imagen.putdata(datos_binarios)
nueva_imagen.save('inv_mapache.jpg')

nueva_imagen.close()
foto.close()