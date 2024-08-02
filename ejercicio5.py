# Ejercicio5
import cv2
from matplotlib import pyplot as plt

# Leer una imagen en color
imagen_color = cv2.imread('ejercicio5.jpg') 

# Convertir la imagen a escala de grises
imagen_grises = cv2.cvtColor(imagen_color, cv2.COLOR_BGR2GRAY)

# Aplicar la ecualización de histograma
imagen_ecualizada = cv2.equalizeHist(imagen_grises)

# Mostrar la imagen original en grises y la imagen ecualizada
plt.subplot(121), plt.imshow(imagen_grises, cmap='gray')
plt.title('Imagen en Escala de Grises'), plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(imagen_ecualizada, cmap='gray')
plt.title('Imagen Ecualizada'), plt.xticks([]), plt.yticks([])

plt.show()

# Guardar la imagen ecualizada
cv2.imwrite('imagen_ecualizada.jpg', imagen_ecualizada)
