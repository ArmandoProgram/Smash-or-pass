import cv2
import matplotlib.pyplot as plt
import numpy as np

def histograma():
    #Cargar imagen
    img = cv2.imread("mapache.jpg", cv2.IMREAD_GRAYSCALE)
    rows, columns = img.shape
    nivelesDeGris = np.zeros(256)    
    for x in range(0,rows):
        for y in range(0,columns):
            pixel = img[x][y]
            for ng in range(0,256):
                if pixel == ng:
                    nivelesDeGris[ng]= nivelesDeGris[ng]+1
    print (nivelesDeGris)
    plt.plot(nivelesDeGris,color="blue", linewidth=1.5, linestyle="-")
    plt.xlabel("Niveles de Gris")
    plt.ylabel("Numero de ocurrencias")
    plt.title("Histograma")
    plt.show()
    cv2.waitKey(0)
    cv2.destroyAllWindows()    
    return

histograma()