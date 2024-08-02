# Ejercicio3
import cv2
from matplotlib import pyplot as plt

# Leer una imagen desde un archivo
imagen = cv2.imread('ejercicio3.jpg') 

# Cambiar el tamaño de la imagen a 300x300 píxeles
imagen_redimensionada = cv2.resize(imagen, (300, 300))

# Mostrar la imagen original y la imagen redimensionada
plt.subplot(121), plt.imshow(cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB))
plt.title('Imagen Original'), plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(cv2.cvtColor(imagen_redimensionada, cv2.COLOR_BGR2RGB))
plt.title('Imagen Redimensionada'), plt.xticks([]), plt.yticks([])

plt.show()

# Guardar la imagen redimensionada
cv2.imwrite('imagen_redimensionada.jpg', imagen_redimensionada)
