# Ejercicio4
import cv2
from matplotlib import pyplot as plt

# Leer una imagen desde un archivo
imagen = cv2.imread('ejercicio4.jpg') 
# Aplicar un filtro de suavizado gaussiano con un kernel de 5x5
imagen_suavizada = cv2.GaussianBlur(imagen, (5, 5), 0)

# Mostrar la imagen original y la imagen suavizada
plt.subplot(121), plt.imshow(cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB))
plt.title('Imagen Original'), plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(cv2.cvtColor(imagen_suavizada, cv2.COLOR_BGR2RGB))
plt.title('Imagen Suavizada'), plt.xticks([]), plt.yticks([])

plt.show()

# Guardar la imagen suavizada
cv2.imwrite('imagen_suavizada.jpg', imagen_suavizada)
