# Ejercicio 1
import cv2
import os

# Leer una imagen en color desde un archivo
imagenRu = 'ejercicio1.jpg'
imagen_color = cv2.imread(imagenRu)

if imagen_color is None:
    print("Error al cargar la imagen.")
    exit()

# Convertir la imagen a escala de grises
imagen_gris = cv2.cvtColor(imagen_color, cv2.COLOR_BGR2GRAY)

# Guardar la imagen en escala de grises en un archivo
imagengris = '...\clases-de-procesamiento\Examen-Final\imagen_gris.jpg'  
cv2.imwrite(imagengris, imagen_gris)

# Mostrar la imagen en escala de grises
cv2.imshow('Imagen en Escala de Grises', imagen_gris)
cv2.waitKey(0)
cv2.destroyAllWindows()