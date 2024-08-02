# Ejercicio2
import cv2
import numpy as np
from matplotlib import pyplot as plt

# Leer una imagen desde un archivo
imagen = cv2.imread('ejercico2.jpg', 0)

# Se aplica el detector de bordes de Canny
bordes = cv2.Canny(imagen, 100, 200)

# Mostrar la imagen original y la imagen con los bordes detectados
plt.subplot(121),plt.imshow(imagen, cmap = 'gray')
plt.title('Imagen Original'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(bordes, cmap = 'gray')
plt.title('Bordes con Canny'), plt.xticks([]), plt.yticks([])

plt.show()

# Guardar la imagen con los bordes detectados
cv2.imwrite('bordes_detectados.jpg', bordes)
