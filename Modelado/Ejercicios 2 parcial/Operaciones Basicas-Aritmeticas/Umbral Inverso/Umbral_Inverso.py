
#Equipo:
#Nuñez Castellanos Amanda
#Lopez Ruiz Uziel Esau
#Armando Ayala Lujan

from PIL import Image
import PIL.ImageOps


image = Image.open('mapache.jpg')
if image.mode == 'RGBA':
    r,g,b,a = image.split()
    rgb_image = Image.merge('RGB', (r,g,b))

    inverted_image = PIL.ImageOps.invert(rgb_image)

    r2,g2,b2 = inverted_image.split()

    final_transparent_image = Image.merge('RGBA', (r2,g2,b2,a))

    final_transparent_image.save('inverso_mapa.jpg')

else:
    inverted_image = PIL.ImageOps.invert(image)
    inverted_image.save('mapa_inverso.jpg')