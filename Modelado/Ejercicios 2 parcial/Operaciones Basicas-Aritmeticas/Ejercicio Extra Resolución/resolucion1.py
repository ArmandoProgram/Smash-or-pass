#Equipo:
#Nuñez Castellanos Amanda
#Lopez Ruiz Uziel Esau
#Armando Ayala Lujan
import cv2 
import matplotlib.pyplot as plt 
import numpy as np 
  
  
img1 = cv2.imread('mapache.jpg', 0) 
  
[m, n] = img1.shape 
print('Dimension de la imagen:', m, n) 
  
print('Imagen orinidal:') 
plt.imshow(img1, cmap="gray")
plt.show()
f = 3
img2 = np.zeros((m//f, n//f), dtype=np.int0)
for i in range(0, m, f): 
    for j in range(0, n, f): 
        try: 
  
            img2[i//f][j//f] = img1[i][j] 
        except IndexError: 
            pass
print('resolución baja:') 
plt.imshow(img2, cmap="gray") 
plt.show()
img3 = np.zeros((m, n), dtype=np.int16) 
for i in range(0, m-1, f): 
    for j in range(0, n-1, f):
        img3[i,j] = img2[i//f][j//f]

for i in range(1, m-(f-1), f): 
    for j in range(0, n-(f-1)): 
        img3[i:i+(f-1), j] = img3[i-1, j]
 
for i in range(0, m-1): 
    for j in range(1, n-1, f): 
        img3[i,j:j+(f-1)] = img3[i, j-1] 

print('Resoluciones de imagenes:') 
plt.imshow(img3, cmap="gray")
plt.show()